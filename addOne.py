# def addOne(digitsArr):
#     """
#     Given an array of single digits the array represents a full integer
#     So given [1,2,3] you need to add 1, you are not allowed to convert the whole thing
#     just add 1. If you are given [9] you need to make it [1,0].
#     """

#     # # reversed here lets you operate on the last index first proceeding downwards to the first i=0
#     # for i in reversed(range(len(digitsArr))):
#     #     # my inital thought was if it was 10 i needed to do something speical, but really 
#     #     if digitsArr[i] < 9:
#     #         digitsArr[i] += 1
#     #         return digitsArr
#     #     digitsArr[i] = 0
#     # return [1] + digitsArr
    


# print(addOne([1, 9]))   # [2, 0]
# print(addOne([9, 9]))   # [1, 0, 0]
# print(addOne([2, 3, 9])) # [2, 4, 0]
# print(addOne([1, 2, 3, 9])) # [1, 2, 4, 0]

# digitsArr = [9]

# for i in range(len(digitsArr)):
#     digitsArr[i] += 1

# print(digitsArr)

my_list = [1, 2, 3, 4]
my_list = [1, 9, 9, 9]
# my_list = [9,9]
def addOne(my_list):
    # for i in range(len(my_list) -1, -1, -1)):
    for i in reversed(range(len(my_list))):
        if my_list[i] < 9:
            my_list[i] += 1
            break
        else:
            my_list[i] = 0
            if i == 0:
                my_list = [1] + my_list
    return my_list

def addOneOpt(my_list):
    for i in reversed(range(len(my_list))):
        if my_list[i] < 9:
            my_list[i] += 1
            return my_list
        my_list[i] = 0
    return [1] + my_list

print(addOneOpt([8]))
# reversed_list = list(reversed_list_iterator)
# print(reversed_list)
# Output: [4, 3, 2, 1]
