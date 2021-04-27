# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/4/27 4:30 下午
# @Author  : changqingai
# @FiarreName: qsort.py
# ----------------------------


def partition(arr, left, right):
    pivot_key = arr[left]
    while left < right:
        while left < right and arr[right] > pivot_key:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] < pivot_key:
            left += 1
        arr[right] = arr[left]
    arr[left] = pivot_key
    return left


def q_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        q_sort(arr, left, pivot - 1)
        q_sort(arr, pivot + 1, right)


def quick_sort(arr):
    q_sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    # 快速排序
    arr = [9, 5, 7, 3, 1, 2, 0, 6, 4, 8]
    # output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    quick_sort(arr)
    print('result: ', arr)
