# A simple program that add even numbers

even_list = [num for num in range(1, 101) if num % 2 == 0]
print(sum(even_list))