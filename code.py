# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:50:09 2020

@author: N PRAFUL RAJ
"""

def bayes(p_e1,p_e2,p_a_e1,p_a_e2):
    p_e1_a=(p_e1*p_a_e1)/((p_e1*p_a_e1)+(p_e2*p_a_e2))
    return p_e1_a

p_e1=1/6
p_e2=5/6

p_a_e1=3/4
p_a_e2=1/4

result=bayes(p_e1,p_e2,p_a_e1,p_a_e2)

print("P(E1|A)=",result)
