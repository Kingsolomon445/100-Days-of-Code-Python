# Using list comprehension to check for data overlap in two text files


file1 = [int(num.strip()) for num in open("file1.txt").readlines()]
file2 = [int(num.strip()) for num in open("file2.txt").readlines()]

result = [num for num in file1 if num in file2]
print(result)
