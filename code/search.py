def linear_search(data, target):
    steps = 0
    for index in range(len(data)):
        steps += 1
        if data[index] == target:
            return index, steps
    return -1, steps


def binary_search(data, target):
    left = 0
    right = len(data) - 1
    steps = 0

    while left <= right:
        steps += 1
        middle = left + (right - left) // 2
        if data[middle] == target:
            return middle, steps
        if data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1, steps


if __name__ == "__main__":
    # ищем число, которого нет в списке
    print("n;linear;binary")
    for n in [8, 16, 32, 64, 128, 256, 512, 1024]:
        data = list(range(n))
        target = n
        linear_index, linear_steps = linear_search(data, target)
        binary_index, binary_steps = binary_search(data, target)
        print(f"{n};{linear_steps};{binary_steps}")
