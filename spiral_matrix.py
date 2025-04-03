'''
spiral matrix 

1 2 3
4 5 6
7 8 9

result = [1 2 3 6 9 8 7 4 5]
it traversal the like sank type

-->--->
-->--.| 
|<---<-
'''
def spiral_matrix(mat):
    if not mat or not mat[0]:
        return []
    
    result = []

    top, bottom = 0, len(mat)-1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


def read_mat(n):
    mat = []
    for _ in range(n):
        a = list(map(int,input().split()))
        mat.append(a)
    return mat

n = int(input())

matrix = read_mat(n)
print(spiral_matrix(matrix))