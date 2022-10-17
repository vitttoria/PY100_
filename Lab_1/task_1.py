list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

unique_num = set(list_)

sum_num = sum(set(list_))
print(sum_num)

print(len(set(list_)))

unique_half = sum_num / len(set(list_))
print(round(unique_half, 5))