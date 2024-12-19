# Python3 Implementation for Gauss-Jordan
# Elimination Method
# Modified version of code from https://www.geeksforgeeks.org/program-for-gauss-jordan-elimination-method/
# This code is contributed by phasing17


N = 2


# function to reduce matrix to reduced
# row echelon form.
def PerformOperation(a, n):
    i = 0
    j = 0
    k = 0
    c = 0
    flag = 0

    # Performing elementary operations
    for i in range(n):
        if a[i][i] == 0:

            c = 1
            while (i + c) < n and a[i + c][i] == 0:
                c += 1
            if (i + c) == n:

                flag = 1
                break

            j = i
            for k in range(1 + n):

                temp = a[j][k]
                a[j][k] = a[j + c][k]
                a[j + c][k] = temp

        for j in range(n):

            # Excluding all i == j
            if i != j:
                # Converting Matrix to reduced row
                # echelon form(diagonal matrix)
                p = a[j][i] / a[i][i]

                k = 0
                for k in range(n + 1):
                    a[j][k] = a[j][k] - (a[i][k]) * p

    return flag


# To check whether infinite solutions
# exists or no solution exists
def CheckConsistency(a, n, flag):

    # flag == 2 for infinite solution
    # flag == 3 for No solution
    flag = 3
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + a[i][j]
        if sum == a[i][j]:
            flag = 2

    return flag


def get_result(a, n) -> list[int]:
    return [round(a[i][n] / a[i][i]) for i in range(n)]


# Driver code
def find_button_presses(matrix: list[list[str]]):
    # matrix e.g. [[94, 22, 8400], [34, 67, 5400]]
    flag = PerformOperation(matrix, N)
    if flag == 0:
        return None
    return get_result(matrix, N)
