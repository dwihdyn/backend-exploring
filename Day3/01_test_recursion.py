# def power(num, n):
#     if n == 1:
#         return num
#     else:
#         return num * power(num, n-1)


# # print CANNOT be inside the function, because the ongoing loop is happening inside it, and print(power(num, n-1)) will kill the power() function
# print(power(4, 3))


'''
factorial(5) = 5 * 4 * 3 * 2 * 1
num * num-1 * num-2 * ..... * 1

fibonacci : 0,1,1,2,3,5,8,13,21

'''


# # factorial
# def factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num * factorial(num-1)


# print(factorial(5))


# # fibo - iterative
# def fibo_iter(len_of_seq):
#     seq = [0, 1]
#     # range(0,5) to create list of numbers from 0 to 4 [0,1,2,3,4] | -2 since we manually print out [0,1]
#     if len_of_seq == 0:
#         return []
#     elif len_of_seq == 1:
#         return [0]
#     else:
#         for i in range(len_of_seq - 2):
#             seq.append(seq[i] + seq[i+1])
#         return seq


# print(fibo_iter(5))


# fibo - recursive | try to find a way to print the whole array, like in fibo_iter()
def fibo_rec(len_of_seq):
    if len_of_seq == 0:
        return []
    elif len_of_seq == 1:
        return 0
    elif len_of_seq == 2:
        return 1
    else:
        return(fibo_rec(len_of_seq - 1) + fibo_rec(len_of_seq - 2))


print(fibo_rec(8))
