
def setZeroes(matrix):

    cols=set()
    rows=set()

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if i in rows or j in cols:
                matrix[i][j]=0

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))