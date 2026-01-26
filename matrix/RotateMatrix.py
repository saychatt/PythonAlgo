from typing import List


class RotateMatrix:
    """
    https://neetcode.io/problems/rotate-matrix/question
    Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.
    You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.
    Test Case 1:  matrix=[[1,2],[3,4]] output = [[3,1],[4,2]]
    Test Case 2: matrix=[[1,2,3],[4,5,6],[7,8,9]] output = [[7,4,1],[8,5,2],[9,6,3]]
    Test Case 3: matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    """
    @staticmethod
    def rotateMatrix(self, matrix: List[List[int]]) -> None:
        # Start from outermost layer
        layer_start = 0
        matrix_size = len(matrix[0])
        # Process each layer from outside to inside
        layer_end = matrix_size - 1
        layer_offset = 0
        
        # Continue until we reach the center
        while layer_end >= 1:
            # Rotate elements in current layer
            for current_col in range(layer_start, layer_end):
                # Calculate corresponding row position for rotation
                corresponding_row = layer_end - current_col + layer_offset
                
                # Store top-right element temporarily
                temp_top_right = matrix[current_col][layer_end]
                
                # Move top-left to top-right
                matrix[current_col][layer_end] = matrix[layer_start][current_col]
                
                # Move bottom-left to top-left
                matrix[layer_start][current_col] = matrix[corresponding_row][layer_start]
                
                # Move bottom-right to bottom-left
                matrix[corresponding_row][layer_start] = matrix[layer_end][corresponding_row]
                
                # Move temp (original top-right) to bottom-right
                matrix[layer_end][corresponding_row] = temp_top_right

            # Move to inner layer
            layer_end -= 1
            layer_start += 1
            layer_offset += 1