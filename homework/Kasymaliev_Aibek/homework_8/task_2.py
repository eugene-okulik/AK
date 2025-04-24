import sys


sys.set_int_max_str_digits(1000000)


first_num = 0
second_num = 1
fibonachi_list = [first_num, second_num]


while len(fibonachi_list) <= 100000:
    first_num = first_num + second_num
    second_num = first_num + second_num
    fibonachi_list.append(first_num)
    fibonachi_list.append(second_num)


print(fibonachi_list[4], fibonachi_list[199], fibonachi_list[999], fibonachi_list[99999])