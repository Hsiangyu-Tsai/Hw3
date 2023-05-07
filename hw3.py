demo = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
def quick_sort(demo, left, right): # 輸入資料，和從兩邊開始的位置
    if left >= right:              # 如果左邊大於右邊時就跳出function
        return
    i = left                      # 左指標
    j = right                     # 右指標
    pivot = demo[left]              # 基準點應擺的位置

    while i != j:
        while demo[j] > pivot and i < j:   # 從右邊開始找，找比基準點小的值
            j -= 1
        while demo[i] <= pivot and i < j:  # 從左邊開始找，找比基準點大的值
            i += 1
        if i < j:                        # 當左右指標沒有相遇時，swap
            demo[i], demo[j] = demo[j], demo[i]

    demo[left] = demo[i]
    demo[i] = pivot                # 基準點更改成兩指標相遇處

    quick_sort(demo, left, i-1)   # 處理兩邊的array
    quick_sort(demo, i+1, right)
quick_sort(demo, 0, len(demo)-1)
print(demo)