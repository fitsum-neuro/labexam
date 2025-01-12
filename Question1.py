def find_matrix_shape(matrix):
     
    if not matrix or not isinstance(matrix, list):
        return (0, 0)
    
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 and isinstance(matrix[0], list) else 0
    
   
