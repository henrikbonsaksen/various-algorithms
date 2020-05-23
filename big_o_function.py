def my_function3(n):
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result = result + i * j * k
    return result
    