# Way 1
def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
n = int(input("Enter number: "))
print(sum_digits(n))


'''
1.
let n = 23 
s = 0 + 23 % 10 => 3
n = 23 // 10 => 2

2.
n = 2 
s = 3 + 2 % 10 => 3 + 0 => 3
n = 2 // 10 => 5
'''

# Way 2
n1 = int(input("Enter n1: "))
s = 0

for i in str(n):
    s = s + int(i)
print(s)

'''
1. let n = 56
i runs at str(56) -> '5'6' -> 0 and 1
s = 0 + 5 => 5
2.
s = 5 + 6 => 11
-> it prints 11
'''