# Otter - Program made for educational intent, can be freely distributed
# and can be used for economical intent. I will not take legal actions
# unless my intelectual propperty, the code, is stolen or change without permission.  
#
# Copyright (C) 2020  VItor Hideyoshi Nakazone Batista
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import math
import numpy as np
import pandas as pd
import Seals

sl = Seals.process

class Algebra:

    def __init__(self, function):
        self.f = function
        self.integral = self.Integral(self.f)
        self.roots = self.Roots(self.f)
        self.edo = self.Edo(self.f)
    
    def d(self, x, e):
        return (self.f(x + e) - self.f(x - e))/(2*e)

    class Integral:

        def __init__(self,function):
            self.f = function
            self.simple = self.Simple(function)
            self.double = self.Double(function)
        
        class Simple:
            def __init__(self, function):
                self.f = function

            def riemann(self,a,b,n=None):
                
                if n is None:
                    n = 10**6

                delta = (b-a)/n

                psi = a
                theta = 0

                while((psi+delta) <= b):
                    
                    theta += (self.f(psi) + self.f(psi + delta))/2
                    psi += delta
                    
                integral = delta*theta

                return integral

            def simpson(self,a,b,n=None):

                if n is None:
                    n = 10**6

                def x(i):
                    return a + i*h

                h = (b-a)/n

                eta = 0
                theta = 0

                psi = 1
                kappa = 1

                while(psi <= (n/2)):

                    eta = eta + self.f(x(2*psi - 1))
                    psi = psi + 1

                while(kappa <= ((n/2)-1)):

                    theta = theta + self.f(x(2*kappa))
                    kappa = kappa + 1

                return (h/3)*( self.f(x(0)) + self.f(x(n)) + 4*eta + 2*theta)


        class Double:
            
            def __init__(self,function):
                self.f = function

            def riemann(self,a,b,c,d,n=None,m=None):
                
                if n is None:
                    n = 10**4

                if m is None:
                    m = n

                dx = (b-a)/n
                dy = (d-c)/m
                kappa = a
                psi = c
                theta = 0

                while((psi + dy) < d):

                    while((kappa + dx) < b):

                        theta = theta + self.f(kappa, psi)
                        kappa = kappa + dx

                    psi = psi + dy
                    kappa = a

                return theta*(dx)*(dy)

            def simpson(self,a,b,c,d,n=None,m=None):
                
                if n is None:
                    n = 10**4

                if m is None:
                    m = n

                dx = (b-a)/n
                dy = (d-c)/m
                
                def x(i):
    
                    x = a + i*dx
                    
                    return x

                def y(i):
                    
                    y = c + i*dy
                    
                    return y

                def g(i):
                    
                    sigma = 0
                    upsilon  = 0
                    
                    zeta = 1
                    csi = 1
                    
                    while(zeta <= (m/2)):
                        
                        sigma += self.f(x(i),y(2*zeta - 1))
                        zeta += 1
                        
                    while(csi <= ((m/2)-1)):
                        
                        upsilon  += self.f(x(i),y(2*csi))
                        csi += 1
                    
                    return (dy/3)*( self.f(x(i),y(0)) + self.f(x(i),y(m)) + 4*sigma + 2*upsilon )

                eta = 0
                theta = 0
                
                psi = 1
                kappa = 1
                
                while(psi <= (n/2)):
                    
                    eta += g(2*psi - 1)
                    psi += 1
                    
                while(kappa <= ((n/2)-1)):
                    
                    theta += g(2*kappa)
                    kappa += 1
                
                return (dx/3)*( g(0) + g(n) + 4*eta + 2*theta)

    class Roots:

        def __init__(self, function=None):
            if function is not None:
                self.f = function

        def bissec(self,a,b,e=None):

            if e is None:
                e = 10**(-6)

            fa = self.f(a)
            
            while abs(a-b) > e:
                
                c = (a+b)/2
                fc = self.f(c)
                
                if (fa*fc) < 0:
                    
                    b = c
                    
                else:
                    
                    a = c
                    fa = fc
                    
                c = (a+b)/2
                
                return c

        def d(self, x, e):
            return (self.f(x + e) - self.f(x - e))/(2*e)

        def newton(self,a,e=None):

            if e is None:
                e = 10**(-6)
            
            fa = self.f(a)
            da = self.d(a,e)
            b = a - fa/da
            
            
            while abs(a-b) > e:
                
                b = a
                a -= (fa/da)
                fa = self.f(a)
                da = self.d(a,e)
                
            return a

        def bissec_newton(self,a,b,e=None):

            if e is None:
                e = 10**(-6)
                
            fa = self.f(a)
            
            c = (a+b)/2                             # 'c' é a raiz calculada
            
            while abs(a-b) > 0.1:
                
                fc = self.f(c)
                
                if fa*fc < 0:
                    
                    b = c
                    
                else:
                    
                    a = c
                    fa = self.f(a)
                    
                c = (a+b)/2
                
            fc = self.f(c)
            dc = self.d(c,e)
            h = c - fc/dc                          # 'h' é uma variável de controle
            
            while abs(c-h) > e:
                
                h = c
                c -= (fc/dc)
                fc = self.f(c)
                dc = self.d(c,e)
                
            return (c)


    class Edo:

        def __init__(self, function):
            self.F = function

        def euler(self,a,y,b,n=None):

            if n is None:
                n = 10**6

            dx = (b-a)/n

            def x(i):
                return a + i*dx

            for i in range(n):

                y = y + (self.F(x(i),y))*dx
                
            return y

        def runge(self,a,y,b,n=None):

            if n is None:
                n = 10**6

            dx = (b-a)/n

            def x(i):
                return (a + i*dx)

            for i in range(n):

                y = y + (dx/2)*(self.F(x(i),y)+self.F(x(i+1),(y+(dx*self.F(x(i),y)))))
                
            return y

        def adams(self,a,y,b,n=None):

            if n is None:
                n = 10**6

            dx = (b-a)/n

            def x(i):
                return (a + i*dx)
            
            for i in range(n):

                f0 = self.F(x(i),y)
                f1 = self.F(x(i+1),y + dx*self.F(x(i)+(dx/2),y+(dx/2)*self.F(x(i),y)))
                f2 = self.F(x(i+2),y + (dx/2)*(3*f1-f0))
                
                y += (dx/12)*(5*f2 + 8*f1 - f0)

            return y

class Interpolation:
    """ Data should be organized in two columns: X and Y"""

    def __init__(self, data):

        self.data = data
        self.polinomial = self.Polinomial(self.data)

    def minimus(self,x):

        theta = 0
        # somatorio de x
        for i in range(self.data.shape[0]):

            theta += self.data.x[i]

        eta = 0
        #somatorio de y
        for i in range(self.data.shape[0]):

            eta += self.data.y[i]

        sigma = 0
        #somatorio de xy
        for i in range(self.data.shape[0]):

            sigma += self.data.x[i]*self.data.y[i]

        omega = 0
        #somatorio de x^2self.dself.dself.d
        for i in range(self.data.shape[0]):

            omega += self.data.x[i]**2


        self.a = (self.data.shape[0]*sigma - theta*eta)/(self.data.shape[0]*omega - (theta**2))

        self.b = (theta*sigma - eta*omega)/((theta**2) - self.data.shape[0]*omega)
        
        ym = 0

        for i in range(self.data.shape[0]):

            ym += self.data.y[i]/self.data.shape[0]

        sqreq = 0

        for i in range(self.data.shape[0]):

            sqreq += ((self.a*self.data.x[i] + self.b) - ym)**2

        sqtot = 0

        for i in range(self.data.shape[0]):

            sqtot += (self.data.y[i] - ym)**2

        self.r2 = sqreq/sqtot

        return self.a*x + self.b

    class Polinomial:

        def __init__(self, data):
            self.data = data

        def vandermonde(self, x):

            matrix = np.zeros((self.data.shape[0],self.data.shape[0]))
            
            for k in range(0, self.data.shape[0]):

                matrix[:,k] = self.data.x[:]**k 

            self.A = sl.gauss(np.c_[matrix,self.data[:,1]])
            
            y = 0

            for i in range(0,self.A.shape[0]):

                y += self.A[i]*(x**i)

            return float(y)

        def lagrange(self, x):

            def L(k,x):
        
                up = down = 1

                for i in [x for x in range(self.data.x.shape[0]) if x != k]:
                    up = up*(x - self.data.x[i])

                for i in [x for x in range(self.data.x.shape[0]) if x != k]:
                    down = down*(self.data.x[k] - self.data.x[i])

                return up/down

            y = 0

            for i in range(self.data.x.shape[0]):

                y += self.data.y[i]*L(i,x)

            return y

        def newton(self,x):
            
            d = np.array(np.zeros((self.data.shape[0],self.data.shape[0])))

            d[0] = self.data.y

            i = j = 0

            while (i < self.data.shape[0]):

                while (j < (self.data.shape[0]-(i+1))):

                    d[i+1][j] = (d[i][j+1] - d[i][j])/(self.data.x[(i+1)+j]-self.data.x[j])
                    j += 1
                
                i += 1
                j = 0
            
            def f(x):

                y = d[0][0]
                i = 0
                
                while ((i+1) < self.data.shape[0]):

                    mult = 1
                    k = 0
                    while (k <= i):
                        mult = mult*(x - self.data.x[k])
                        k += 1

                    y += d[i+1][0]*mult
                    i += 1

                return y

            self.f = f
            
            return f(x)

        def gregory(self,x):

            h = self.data.x[0] - self.data.x[1]
            
            d = np.array(np.zeros((self.data.shape[0],self.data.shape[0])))

            d[0] = self.data.y

            i = j = 0

            while (i < self.data.shape[0]):

                while (j < (self.data.shape[0]-(i+1))):

                    d[i+1][j] = (d[i][j+1] - d[i][j])/((i+1)*h)
                    j += 1
                
                i += 1
                j = 0
            
            y = d[0][0]
            i = 0
            
            while ((i+1) < self.data.shape[0]):

                mult = 1
                k = 0
                while (k <= i):
                    mult = mult*(x - self.data.x[k])
                    k += 1

                y += d[i+1][0]*mult
                i += 1

            return y   