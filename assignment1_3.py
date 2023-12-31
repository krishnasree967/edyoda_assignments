# Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers=[1,2,3,4,5,6,7,8,9]
even_num=0
odd_num=0
for x in numbers:
    if  x % 2 == 0 :
        even_num += 1
    else:
        odd_num += 1

print("number of even numbers:",even_num)
print("number of odd numbers:",odd_num)
