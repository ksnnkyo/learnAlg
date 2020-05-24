def quick(quickList):
    data_len = len(quickList)
    if data_len >= 2:
        mid = quickList[0]
        left, right = [], []
        for i in range(1, data_len):
            if quickList[i] > mid:
                right.append(quickList[i])
            else:
                left.append(quickList[i])
        return quick(left) + [mid] + quick(right)

    else:
        return quickList


def quick_unit(unit_list, low, high):
    mid = unit_list[low]
    while low < high:
        while unit_list[high] >= mid and high > low:
            high = high - 1

        unit_list[low],  unit_list[high] = unit_list[high], unit_list[low]

        while unit_list[low] <= mid and low < high:
            low = low + 1

        unit_list[high], unit_list[low] = unit_list[low], unit_list[high]
    unit_list[low] = mid
    return high


def quick2(quickList, low, high):
    if low >= high:
        return
    mid_index = quick_unit(quickList, low, high)
    quick2(quickList, low, mid_index - 1)
    quick2(quickList, mid_index + 1, high)


if __name__ == "__main__":
    quickList = [3, 4, 1, 2, 5, 8, 0]
    print("Quick1 \n")
    print(quick(quickList))
    print("\n")
    print("Quick2 \n")
    quick2(quickList, 0, len(quickList) - 1)
    print(quickList)
