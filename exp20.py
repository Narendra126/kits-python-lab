# def merge(l1,l2):
#     if(l1 == sorted(l1) and l2 == sorted(l2)):
#         a = l1 + l2
#         return f"The merged sorted list is {a}"
#     else:
#         l1.sort()
#         l2.sort()
#         a1 = l1 + l2
#         return f"After sorted and merged list is {a1}"           

# l1 = list(map(int,input("Enter l1: ").split()))
# l2 = list(map(int,input("Enter l2: ").split()))
# print(merge(l1,l2))

def merge(list1, list2):
    result = list1 + list2
    result.sort()
    return result
a = [1, 4, 6]
b = [2, 3, 5]

print(merge(a, b))

def merge(list1, list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    
    result += list1
    result += list2
    
    return result
a = [1, 4, 6]
b = [2, 3, 5]

print(merge(a, b))