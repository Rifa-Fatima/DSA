def sort(arr,k):
    if k >= len(arr):
        return sorted(arr)
    
    first_k = sorted(arr[:k])
    rest = sorted(arr[k:],reverse = True)
    return first_k + rest

my_list = [10,5,8,3,7,2,6,4,9,1]
k = 5
sorted_list = sort(my_list,k)
print(sorted_list)