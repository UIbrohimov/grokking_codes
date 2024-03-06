simple_list = [0,1,2,3,4,5,6,7,8,9]

def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        # finding middle of an array
        mid = low + high

        # getting getting middle index of an array as a guess
        guess = array[mid]

        if guess == item:
            # if guess is the same as an element we are looking for
            # we just retur mid index
            return mid
        if guess > item:
            # if guess is bigger than the element we are looking for
            # we mark high point as mid - one, we just drop half part of an array
            high = mid - 1
        else:
            # if guess is smaller than the item we are looking for
            # we mark mid as starting point by dropping half part of an array 
            low = mid + 1

    return None

print(binary_search(array=simple_list, item=4))
print(binary_search(array=simple_list, item=-1))


