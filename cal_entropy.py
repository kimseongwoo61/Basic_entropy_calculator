# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 06:06:27 2022

@author: kimse

파일의 엔트로피를 계산해보자!!!
"""

import math
import os


def entropy_cal(file_dir):
    f = open(file_dir, "rb")
    entropy = [0 for i in range(256)]
    
    for i in f.read():
        for j in range(256): #파일 바이너리의 빈도값을 분석한다.
            if(i == j):
                entropy[i] += 1
        
    print("- Byte Frequency")
    for i in range(256):
        if(entropy[i]==0):
            continue
        else:
            print(str(i)+" : "+str(entropy[i])) #바이트 빈도값을 출력한다.

    sum_entropy = 0
    size = os.path.getsize(file_dir)
    
    for i in range(256):
        if(entropy[i]!=0):
            sum_entropy += (entropy[i]/size) * math.log2(entropy[i]/size)
            #p(x) = entropy[i]/size
            #log2(p(x)) = math.log2(entropy[i]/size)
            #참고로 math.log2인자에 0이 들어가면 domain 에러 발생하므로 주의.
            
    print("Total ENTROPY : ",end='')
    print(sum_entropy * (-1))



if __name__ == "__main__":
    file_dir = str(input("파일 경로를 입력해 주세요. : "))
    entropy_cal(file_dir)
