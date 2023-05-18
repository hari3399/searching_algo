# simple  binary serching algoritham for basic understanding 

def binsearch(ls, key):
    h = len(ls) - 1  # Initialize the upper bound of the search range
    l = 0  # Initialize the lower bound of the search range
    m = (l + h) // 2  # Calculate the middle index of the search range

    while l <= h:  # Continue the search until the lower bound exceeds the upper bound
        m = (l + h) // 2  # Recalculate the middle index

        if ls[m] == key:  # Check if the middle element is equal to the key
            return m  # Return the index where the key is found
        elif ls[m] < key:  # Check if the middle element is less than the key
            l = m + 1  # Adjust the lower bound to search the right half
        else:  # The middle element is greater than the key
            h = m - 1  # Adjust the upper bound to search the left half

    return -1  # Return -1 to indicate that the key is not found in the list


if __name__ == '__main__':
    ls = [1, 3, 5, 6, 11, 12, 34, 55, 66, 88]  # Sorted list for binary search
    key = 66  # Key to search for in the list

    result = binsearch(ls, key)  # Call the binary search function
    print(result) #printing results



             
