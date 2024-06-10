import math

arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = float(input(f"Enter element {i + 1}: "))
    arr.append(element)
total_sum = sum(arr)
mean = total_sum / n
variance_sum = 0
for x in arr:
    variance_sum += (x - mean) ** 2
variance = variance_sum / n
deviation = math.sqrt(variance)
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Deviation: {deviation}")


