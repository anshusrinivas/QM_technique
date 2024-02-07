import pandas as pd
from pprint import *
import random


def min_to_binary(min_term):
    res_term=min_term
    if(min_term<0):
        return None
    res=''
    while(min_term!=0):
        res+=str(min_term%2)
        min_term=min_term//2
    r=[x for x in res]
    while len(r)<4:
        r.append('0')
    r.reverse()
    res=''
    for i in r:
        res+=i
    return {res:res_term}
def bin_sort(ip):
    count_dict={}
    for i in ip:
        temp_lis=list(i.keys())
        count=0
        for j in temp_lis[0]:
            if j=='1':
                count+=1
        count_dict.setdefault(count,[])
        count_dict[count].append(i)
    return count_dict
def compare1(ip1,ip2):
    ip1_key=[y[0] for y in (list(x.values()) for x in ip1)]
    ip1_val=[y[0] for y in (list(x.keys()) for x in ip1)]
    ip2_key=[y[0] for y in (list(x.values()) for x in ip2)]
    ip2_val=[y[0] for y in (list(x.keys()) for x in ip2)]
    n=4
    n_1=len(ip1)
    n_2=len(ip2)

    res_lis=[]
    action=0
    #print(f'{ip1_val}\n{ip1_key}\n{ip2_key}\n{ip2_val}\n{n}')
    for i in range(n_1):
        for j in range(n_2):
            count=0
            temp_1=ip1_val[i]
            temp_2=ip2_val[j]
            temp_res=''
            #print(f'{temp_1}\n{temp_2}')
            for z in range(len(temp_1)):
                if temp_1[z]!=temp_2[z]:
                    temp_res+='_'
                    count+=1
                else:
                    temp_res+= temp_1[z]
            if count==1 and type(ip1_key[i])==int and type(ip2_key[j])==int:
                res_lis.append({temp_res:[ip1_key[i],ip2_key[j]]})
                action+=1
            elif count==1 and type(ip1_key[i])==list and type(ip2_key[j])==list:
                res_lis.append({temp_res:ip1_key[i]+ip2_key[j]})
                action+=1
    if action!=0:
        return res_lis
    else:
        return None




min_lis=set(map(int,input().split()))
#min_lis={random.randint(0,15) for x in range(10)}
#min_lis=[0, 1, 3, 7, 8, 9, 10, 12, 13]
min_lis=list(min_lis)
binary_d=[]
for i in min_lis:
    binary_d.append(min_to_binary(i))

sort_dict=bin_sort(binary_d)
try:
    min_0=sort_dict[0]
except:
    pass
try:
    min_1=sort_dict[1]
except:
    pass
try:
    min_2=sort_dict[2]
except:
    pass
try:
    min_3=sort_dict[3]
except:
    pass
try:
    min_4=sort_dict[4]
except:
    pass
print(min_lis,end='\n')
'''pprint(binary_d)
print()
pprint(sort_dict)
print()'''
#print(f"{min_1}\n{min_2}\n{min_3}")
try:
    com0_1=compare1(min_0,min_1)
except:
    pass
try:
    com1_2=compare1(min_1,min_2)
except:
    pass
try:
    com2_3=compare1(min_2,min_3)
except:
    pass
try:
    com3_4=compare1(min_3,min_4)
except:
    pass
'''try:
    pprint(com0_1)
    print()
except:
    pass
try:
    pprint(com1_2)
    print()
except:
    pass
try:
    pprint(com2_3)
    print()
except:
    pass

try:
    pprint(com3_4)
    print()
except:
    pass'''

try:
    com3=compare1(com0_1,com1_2)
except:
    pass

try:
    com4=compare1(com1_2,com2_3)
except:
    pass
try:
    com6=compare1(com3,com4)
except:
    pass
#print('\n\n\n')
'''try:
    pprint(com3)
    print()
except:
    pass

try:
    pprint(com4)
    print('\n\n\n\n')
except:
    pass
try:
    pprint(com6)
except:
    pass'''

# to find prime implicants
p_imp=[]
p_imp_bin=[]
try:
    for i in com4:
        for x in i.values():
            p_imp.append(x)
        for x in i.keys():
            p_imp_bin.append(x)
except:
    pass
try:
    for i in com3:
        for x in i.values():
            p_imp.append(x)
        for x in i.keys():
            p_imp_bin.append(x)
except:
    pass

flag=1
p_imp_bin=set(p_imp_bin)
p_imp_bin=list(p_imp_bin)
remai_lis=min_lis

for i in p_imp:
    for j in i:
        if j in remai_lis:
            remai_lis.remove(j)

if remai_lis:
    try:
        for i in com3_4:
            for x in i.values():
                for y in x:
                    if y in remai_lis:
                        p_imp.append(x)
                        for z in i.keys():
                            p_imp_bin.append(z)
        for i in p_imp:
            for j in i:
                if j in remai_lis:
                    remai_lis.remove(j)
    except:
        pass
        
if remai_lis:
    try:
        for i in com2_3:
          for x in i.values():
            for y in x:
                if y in remai_lis:
                    p_imp.append(x)
                    for z in i.keys():
                        p_imp_bin.append(z)
        for i in p_imp:
            for j in i:
                if j in remai_lis:
                    remai_lis.remove(j)
    except:
        pass
if remai_lis:
    try:
        for i in com1_2:
          for x in i.values():
            for y in x:
                if y in remai_lis:
                    p_imp.append(x)
                    for z in i.keys():
                        p_imp_bin.append(z)
        for i in p_imp:
            for j in i:
                if j in remai_lis:
                    remai_lis.remove(j)
    except:
        pass

if remai_lis:
    try:
        for i in com0_1:
          for x in i.values():
            for y in x:
                if y in remai_lis:
                    p_imp.append(x)
                    for z in i.keys():
                        p_imp_bin.append(z)
        for i in p_imp:
            for j in i:
                if j in remai_lis:
                    remai_lis.remove(j)
    except:
        pass

p_imp_bin=set(p_imp_bin)
p_imp_bin=list(p_imp_bin)
print(f'prime imp={p_imp}\n bin={p_imp_bin}')
print(f'remaining={remai_lis}')
