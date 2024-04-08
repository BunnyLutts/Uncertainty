from decimal import Decimal
from math import sqrt
from typing import Any

expr_t_95 = [0, 
             12.69, 4.271, 3.179, 2.776, 2.570, 
             2.447, 2.365, 2.306, 2.262, 2.228,
             2.201, 2.179, 2.160, 2.145, 2.131,
             2.120, 2.110, 2.101, 2.093, 2.086,]

def calcAvg(x):
    sum = 0
    for i in x:
        sum = sum+i
    return sum/len(x)

def calcSigma(x):
    avg = calcAvg(x)
    sum  = 0
    for i in x:
        sum = (sum+(avg-i)**2)
    return sqrt(sum/(len(x)-1))

def calcUncertainty(x, d, c):
    sigma = calcSigma(x)
    t = expr_t_95[len(x)]/sqrt(len(x))
    delta_a = sigma*t
    delta_b = d/c
    return sqrt(delta_a**2 + delta_b**2)

class ExpData:
    def __init__(self, avg, uncertainty):
        self.avg = avg
        self.u = uncertainty
    
    def __str__(self):
        return f"avg: {self.avg}, u: {self.u}, ur: {self.u/self.avg}"

    def __repr__(self):
        return f"avg: {self.avg}, u: {self.u}, ur: {self.u/self.avg}"
    
    def __add__(self, other):
        avg = self.avg + other.avg
        u = sqrt(self.u**2 + other.u**2)
        return ExpData(avg, u)

    def __sub__(self, other):
        avg = self.avg - other.avg
        u = sqrt(self.u**2 + other.u**2)
        return ExpData(avg, u)

    def __mul__(self, other):
        avg = self.avg*other.avg
        ur1 = self.u/self.avg
        ur2 = other.u/other.avg
        ur = sqrt(ur1**2 + ur2**2)
        u = ur*avg
        return ExpData(avg, u)
    
    def __truediv__(self, other):
        avg = self.avg/other.avg
        ur1 = self.u/self.avg
        ur2 = other.u/other.avg
        ur = sqrt(ur1**2 + ur2**2)
        u = ur*avg
        return ExpData(avg, u)
    
    def __pow__(self, other):
        avg = self.avg**other
        ur1 = self.u/self.avg
        ur = abs(ur1*other)
        u = ur*avg
        return ExpData(avg, u)


def genData(x:list, d, c=1.05):
    avg = calcAvg(x)
    u = calcUncertainty(x, d, c)
    return ExpData(avg, u)

def genOneData(x:float, d, c=1.05):
    avg = x
    u = d/c
    return ExpData(avg, u)

def cons(x) :
    return ExpData(x, 0)