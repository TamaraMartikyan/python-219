import random

def generate_random_matrix(row,col):
    return[[random.randint(1,100) for i in range(row)]for j in range(col)]


def get_column_sum(matrix, col_index):
    return sum(row[col_index] for row in matrix)


def get_row_average(matrix, row_index):
    return sum(matrix[row_index]) / len(matrix[row_index])


matrix=generate_random_matrix(3,3)
#print(matrix)
for row in matrix:
    print(row)

col_sum= get_column_sum(matrix, 0)
print(col_sum)

row_average=get_row_average(matrix,0)
print(row_average)
  
