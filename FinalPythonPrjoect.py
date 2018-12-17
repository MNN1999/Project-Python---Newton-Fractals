#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:43:51 2018

@author: nabeel
"""

from scipy import *
from pylab import *
import sys

def f(x):
    return 6*x**5-5*x**4-4*x**3+3*x**2
def df(x):
    return 30*x**4-20*x**3-12*x**2+6*x


class fractal2D(object):
    def __init__(self,f,*args):
        self.function=f
        self.derivatefunction = args[0]
        self.zeros=[]
    def __Newton__(self,guess):
        x=guess
        tol = 1e-10
        for i in range(1010):
            y=x
            x=x-self.function(x)/self.derivatefunction(x)
            if abs(x-y)<tol:
                return x
        else:
            return "No conv detected"
    def __repr__(self):
        return ("({},{})".format(self.function,self.derivatefunction))
    def __inpoint__(self,xo):
        tol=1e-9
        x = self.__Newton__(xo)
        if x == "No conv detected":
            return "Special Value", "Have complex roots"
            
        for i in range(len(self.zeros)):
            if (abs(x-self.zeros[i])<tol):
                break
        else: 
            self.zeros.append(x)
            return len(self.zeros)
        
    def __plot__(self, N, a,b,c,d):
        xvalues = linspace(a,b,N)
        yvalues = linspace(c,d,N)
        X, Y = meshgrid(xvalues, yvalues)
        P=[]
        for i in range(N):
            for j in range(N):
                P.append(array([X[i,j],Y[i,j]]))
                
        P=fliplr(P)
        P=P.transpose()
        A=zeros(shape(P))
        k=0
        for i in range(len(P)):
            for j in range(len(P[0])):   
                A[i,j]=(self.__Newton__(P[i,j]))
                k+=1
        pcolor(A)
        

        
        
fractal = fractal2D(f,df)
print(fractal.__Newton__(5))
print(fractal.__inpoint__(99))
A=fractal.__plot__(100,-1,1,-1,1)


