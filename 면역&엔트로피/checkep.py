# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 16:17:41 2022

@author: kimse
"""

#findinstruction.py
#-*- coding: utf-8 -*-
from immlib import *
import math
 
def main(args):
    imm = Debugger()
    
    start = 0x401000
    end = 0x412fff
    count = 0
    
    #break_point_Addr = []
    #break_point_Addr += Set_breakPoint_Targets(imm, start, end)
    
    imm.run()
    while(True):
        if(not(imm.isRunning())):
            f_stream = read_Binary(imm, start, end)
            
            result_entropy = cal_Entropy(imm, 
                                         f_stream, 
                                         end-start)
            
            record_Entropy(imm.getRegs()['EIP'], 
                           result_entropy, 
                           count)
            count += 1
        if(imm.isFinished()):
            imm.quitDebugger()
        imm.run()



def Set_breakPoint_Targets(imm, start, end):
    
    jmp_list = imm.search('\xea') # 바이트 코드로 jmp인 주소를 모두 검색한다.
    jmp_list += imm.search('\xeb')
    jmp_list += imm.search('\xe9')
    jmp_list += imm.search('\xff')
    
    call_list = imm.search('\xe8') # 바이트 코드로 call 인 주소를 모두 검색한다.
    call_list += imm.search('\x9a')
    
    BP_list =[] #중단점 설정할 주소를 리스트에 저장한다.
    
    for i in jmp_list:
        if(i>=start and i<=end):
            BP_list.append(i)
            
    for i in call_list:
        if(i>=start and i<=end):
           BP_list.append(i)
    
    for i in BP_list: #log 창에 중단점 정보를 표시한다. 
        imm.log("- set BreakPoint at -->"+hex(i))
        imm.setBreakpoint(i)
    
    return BP_list
                

def read_Binary(imm, start, end):
    imm.log("read binary & wait a minutes...")
    file_byte_stream = imm.readMemory(start, end-start)
    return file_byte_stream    


def cal_Entropy(imm, file_stream, file_size):
    frequency = [0 for i in range(256)]
    
    for i in file_stream:
        for j in range(256):
           if(ord(i) == j):
               frequency[j] += 1
    
    sum_entropy = 0
    for i in range(256):
        if(frequency[i] != 0):
            sum_entropy += (float(frequency[i])/float(file_size)) * math.log(float(frequency[i])/float(file_size), 2)
            
    return sum_entropy * (-1)
    

def record_Entropy(addr_BP, entropy, count):
    with open("C:/Users/kimse/Desktop/record_entropy.txt",'a') as f:
        data = str(count) + " -> BP_addr : "+str(hex(addr_BP))+"  E : "+str(entropy)+'\n'
        f.write(data)
    f.close()
        
