def is_sorted(l):
    if(l == l.sort()):
        print("True")
    else:
        print(f"False")
    return f"The sorted list is {l}"   

l= list(map(int,input("Enter a list: ").split()))
print(is_sorted(l))