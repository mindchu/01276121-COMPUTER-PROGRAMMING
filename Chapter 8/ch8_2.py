def bubble_sort(arr):
    sort_arr = arr.copy()
    sort_arr.sort()
    print(f"Normal sort :\n{sort_arr}")

def sort_avoid_negative_num(arr):
    positive_arr = []
    for num in arr:
        if num >= 0:
            positive_arr.append(num)
    positive_arr.sort()
    sort_arr = []
    arr_index = 0
    positive_index = 0
    for num in arr:
        if num >= 0:
            sort_arr.append(positive_arr[positive_index])
            arr_index += 1
            positive_index += 1
        else:
            sort_arr.append(arr[arr_index])
            arr_index += 1
    print(f"sort avoid negative number :\n{sort_arr}")

print("*** Sort avoid negative number ***")
number = list(map(int, input("Enter Input : ").split()))
bubble_sort(number)
sort_avoid_negative_num(number)
print("===== End of program =====")