def answer():
    num = int(input())
    print(probs(num))

def probs(num:int) -> int:
    if(num < 149):
        return 99
    else:
        if(((num%100)-49) >= 0):
            return num + (99-num%100)
        else:
            return num - num%100 - 1


if __name__ == "__main__":
    answer()