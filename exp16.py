def first_diff(s1,s2):
    if(len(s1) == len(s2)):
        for i in range(len(s1)):
            if(s1[i] == s2[i]):
                continue
            else:
                print(f"The different position is {i} and letter is {s2[i]}")            
        else:    
            return f"Strings are identical so returning -1"
    else:
        print("The both strings length is not equal")
                    
s1 = input("Enter s1: ") 
s2 = input("Enter s2: ") 
print(first_diff(s1,s2)) 