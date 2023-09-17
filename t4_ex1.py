numbers1 = {1:2, 2:3, 3:4, 4:5}
numbers2 = {
    value: key
    for key, value
    in numbers1.items()
}

print(numbers2)