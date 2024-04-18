def Modulo():
    input_list = []
    for x in range(10):
        input_list.append(input())
    print(uniqueModulo(input_list))


def uniqueModulo(mylist) -> int:
    myset = set()
    for x in mylist:
        myset.add(int(x)%42)
    return len(myset)




if __name__ == "__main__":
    Modulo()