def second_largest_one(list_a):
    if len(list_a) <2:
        return -1

    set_list = list(set(list_a))

    set_list.sort(reverse = True)
    
    return set_list[1] if len(set_list) > 1 else -1


list_a = list(map(int,input().split()))

a = second_largest_one(list_a)
print(a)