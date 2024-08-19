import random

random_numbers = [random.randint(1, 100) for _ in range(100)]

# with open("random_numbers.txt", "w") as f:
#     for number in random_numbers:
#         f.write(f"{number}\n")

with open("random_numbers.txt", "r") as f:
    count = 0
    for line in f:
        if int(line.strip()) % 2 == 0:
            count += 1

print(count)
