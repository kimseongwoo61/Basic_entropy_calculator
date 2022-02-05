# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 18:12:34 2022

@author: kimse
"""
import matplotlib.pyplot as plt

def file_parser():
    x_count = [0 for i in range(3434)]
    y_E = [float(0) for i in range(3434)]
    BP_addr = [0 for i in range(3434)]
    index = 0
    i=0
    
    parsing_context = ''
    
    with open("C:/Users/kimse/Desktop/record_entropy.txt",'r') as f:
        while(True):
            parsing_context = f.readline()
            
            if(parsing_context == ''):
                f.close()
                break
            
            index = parsing_context.find(' ')
            x_count[i] = int(parsing_context[0:index])
            
            index = parsing_context.find('E : ')
            y_E[i] = float(parsing_context[index+4:(index+17)])
            
            index = parsing_context.find('BP_addr : ')
            BP_addr[i] = int(parsing_context[index+10:index+18],16)
            i +=1
            
    notDupl_BP, frequency_BP = delete_duplication(BP_addr)
    grape_Entropy(x_count, y_E, BP_addr, notDupl_BP, frequency_BP)
    
def delete_duplication(BP_addr):
    notDupl_BP = []
    
    for i in BP_addr:
        if i not in  notDupl_BP:
            notDupl_BP.append(i)
    
    frequency_BP = [0 for i in notDupl_BP]
    
    index = 0
    for i in notDupl_BP:
        for j in BP_addr:
            if(i == j):
                frequency_BP[index] += 1
        index += 1
    print(frequency_BP)
    print(notDupl_BP)
            
    return notDupl_BP, frequency_BP


           
def grape_Entropy(x_count, y_E, BP_addr, notDupl_BP, frequency_BP):
    plt.plot(x_count, y_E)
    plt.show()
    plt.plot(notDupl_BP, frequency_BP)
    plt.show()
    
    
    
      
file_parser()
            
        