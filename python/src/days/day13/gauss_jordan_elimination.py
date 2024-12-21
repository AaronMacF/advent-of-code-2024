# Python3 Implementation for Gauss-Jordan Elimination Method
# Modified version of code from https://www.geeksforgeeks.org/program-for-gauss-jordan-elimination-method/
# The original code is contributed by phasing17


from typing import Union


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


def get_result(a, n) -> list[float]:
    return [a[i][n] / a[i][i] for i in range(n)]


def get_result_as_list_of_int(matrix: list[float]) -> Union[None, list[int]]:
    tolerance = (
        0.001  # if number is within 0.001 of an integer, assume it is an integer
    )
    rounded_values = list(map(round, matrix))
    if all(
        [
            abs(value - rounded_value) < tolerance
            for (value, rounded_value) in zip(matrix, rounded_values)
        ]
    ):
        return rounded_values
    return None


# Driver code
def find_button_presses(matrix: list[list[str]]) -> Union[None, list[int]]:
    # matrix e.g. [[94, 22, 8400], [34, 67, 5400]]
    flag = PerformOperation(matrix, N)
    if flag != 0:
        return None
    result = get_result(matrix, N)
    integer_result = get_result_as_list_of_int(result)
    return integer_result
