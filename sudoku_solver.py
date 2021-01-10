sudoku_correct =[
    [8,2,7,1,5,4,3,9,6],
    [9,6,5,3,2,7,1,4,8],
    [3,4,1,6,8,9,7,5,2],
    [5,9,3,4,6,8,2,7,1],
    [4,7,2,5,1,3,6,8,9],
    [6,1,8,9,7,2,4,3,5],
    [7,8,6,2,3,5,9,1,4],
    [1,5,4,7,9,6,8,2,3],
    [2,3,9,8,4,1,5,6,7],
]

sudoku_incorrect =[
    [9,2,7,1,5,4,3,9,6],
    [9,6,5,3,2,7,1,4,8],
    [3,4,1,6,8,9,7,5,2],
    [5,9,3,4,6,8,2,7,1],
    [4,7,2,5,1,3,6,8,9],
    [6,1,8,9,7,2,4,3,5],
    [7,8,6,2,3,5,9,1,4],
    [1,5,4,7,9,6,8,2,3],
    [2,3,9,8,4,1,5,6,7],
]

def sudoku_verify(grid, n = 3):
    """
    Function to verify if a sudoku solution is correct
    If there is an issue, will raise an AssertionError
    
    
    ::param grid: (list[list]) a 9x9 list
    ::param n: (int) Size of sudoku problem, default is 3 (ie 9x9)
                     But can be any integer
                     eg 4, where the box is 16x16, and 4 4x4 boxes
    ::return: (True) or raises an AssertionError
    """    
    for row in grid:
        assert len(set(row)) == len(row), \
        "The number of unique element, and size of row is different"
    for i in range(len(grid)):
        col = [row[i] for row in grid]
        assert len(set(col)) == len(col), \
        "The number of unique element, and size of column is different"
    for i in range(n):
        for j in range(n):
            for i in range(n):
                box = [row[n*i:(i+1)*n] for row in grid[n*j:(j+1)*n]]
                flat_box = [item for sublist in box for item in sublist]

                assert len(set(flat_box)) == len(flat_box), \
                "The number of unique element, and size of box is different"

    return True