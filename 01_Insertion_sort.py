array = [4, 6, 1, 2, 5, 8, 3]

def insertion_sort(array):
    """
    Complexity:
    Avg - O(n^2)
    Worst - O(n^2)
    Best - O(n)
    """
    for i in range(1, len(array)):
        key = array[i] # element which is going to be moved
        j = i -1 # begin at preceding number
        while j >= 0 and array[j] < key:
            #print(array)
            #input()
            array[j+1] = array[j] # shift all numbers to the right
            j = j -1 # by shifting iterator to left
        array[j + 1] = key # when correct place is found, insert number into empty spot
    return array

if __name__ == "__main__":
    print(insertion_sort(array))

