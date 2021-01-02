---
title: "Learning Rust"
date: 2020-11-11T20:47:48-06:00
draft: false
toc: false
images:
tags:
  - computer-science
  - rust
---

Hey there.

I didn't want to write yesterday because I was working on my project. In other news, I decided to learn a little bit of Rust through the [Official Rust Book](https://doc.rust-lang.org/stable/book/) since I used to play around with the C programming language. So far, I've found Rust to be an interesting language that remedies some of the problems with "unsafe" languages like C while still attempting to give access to the low level. 

Like C, Rust has `struct`s and `enum`s and it allows unsafe memory access through its "unsafe" mode. What I found quite interesting, however, was Rust's memory management system. Essentially, Rust remedies the issues of dangling references and data races through its concept of ownership. Essentially, every value in Rust has only **one** owner at a time. For example, in the code below:

`let x = 23;`

`x` is the owner of the value `23`. With primitive types like integers (which Rust determines through type inference) ownership isn't a huge problem since primitives are easily able to be copied from one value to another, but with heap-allocated data types (like `String`), the concept of ownership comes into play. Let's say I have the following:

```rust
fn main() {
  let s = String::from("Hello");
  let s2 = s;
  println!("{}", s);
}
```

Rust throws the following compilation error:

```
error[E0382]: borrow of moved value: `s`
 --> test.rs:4:18
  |
2 |   let s = String::from("Hello");
  |       - move occurs because `s` has type `std::string::String`, which does not implement the `Copy` trait
3 |   let s2 = s;
  |            - value moved here
4 |   println!("{}", s);
  |                  ^ value borrowed here after move

error: aborting due to previous error; 1 warning emitted

For more information about this error, try `rustc --explain E0382`.
```

Basically, this error is saying that `s` was not copied to `s2` (it doesn't implement the `Copy` trait — or interface — so Rust doesn't try to copy it), meaning instead it was *moved*. Initially, `s` pointed to "Hello", but after `s2` is assigned to `s`, it takes ownership of the value and the variable `s` will be invalidated. Thus, when we try to call the `println!` macro, the Rust compiler detects that the variable has been invalidated and avoids compiling. This avoids the issue of pointer aliasing and dangling references, which are all-too-common in C programs.

There's more I could talk about, but that's why there is an entire book on the subject. Hopefully, I'll write some Rust code in the future worth sharing. :) 