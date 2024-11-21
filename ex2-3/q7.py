sum_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i
print(f"The sum of all even numbers between 1 and 100 is {sum_even}")