# implementaion of linearsearch algoritham using python for basic understanding

def liserch(list, key, len):
    counter = 0  # Initialize a counter to keep track of the number of iterations

    for i in range(0, len):  # Iterate through each element in the list
        counter += 1  # Increment the counter

        if list[i] == key:  # Check if the current element matches the key
            return key, counter  # Return the key and the number of iterations taken

    return ("not in list")  # Return a message indicating that the key is not found in the list


if __name__ == "__main__":
    list = list(range(1, 101))  # Create a list from 1 to 100
    len = len(list)  # Get the length of the list
    key = int(input("please enter number which you want to search: "))  # Get the key from user input

result = liserch(list, key, len)  # Call the linear search function
print(result)  # Print the result to the console
