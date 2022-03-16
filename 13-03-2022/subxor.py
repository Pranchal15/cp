import re
import sys
from sys import stdin, stdout

def get_string(): return sys.stdin.readline().strip() 

def occurences(n,x):
    reg = r'(?=({}))'.format(x)
    return re.findall(reg,n)

def occurences_including_zero(n, x):
    reg = r'(?=(0+{}))'.format(x)
    return re.findall(reg,n)

def get_binary_representation(n):
    return bin(n).replace("0b", "")

t = int(stdin.readline())


def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0 
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal) 



while(t>0): 
    n = int(input())
    test_str = get_string() 
    dic = {} 
    str_bin_dic = {}

    number = binary_to_decimal(int(test_str))
    answer = 0
    for i in range(1, number+1):
        binary = get_binary_representation(i) 
        occurrence = occurences(test_str, str(binary) )
        occurence2 = occurences_including_zero(test_str, str(binary))
        if len(occurrence)%2!=0:
            answer = answer ^ i 
        if len(occurence2)%2!=0: 
            answer = answer ^i

    print(answer%998244353)
    t-=1