'''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is 
the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

def fibonnaci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    f_previous = fibonnaci(n-1)
    # print(f_previous)
    return f_previous + [sum(f_previous[-2:])]

# def fibonnaci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     return fibonnaci(n-1) + fibonnaci(n-2)

# def fibonnaci(n):
#     if n == 1:
#         return [1]
#     f_list = [1, 1]

#     # f_previous = 1
#     # f_next = 1    
#     # for i in range(2, n):
#     #     f_temp = f_next 
#     #     f_next += f_previous
#     #     f_previous = f_temp
#     #     f_list.append(f_next)

#     for i in range(2, n):
#         f_list.append(f_list[i-2] + f_list[i-1])

#     return f_list

num = int(input('Give the number (>=1): '))
while num < 1:
    num = int(input('Give the number (>=1): '))
res = fibonnaci(num)
print(res)
