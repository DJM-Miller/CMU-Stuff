from itertools import combinations

def Perket(ing_list):
    #find all combinations
    combo_set = set()
    for i in range(len(ing_list)+1):
        for subset in combinations(ing_list,i):
            combo_set.add(subset)
    
    
    smallest_diff = 1000000000
    for combo in combo_set:
        temp_bitter = 0
        temp_sour = 1
        for ing in combo:
                temp_sour *= ing[0]
                temp_bitter += ing[1]
        if(smallest_diff > abs(temp_bitter - temp_sour)) and len(combo) > 0:
            smallest_diff = abs(temp_bitter-temp_sour)

    return smallest_diff



def get_ingredients():
    N = int(input())
    #input ingredient pairs
    ing_list = []
    for i in range(N):
        x,y = input().split()
        ing_list.append((int(x),int(y)))
    return ing_list      

    

if __name__ == "__main__":
    ing_list = get_ingredients()
    print(Perket(ing_list))