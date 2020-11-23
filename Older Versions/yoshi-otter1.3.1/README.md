# Otter - Numeric Calculus

This python package is made for applied Numeric Calculus of Algebra Functions. It is made with the following objectives in mind:

* Receive one variable function from user input
  
* Receive two variable function from user input

* Performe derivatives with one variable functions

* Performe integral with received functions

* Use methods to proccess the matrices.

* Find root of functions throw method of bissection and method of newton

* Solve Diferential Equations throw method of euler and runge

* Performe Minimus Interpolation and Polinomial Interpolation

## Syntax

To initialize a Otter instance linked to functions use the following syntax `otr = Otter.algebra(f)`, where `otr` will be a arbitrary name for the instance and `f` is a function of *one variable*.

To initialize a Otter instance linked to data and interpolation use the following syntax `otr = Otter.interpolation(data)`, where `otr` will be a arbitrary name for the instance and data will be a *numpy* matrix where the first columns has to contain the values for `x` and the second column contains the values for `y`.

### Algebra

Algebra is a Python Class where some of the features described previously are defined as Classes as well, like: `Integral`, `Roots`, `EDO` (diferential equations).

#### Integral

To call the class *Integral* append the sufix with lower case in front of the instance like: `otr.integral`. The Integral class has two other class defined inside, `Simple` and `Double`, to call them append the sufix with lower case in front as `otr.integral.simple` or `otr.integral.double`. Then pick between Riemann's Method or Simpson's Method by appending the sufix `riemann` or `simpson` as well.

After that the syntax will be something like `otr.integral.double.riemann(a,b,c,d,n,m)`, where `a` and `c` will be the first value of the interval of integration respectively in x and y, `b` and `d` will be the last, `n` and `m` will be the number of partitions.

The syntax for one variable integrations will be `otr.integral.simple.riemann(a,b,n)`.

If `n` is not defined the standart value in 10^6 partitions for one variable and 10^4 for double. And if `m` is not defined the standart value will be equal to `n`.

#### Roots

To call the class *Root* append the sufix with lower case in front of the instance like: `otr.roots`. The Roots class has three methods defined inside, `bissec`, `newton` and `bissec_newton`, to call them append the sufix with lower case in front as `otr.roots.bissec` or `otr.roots.newton` or even `otr.roots.bissecnewton`.

The syntax for the bissection method and bissec_newton is equal to `otr.roots.bissec(a,b,e)` and `otr.roots.bissec_newton(a,b,e)`, where `a` is the first element of the interval containing the root and `b` is the last, `e` being the precision.

The syntax for the newton method is equal to `otr.roots.newton(a,e)`, where `a` is the element closest to the root and `e` is the precision.

If `e` is not defined the standart value is 10^(-6).

#### Diferential Equations

To call the class *EDO* (*E*quações *D*iferenciais *O*rdinárias) append the sufix with lower case in front of the instance like: `otr.edo`. The *EDO* class has two methods defined inside: `euler` and `runge`, to call them append the sufix with lower case in front as `otr.edo.euler` or `otr.edo.runge`.

The syntax for the diferential equations method is equal to `otr.edo.euler(a,y,b,n)` or `otr.edo.runge(a,y,b,n)`, where `a` and `y` will be the inintial point  and `b` is the value in *x* which you want to know the corresponding value in *y* and `n` is the number of operations.

If `n` is not defined the standart value is 10^7.

### Interpolation

The python class *Interpolation* is divided in one method, minimus interpolation, and one class, polinomial interpolation.

To call the method *minimus* use a syntax like `otr = Otter.interpolation(data)`, where `data` is a data frame containing values for *x* and *y*, `otr` is an instance and append the method in front of the instance like: `otr.minimus(x)`, where *x* is value of *f(x)* you want to estimate.

To call the class *Polinomial* append the sufix with lower case in front of the instance like: `otr.polinomial`. The *Polinomial* class has four methods defined inside: `vandermonde`, `lagrange`, `newton` and `gregory`, to call them append the sufix with lower case in front like `otr.edo.gregory(x)` where *x* is value of *f(x)* you want to estimate.

## Installation

To install the package from source `cd` into the directory and run:

`pip install .`

or run

`pip install yoshi-otter`
