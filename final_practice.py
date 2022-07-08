a = [1,2,3,4]
b = a
b[2] = 6
print(a)
print(b)

def eat(x):
    x[1] = 9
    x[3] = 11

def prob3():
    food = [4,5,6,7]
    eat(food)
    print('food =', food)

#problem 5
def create_2d(height, width):
    a = [[]]*height
    for row in range(height):
        b = []
        for col in range(width):
            b += [row*col]
        a[row] = b
    return a

#problem 6
def add_one(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] += 1
