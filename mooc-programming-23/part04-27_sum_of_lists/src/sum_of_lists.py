# Write your solution here
def list_sum(a:list[int], b:list[int])->list[int]:
    sum_list = []

    for index in range(len(a)):
        sum_list.append(a[index]+b[index])
    return sum_list