# [1,2,3,4]
# [24,12,8,6]

# def prodExceptSelf(inputArray):
#     finalArray = []
#     for num in inputArray:
#         final = 1
#         for secondNum in inputArray:
#             if num == secondNum:
#                 continue
#             final *= secondNum
#         finalArray.append(final)
#     return finalArray

def prodExceptSelf(inputArray):
    finalArray = []
    for num in inputArray:
        slic = inputArray[:num] + inputArray[num+1:]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(prodExceptSelf(arr))
print(arr[:2]+arr[2+1:])
