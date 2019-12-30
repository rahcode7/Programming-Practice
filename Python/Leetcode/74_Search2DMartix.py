# Problem - https://leetcode.com/problems/search-a-2d-matrix/


from typing import List
matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
        ]
target = 3

class Solution:
    # Inefficient
    # def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if target == matrix[i][j]:
    #                 return True
    #     return(False)

    # Efficient
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        flatten = []
        for i in matrix:
            flatten += i  
            print(flatten)   
        return(target in flatten)

print(Solution.searchMatrix(matrix,target))