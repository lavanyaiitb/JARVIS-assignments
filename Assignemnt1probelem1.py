import numpy as np
from numpy import random
initarray = np.random.randint(100,size=(5,5))
print("Array obtained by random integres")
print(initarray)
# middle element of array
print("Middle element of the array:",initarray[2,2])

# Calculate the mean of each row
row_means = np.mean(initarray, axis=1)


# Print the means
print("Mean of each row:")
for i in range(len(row_means)):  # Iterate using index
    print(f"Row {i + 1}: {row_means[i]}")
    
#overall mean of array
x=np.mean(initarray)
print(x)

filterarray = initarray > x
new_array= initarray[filterarray]

print("NEW REQUIRED ARRAY")
print(new_array)

        
def numpy_spiral_order(matrix):
    result = []
    top, bottom = 0, matrix.shape[0] - 1
    left, right = 0, matrix.shape[1] - 1

    while top <= bottom and left <= right:
        # Traverse top row
        for col in range(left, right + 1):
            result.append(int(matrix[top, col]))#without int the output was not in proper array form eoth integers
        top += 1

        # Traverse right column
        for row in range(top, bottom + 1):
            result.append(int(matrix[row, right]))
        right -= 1

        if top <= bottom:
            # Traverse bottom row
            for col in range(right, left - 1, -1):
                result.append(int(matrix[bottom, col]))
            bottom -= 1

        if left <= right:
            # Traverse left column
            for row in range(bottom, top - 1, -1):
                result.append(int(matrix[row, left]))
            left += 1

    return result

# Call and print the result of spiral order traversal
spiral_order_result = numpy_spiral_order(initarray)
print("Spiral order traversal of the array:")
print(spiral_order_result)