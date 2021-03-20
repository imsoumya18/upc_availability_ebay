# Q 3a
# x = []
# n = int(input('Enter no of numbers: '))
#
# for i in range(n):
#     no = int(input('Enter number' + str(i+1) + ': '))
#     if no%2 == 0:
#         x.append(no)
#
# print(x)


# Q 3b
# x = [2, 6, 5, 9]
# result = 1
#
# for i in x:
#     result *= i
#
# print('The result is: ' + str(result))


# Q 3c
# x = ['abc', 'xyz', 'aba', '1221']
# count = 0
#
# for i in x:
#     if len(i) >= 2 and i[0] == i[-1]:
#         count += 1
#
# print('No of such string(s): ' + str(count))


# Q 3d
# text = input('Enter a string: ')
# a, e, i, o, u = 0, 0, 0, 0, 0
#
# for t in text:
#     if t == 'a' or t == 'A':
#         a += 1
#     elif t == 'e' or t == 'E':
#         e += 1
#     elif t == 'i' or t == 'I':
#         i += 1
#     elif t == 'o' or t == 'O':
#         o += 1
#     elif t == 'u' or t == 'U':
#         u += 1
#
# print('No of vowels:')
# print('a/A: ' + str(a))
# print('e/E: ' + str(e))
# print('i/I: ' + str(i))
# print('o/O: ' + str(o))
# print('u/U: ' + str(u))


n = int(input('Enter no of employees: '))
name = []
basic = []
