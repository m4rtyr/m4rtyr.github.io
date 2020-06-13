---
layout: post
title: Derivative of $\ln x$
date: 2020-06-13 16:08
summary: The derivative of $\ln x$ in two ways.
categories: mathematics
---

Finding the derivative of $\ln x$ is pretty simple. We start as usual, with a function $y$:

$$y = \ln x$$

$$x = e^y$$

Next, we take the derivative with respect to $x$:

$$\frac{d(e^y)}{dx} = 1$$.

Using the chain rule, we can find the derivative pretty easily. First, take the derivative of $e^y$ with respect to $y$ and then multiply that by the derivative of $y$ with respect to $x$:

$$\frac{d(e^y)}{dy} \cdot \frac{dy}{dx} = 1$$

$$e^y \cdot \frac{dy}{dx} = 1$$

$$\frac{dy}{dx} = \frac{1}{e^y}$$

$$\frac{dy}{dx} = \frac{1}{x}$$



The above is very expedient. However, it relies on the fact that we know the derivative of $e^x$. In fact, there is a way to find the derivative directly using the logarithmic series. 

$$y = \ln x$$

$$y + \Delta y = \ln(x + \Delta x)$$

$$\Delta y = \ln\biggl(\frac{x + \Delta x}{x}\biggl) = \ln\biggl(1 + \frac{\Delta x}{x}\biggl)$$

$$\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{\ln\biggl(1 + \frac{\Delta x}{x}\biggl)}{\Delta x}$$

$$\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{1}{\Delta x} \sum_{n=1}^\infty \frac{1}{n}\biggl(\frac{\Delta x}{x}\biggl)^n$$

$$\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \sum_{n=1}^\infty \frac{1}{n}\frac{(\Delta x)^{n-1}}{x^n}$$

$$\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim_{\Delta x \to 0} \frac{1}{x} + \sum_{n=2}^\infty \frac{1}{n}\frac{(\Delta x)^{n-1}}{x^n}$$

From here, on the RHS, the sum approaches zero as $\Delta x$ approaches $0$, and $\frac{1}{x}$ stays constant. As a result:

$$\frac{d(\ln x)}{dx} = \frac{1}{x}$$

