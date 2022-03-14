import re
import sys
from sys import stdin, stdout

def get_string(): return sys.stdin.readline().strip() 

def get_bin_rep(n):
    return bin(n).replace("0b", "")

def binary_to_decimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal) 
def find_all_occurrence(n,x):
    reg = r'(?=({}))'.format(x)
    return re.findall(reg,n)

def find_all_occurrence_zero(n, x):

    reg = r'(?=(0+{}))'.format(x)
    return re.findall(reg,n)
    

test_cases = int(stdin.readline())


while(test_cases>0): 
    n = int(input())
    test_str = get_string() 
    dic = {} 
    str_bin_dic = {}

    number = binary_to_decimal(int(test_str))
    ans = 0
    for i in range(1, number+1):
        binary = get_bin_rep(i) 
        occurrence = find_all_occurrence(test_str, str(binary) )
        occ_2 = find_all_occurrence_zero(test_str, str(binary))
        if len(occurrence)%2!=0:
            ans = ans ^ i 
        if len(occ_2)%2!=0: 
            ans = ans ^i

    print(ans%998244353)
    test_cases-=1