print("TASK 1")

def maximum(*args):
    print(max(args))
maximum(23, 12, 556)

print("TASK 2")
def sum_num(a):
    total = 0
    for i in a:
        total += i
    print(total)
sum_num(a=[8, 2, 3, 0, 7])

print("TASK 2.1") # с несколькими списками
a = [8, 2, 3, 0, 7]
b = [1, 7, 89, 89]

def summall(iterable):
    result = 0
    for i in iterable:
        result += i
    print(result)

summall(a)
summall(b)

print("TASK 3")
def multi(c):
    total_1 = 1
    for i in c:
        total_1 *= i
    print(total_1)
multi(c=[8, 2, 3, -1, 7])

print("TASK 4")
def viceversa(ff):
    print(ff[::-1])
viceversa(ff=str('1234abcd'))

print("TASK 5")
def fff(n):
    if n == 0:
        return 1
    return fff(n - 1) * n


print(fff(5))


print("TASK 6")
text_text = input("Enter some text:")
low_c = 0
up_c = 0
for i in text_text:
      if(i.islower()):
            low_c += 1
      elif(i.isupper()):
            up_c += 1
print("Lowercase letters:", low_c)
print("Uppercase letter:", up_c)

print("TASK 7")
def palindrome(args):
    if args == args[::-1]:
        print(f'The word {args} is palindrome')
    else:
        print(f'The word {args} is not palindrome')
palindrome(args='flipp')
palindrome(args='казак')
palindrome(args='Anna')
palindrome(args='anna')

print("TASK 8")
def bank_income(x, y):
    return ((x * 0.1 * y)  + x)
x = float(input('first deposit:'))
y = int(input('years:'))


print(bank_income(x, y))


# print("TASK 9")
# nums = [45, 55, 60, 37, 100, 105, 220]
# new_lst = []
# def only_numbers(nums):
#     for i in nums:
#         if i % 15 == 0:
#             new_lst.append(i)
#     return new_lst



