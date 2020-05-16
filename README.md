# Otter - Numeric Calculus

This python package is made for applied Numeric Calculus of Algebra Functions. It is made with the following objectives in mind:

* Receive one variable function from user input
  
* Receive two variable function from user input

* Performe derivatives with one variable functions

* Performe integral with received functions

* Use methods to proccess the matrices.

* Find root of functions throw method of bissection and method of newton

* Solve Diferential Equations throw method of euler and runge

* Performe Polinomial Interpolation and Minimus Interpolation

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

### Interpolation

The python class *process* has all the methods described in the first session.

To call the method use a syntax like `sl = Seals.process()`, where `sl` is an instance and to use a method you have to append the method in front of the instance like: `sl.identity(array)`.

* The method *identity* returns a *numpy* identity matrix of the order of the matrix passed into to it, and it has the following syntax `sl.identity(array)`, which `array` is a square matrix.

## Installation

To install the package from source `cd` into the directory and run:

`pip install .`

or run

`pip install otter`
