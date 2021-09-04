#List comprehension
squares = []
for x in range(10):
    squares.append(x+1)
    print(squares)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#shorthand
squares = [x+1 for x in range(10)]
print(squares)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#nested list comprehensions
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],

]

matrix2 = []
for i in range(4):
    matrix2.append([row[i] for row in matrix])
print(matrix2)
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#shorthand
matrix2 = [[row[i] for row in matrix] for i in range(4)]
print(matrix2)
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


#-----------------Examples-----------------

#--------example 1--------
# Getting square of even numbers from 1 to 10
squares = [n**2 for n in range(1, 11) if n%2==0]
 
# Display square of even numbers
print(squares)

#[4, 16, 36, 64, 100]

#--------example 2--------
# Assign matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]
 
# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix))]
 
print(trans)

#[++++[+10, 40, 70], [20, 50, 80], [30, 60, 90]]

#--------example 3--------
# Initializing string
string = 'Geeks4Geeks'
 
# Toggle case of each character
List = list(map(lambda i: chr(ord(i)^32), string))
 
# Display list
print(List)

#[‘g’, ‘E’, ‘E’, ‘K’, ‘S’, ‘\x14’, ‘g’, ‘E’, ‘E’, ‘K’, ‘S’, ‘\x01’]

#--------example 4--------
# Reverse each string in tuple
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')]
 
# Display list
print(List)

#['skeeG', 'rof', 'skeeG']

#--------example 5--------
# Explicit function
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum
 
 
# Initializing list
List = [367, 111, 562, 945, 6726, 873]
 
# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]
 
# Displaying new list
print(newList)

#[16, 3, 18, 18]