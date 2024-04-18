def answer():
    x = input()
    print(howlBack(len(x)))
    
def howlBack(length:int):
    myhowl = "AWAWHO" + 'O'*(length-5)
    return myhowl



if __name__ == "__main__":
    answer()