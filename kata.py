# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

# Let's see some memos

def snail(snail_map):
    tail = list()
    while True:
        # Move right
        if snail_map:
            for number in snail_map[0]:
                tail.append(number)
            del snail_map[0]
        else:
            return tail
        # Move down
        if snail_map:
            for i in range(len(snail_map)):
                number = snail_map[i][-1]
                tail.append(number)
                del snail_map[i][-1]
        else:
            return tail
        # Move left
        if snail_map:
            for i in range(len(snail_map[-1])):
                number = snail_map[-1][-1]
                tail.append(number)
                del snail_map[-1][-1]
            del snail_map[-1]
        else:
            return tail
        # Move up
        if snail_map:
            for i in range(len(snail_map), 0, -1):
                number = snail_map[i-1][0]
                tail.append(number)
                del snail_map[i-1][0]
        else:
            return tail