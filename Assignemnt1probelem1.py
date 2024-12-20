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
    init_row, final_row = 0, matrix.shape[0] - 1
    init_col, final_col = 0, matrix.shape[1] - 1

    while init_row <= final_row and init_col <= final_col:
        # Traverse top row
        for i in range(init_col, final_col + 1):
            result.append(int(matrix[init_row, i])) # without int the output was not in proper array form with integers
        init_row += 1

        # Traverse right column
        for j in range(init_row, final_row + 1):
            result.append(int(matrix[j, final_col]))
        final_col -= 1

        if init_row <= final_row:
            # Traverse bottom row
            for i in range(final_col, init_col - 1, -1):
                result.append(int(matrix[final_row,i]))
            final_row -= 1

        if init_col <= final_col:
            # Traverse left column
            for j in range(final_row, init_row - 1, -1):
                result.append(int(matrix[j, init_col]))
            init_col += 1

    return result

# Call and print the result of spiral order traversal
spiral_order_result = numpy_spiral_order(initarray)
print("Spiral order traversal of the array:")
print(spiral_order_result)
