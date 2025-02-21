# Bubble sort using python

# Changes in the bubble_sort.py files for understanding 

print("Enter the list to be sorted separated by spaces")
l = list(map(int, input().split()))

for h in range(len(l)):
    for i in range(len(l) - 1 - h):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]

print("Sorted list:", l)
