def Alphabet(instring):
    missing = 26 - LIS(instring)
    return missing

#Longest increasing subsequence
def LIS(arr):
    n = len(arr)
    lis = [1]*n  #initialize all indexes to 1

    #Computed LIS bottom up
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    longest = 0
    for i in range(n):
        longest = max(longest,lis[i])
    
    return longest


if __name__ == "__main__":
    ins = input()
    print(Alphabet(ins))
