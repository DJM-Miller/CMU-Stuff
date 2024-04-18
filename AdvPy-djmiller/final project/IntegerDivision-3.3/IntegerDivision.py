from sys import stdin, stdout
from collections import Counter

def get_input():
    N,d = input().split()
    d = int(d)
    #input ints in list
    mylist = list(map(int, input().split()))
    return d, mylist

def intDivision(d, mylist):
    count = 0
    #find quotient
    for x in range(len(mylist)):
        mylist[x] = int(mylist[x]/d)
    #Map containing frequency of each value
    res = Counter(mylist)
   
    #calc total pairs based on frequency
    for x in res:
        n = res[x]
        count += int((n*(n-1))/2)   
        
    return count



if __name__ == "__main__":
    d, mylist = get_input()
    print(intDivision(d, mylist))