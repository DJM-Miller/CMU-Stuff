def aDifProb():
    #loop continues as long as it continues to recieve input
    while True:
        try:
            x,y = input().split()
            print(findDifference(x,y))
        except:
            break

def findDifference(x,y):
    return abs((int(x)-int(y)))

if __name__ == "__main__":
    aDifProb()