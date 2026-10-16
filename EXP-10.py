import numpy as np

# Create an array
array = np.random.randint(1, 100, 9)

print("Original Array:")
print(array)

# Square root
print("\nSquare Root:")
print(np.sqrt(array))

# Find dimension
print("\nDimension of Array:")
print(array.ndim)

# Reshape into 3 x 3
new_array = array.reshape(3, 3)

print("\n3 x 3 Array:")
print(new_array)

# Find dimension
print("\nDimension after Reshape:")
print(new_array.ndim)

# Convert to one-dimensional array
print("\nRavel:")
print(new_array.ravel())

# Reshape again
newm = new_array.reshape(3, 3)

print("\nNew Matrix:")
print(newm)

# Select elements
print("\nElements newm[2,1:3]:")
print(newm[2, 1:3])

print("\nElements newm[1:2,1:3]:")
print(newm[1:2, 1:3])

print("\nElements new_array[0:3,0:0]:")
print(new_array[0:3, 0:0])

print("\nElements new_array[0:2,0:1]:")
print(new_array[0:2, 0:1])

print("\nElements new_array[0:3,0:1]:")
print(new_array[0:3, 0:1])

print("\nRows new_array[1:3]:")
print(new_array[1:3])