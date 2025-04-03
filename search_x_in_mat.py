def search_x_in_mat(matrix,x):
    rows, cols = len(matrix) , len(matrix[0])
    row , col = 0 ,cols-1

    while row < rows and col >= 0:
        if matrix[row][col] == x:
            return True
        elif matrix[row][col] > x:
            col -= 1
        else:
            row +=1
    return False



def read_matrix(n):
    mat = []
    for i in range(n):
        a = list(map(int,input().split()))
        mat.append(a)
    return mat


n = int(input())
x = int(input())
matrix = read_matrix(n)
print(search_x_in_mat(matrix,x))