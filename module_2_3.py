my_list = [42,69,322,13,0,99,-5,9,8,7,-6,5]
len_ = len(my_list)
beg = 0
while beg < len_:
    if (my_list[beg]) > 0:
        print(my_list[beg])
    beg = beg + 1
    if beg == len_:
        break
    if (my_list[beg]) < 0:
        break