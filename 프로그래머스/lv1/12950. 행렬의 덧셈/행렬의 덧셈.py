def solution(arr1, arr2):
    answer = []
    temp = []
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
        temp = []
    return answer