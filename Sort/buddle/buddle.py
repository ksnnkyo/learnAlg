def buddle(buddleList):
    list_len = len(buddleList)
    if list_len == 1:
        return buddleList

    for i in range(list_len):
        flag = True
        for j in range(list_len - i - 1):
            if buddleList[j + 1] < buddleList[j]:
                buddleList[j], buddleList[j +
                                          1] = buddleList[j + 1], buddleList[j]
                flag = False

        if flag:
            break
    return buddleList


if __name__ == "__main__":
    bubbleList = [3, 4, 1, 2, 5, 8, 0]
    print(buddle(bubbleList))
