import random

total = 0
count = 20
even_count = 0


smallest = None
largest = None
second_smallest = None
second_largest = None

for i in range(count):
    num = random.randint(1, 100)
    print("Generated number:", num)


    total += num


    if num % 2 == 0:
        even_count += 1


    if smallest is None or num < smallest:
        second_smallest = smallest
        smallest = num
    elif second_smallest is None or num < second_smallest:
        second_smallest = num

    
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif second_largest is None or num > second_largest:
        second_largest = num

average = total / count

print("\nAverage:", average)
print("Smallest value:", smallest)
print("Largest value:", largest)
print("Second smallest value:", second_smallest)
print("Second largest value:", second_largest)
print("Number of even values:", even_count)

