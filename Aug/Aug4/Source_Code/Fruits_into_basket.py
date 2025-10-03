fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

fruit_count = {}
length = 0
left = 0

for right in range(len(fruits)):
    fruit = fruits[right]
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

    while len(fruit_count) > 2:
        left_fruit = fruits[left]
        fruit_count[left_fruit] -= 1
        if fruit_count[left_fruit] == 0:
            del fruit_count[left_fruit]
        left += 1

    length = max(length, right - left + 1)

print(length)
