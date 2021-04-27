# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/4/27 2:12 下午
# @Author  : changqingai
# @FileName: mergesort.py
# ----------------------------


def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    return merge(merge_sort(arr[0: middle]), merge_sort(arr[middle:]))


if __name__ == "__main__":
    # 归并排序
    arr = [9, 5, 7, 3, 1, 2, 0, 6, 4, 8]
    # output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    res = merge_sort(arr)
    print('result: ', res)
