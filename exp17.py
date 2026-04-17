def number_of_factors(n):
    count= 0
    for i in range(1,n+1):
        if(n / i):
            print(i)
            count +=1
    return f"The count of n is {count}"       


n = int(input("Enter n: "))
print(number_of_factors(n))    