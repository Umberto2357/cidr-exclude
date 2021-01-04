# coding:utf-8
# @Date    : 2020-08-23
# @Author  : ruby1
# @Version : 1.2 
# @Release Note: correct large prefix merge error

import ipaddress
import netaddr 

def prepList(listn):
    fileInput = open(listn)
    listprep = []
    #fileInput = open("cidrInput.txt")
    for line in fileInput:
        line = line.rstrip()
        i = ipaddress.ip_network(line)
        listprep.append(i)
    return listprep

def cidrExclude(list1, list2):
    newAdd = []
    cidrOutput = []
    cidrOutputMerge = []
    i=0
    while i < len(list1):
        overlap = 0
        newAdd = []
        for j in range(len(list2)): 
            if list1[i].overlaps(list2[j]):
                overlap = 1
                if list1[i].supernet_of(list2[j]):
                    newAdd = list(list1[i].address_exclude(list2[j]))
                    newAdd.sort()
                    list1=list1[:i+1]+newAdd+list1[i+1:]            
                    break
        if overlap == 0:
            print("Output",list1[i],"\n")
            cidrOutput.extend(list1[i])
        i+=1


    cidrOutputMerge = ipaddress.collapse_addresses(cidrOutput)
    fileOutput = open("cidrOutput.txt", "w")
    for iprange in cidrOutputMerge:
        fileOutput.write("".join(str(iprange)))
        fileOutput.write("\n")

if __name__ == '__main__':
    list1 = prepList("cidrInput.txt")
    list2 = prepList("cidrExclude.txt")
    cidrExclude(list1, list2)




