music_play_count = {
    'Rock': 3,
    'Paper': 4,
    'Scissors': 5,
    'Lizard': 432,
    'Spock': 0,
}

# write function for sort musci_play_count doctionary with quicksort
def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    
    return smallestIndex


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def sortMusicList(data):
    sortedMusic = {}
    sortedValues = selectionSort(list(data.values()))
    for item in sortedValues:
        for key, value in data.items():
            if item == value:
                sortedMusic[key] = value

    return sortedMusic

print(sortMusicList(music_play_count))


