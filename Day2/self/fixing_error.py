# Error 1
def mean(*numbers):
    # print(type(numbers))
    avg = sum(numbers) / len(numbers)
    return avg


mean(5, 3, 4, 5, 6, 4)
