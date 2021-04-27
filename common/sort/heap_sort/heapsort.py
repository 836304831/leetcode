# -*- coding: utf-8 -*-
# ----------------------------
# @Time    : 2021/4/27 10:42 上午
# @Author  : changqingai
# @FileName: heapsort.py
# ----------------------------


def _swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def _heap_adjust(arr, i, n_len):
    left_index = i * 2 + 1
    right_index = i * 2 + 2
    min_index = i

    if left_index < n_len and arr[left_index] < arr[min_index]:
        min_index = left_index
    if right_index < n_len and arr[right_index] < arr[min_index]:
        min_index = right_index

    if min_index != i:
        _swap(arr, i, min_index)
        _heap_adjust(arr, min_index, n_len)


def build_heap(arr):
    i = len(arr) // 2 - 1
    while i >= 0:
        _heap_adjust(arr, i, n_len=len(arr))
        i -= 1
    print('middle arr: ', arr)


def heap_sort(arr):
    build_heap(arr)
    n = len(arr)
    for i in range(1, n):
        _swap(arr, 0, n - i)
        _heap_adjust(arr, 0, n - i)
    print('sorted:', arr)


if __name__ == "__main__":
    # 小根堆，从大到小排序
    arr = [9, 5, 7, 3, 1, 2, 0, 6, 4, 8]
    # output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    heap_sort(arr)
