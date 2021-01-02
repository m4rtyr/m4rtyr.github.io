---
title: "Getting a MAC Address on a Mac"
date: 2020-11-23T20:33:28-06:00
draft: false
toc: false
images:
tags:
  - computer-science
  - c
  - networking
---

Hey there.

Recently, I needed to write some code in C to get the MAC address of a particular interface. On Linux, this is pretty easy to do. However, on BSD systems and, more importantly, on macOS, it wasn't as straightforward and I had to do some digging to find an answer.

On Linux, generally I would find the MAC address by doing an `ioctl()` call with the argument `SIOCGIFHWADDR` like so:

```c
{
  /* --snip-- */
  struct ifreq ifr = { 0 };
  strncpy(&ifr.ifr_addr, interface_name, sizeof(ifr.ifr_addr));
  if (ioctl(fd, SIOCGIFHWADDR, &ifreq) < 0) {
    /* Error */
  }
  // Now the hardware address can be accessed in ifr_hwaddr
}
```

However, on macOS, the code isn't as compact. I won't keep you waiting, so here's the code:

```c
int mib[6] = { CTL_NET, AF_ROUTE, 0, AF_LINK, NET_RT_IFLIST, 0 };
size_t len = 0;
mib[5] = if_nametoindex(interface);
if (!mib[5]) {
      /* Error */
}
if (sysctl(mib, 6, NULL, &len, NULL, 0) < 0) {
     /* Error */
}

char *buf = calloc(1, len);
if (!buf) {
    /* Error */
}
if (sysctl(mib, 6, buf, &len, NULL, 0) < 0) {
    /* Error */
}

struct if_msghdr *ifm = (struct if_msghdr *) buf;
struct sockaddr_dl *sdl = (struct sockaddr_dl *)(ifm + 1);
u_char *src = (u_char *) LLADDR(sdl);
```

...

As someone who has written stuff for Linux machines, this wasn't super out there. But I needed to look at each line step by step to understand it. Before I do that though, I want to talk a little bit about `sysctl()`. As the man page for it says:

>The sysctl() function retrieves system information and allows processes with appropriate privileges to set system information.  The information available from sysctl() consists of integers, strings, and tables.  Information may be retrieved and set from the command interface using the sysctl(8) utility.

So as far as I understand, it's basically like `ioctl()`, which is weird since you can also call `ioctl()` on macOS as well. `sysctl()` operates on multiple "levels". These levels describe the operation you're trying to execute (in code, you use an array — in this case, we use the array `mib` — to represent the different levels we are accessing). At the top level is the "type" of operation you're trying to execute:

| Name        | Next level names | Description                     |
| ----------- | ---------------- | ------------------------------- |
| CTL_DEBUG   | sys/sysctl.h     | Debugging                       |
| CTL_VFS     | sys/mount.h      | File system                     |
| CTL_HW      | sys/sysctl.h     | Generic CPU, I/O                |
| CTL_KERN    | sys/sysctl.h     | High kernel limits              |
| CTL_MACHDEP | sys/sysctl.h     | Machine dependent               |
| CTL_NET     | sys/socket.h     | Networking                      |
| CTL_USER    | sys/sysctl.h     | User-level                      |
| CTL_VM      | sys/resources.h  | Virtual memory (struct loadavg) |

Since we're looking for the hardware address, let's look under the `CTL_NET` level. The second level appears to detail the  particular network layer we're interested in. There's three layers: `PF_ROUTE`, `PF_INET`, and `PF_INET6`. `PF_INET*` deals with the internet layer (so IP addresses) while `PF_ROUTE` deals with the routing table.  Referring to the manual:

> [PF_ROUTE — ] Return the entire routing table or a subset of it.  The data is returned as a sequence of routing messages (see route(4) for the header file, format and meaning).  The length of each message is contained in the message header. The third level name is a protocol number, which is currently always 0.  The fourth level name is an address family, which may be set to 0 to select all address families.  The fifth, sixth, and seventh level names are as follows:
>
> | Fifth level     | Sixth level   | Seventh Level      |
> | --------------- | ------------- | ------------------ |
> | NET_RT_FLAGS    | rtflags       | None               |
> | NET_RT_DUMP     | None          | None or fib number |
> | NET_RT_IFLIST   | 0 or if_index | None               |
> | NET_RT_IFMALIST | 0 or if_index | None               |
> | NET_RT_IFLIST   | 0 or if_index | None               |

OK, so the third level is always zero, so we don't need to worry about that...the fourth level is an address family. Considering we're interested in a hardware address, we're interested in the *link layer*, so we should probably consider using `AF_LINK`. The fifth level is **really** what we're interested in. `NET_RT_IFLIST` is the key here: it returns information about interfaces (`NET_RT_IFMALIST` is for multicast addresses and frankly I don't even know what `NET_RT_IFLISTL` is for). The sixth level allows us to narrow our target. By default, `NET_RT_IFLIST` will return information about a list of interfaces, but if we give it a specific interface (via an interface *index number*), it will return information about that particular interface.  Thus, the snippet:

```c
int mib[6] = { CTL_NET, AF_ROUTE, 0, AF_LINK, NET_RT_IFLIST, 0 };
size_t len = 0;
mib[5] = if_nametoindex(interface);
if (!mib[5]) {
      /* Error */
}
/* --snip-- */
```

Is actually pretty easy to follow. In the array `mib`, we specify that we want to:

1. Do a network operation (`CTL_NET`)
2. Access the routing table (`AF_ROUTE`)
3. — this is probably reserved for something in the future, idk, but we need to specify it anyway — (`0`)
4. Access the link layer (`AF_LINK`)
5. Get information about interfaces (`NET_RT_IFLIST`)
6. Get information about a particular interface (`0`)

You might notice that in the last part of the array, I initialize the value to `0`. The reason is that we can't just provide the interface as a string name. Instead, we must get the index of the interface, a unique numerical value that identifies an interface. To do this, we use the `if_nametoindex()` sys-call and set the sixth entry of the array to that index.



Whew! Now, we just need to make a call to `sysctl()`...twice? 

```c
if (sysctl(mib, 6, NULL, &len, NULL, 0) < 0) {
     /* Error */
}

char *buf = calloc(1, len);
if (!buf) {
    /* Error */
}
if (sysctl(mib, 6, buf, &len, NULL, 0) < 0) {
    /* Error */
}
```

 OK, so to explain what's happening here, let's consult the manual page (for the third time):

> ```
> int
> sysctl(int *name, u_int namelen, void *oldp, size_t *oldlenp, void *newp, size_t newlen);
> ```
>
> ...
>
> The information is copied into the buffer specified by oldp.  The size of the buffer is given by the location specified by oldlenp before the call, and that location gives the amount of data copied after a successful call and after a call that returns with the error code ENOMEM.  
>
> If the amount of data available is greater than the size of the buffer supplied, the call supplies as much data as fits in the buffer provided and returns with the error code ENOMEM.  If the old value is not desired, oldp and oldlenp should be set to NULL. The size of the available data can be determined by calling sysctl() with the NULL argument for oldp.  The size of the available data will be returned in the location pointed to by oldlenp. For some operations, the amount of space may change often.  For these operations, the system attempts to round up so that the returned size is large enough for a call to return the data shortly thereafter.

Basically, before the data is copied into `oldp` the size of the buffer needs to be calculated first. Therefore, we let `sysctl()` do this for us by giving the operation we want to do with `sysctl()` (`mib`), the length of the instructions list, and then provide a pointer to the `len` variable while setting everything else to `NULL ` and `0` in the argument list. Once we do that, `sysctl()` looks at the list of instructions we provided and determines how much space will need to be allocated for the resultant data and then stores that calculated value in `len`. Thus, we can allocate a region of bytes of size `len` called `buf` which, if we pass to `sysctl()` again, will be filled with the resultant data.

Now, we need to parse this region of bytes to get the hardware address. The `struct if_msghdr` is used specifically for storing information about interfaces. Thus, you can simply cast the array of bytes to get the interface information in a readable format. Then, to get the hardware address, we cast the `struct if_msghdr` to a `struct sockaddr_dl` so we can directly access the hardware address...kinda:

```c
struct if_msghdr *ifm = (struct if_msghdr *) buf;
struct sockaddr_dl *sdl = (struct sockaddr_dl *)(ifm + 1);
```

In the original post I found this in, I couldn't find an explanation for the reason to add `1` to `ifm`. It's likely that the 0th index is reserved for some other type of information, though I don't really know at this point. The last step was to take `sdl` and convert it to a series of bytes representing a hardware address. By using the `LLADDR` macro, we can obtain the MAC address of the interface as a series of bytes:

```
u_char *src = (u_char *) LLADDR(sdl);
```

To explain what's going on above, let's examine the `LLADDR` macro:

```c
#define LLADDR(s) ((caddr_t)((s)->sdl_data + (s)->sdl_nlen))
```

OK...so this doesn't tell us much. To save time, I'll tell you what's going on: in the `struct sockaddr_dl`, there's a field called `sdl_data` which contains both the interface name and the link layer address (in that order). Since we don't know how long the interface name is, the structure also has a field named `sdl_nlen` which contains the length of the interface name. Thus, by advancing `sdl_nlen` bytes through `sdl_data`, we obtain a `char *` with the interface address (this is cast to the type `caddr_t`, so we need to cast it back to a `char *` or any other byte-sized type in order to obtain the hardware address).

So yeah...that was a lot of hassle to explain a pretty simple operation. It's weird that there's so little documentation there is on this, considering that this is a pretty common low-level network operation. 