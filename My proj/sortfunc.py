def buble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True

nums1 = list(map(int, input('Введите числа через пробел:').split()))
buble_sort(nums1)
print(nums1)

def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
            ls[i], ls[lowest] = ls[lowest], ls[i]

nums2 = list(map(int, input('Введите числа через пробел:').split()))
selection_sort(nums2)
print(nums2)