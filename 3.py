from random import randint

l1 = [randint(1, 100) for num in range(1000)]
i = 0
num_to_search = 25
while i < len(l1):
    if l1[i] == num_to_search:
        print(f"{num_to_search} found at index {i}")
        break
    i += 1
