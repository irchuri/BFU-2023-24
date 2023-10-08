# ~ ~ ~ ~ T U P L E S ~ ~ ~ ~ #
B = (100, 200, 300, "Москва", 1.256)  # tuple
A = [100, 200, 300, "Москва", 1.256]  # list

# can work with elements
# can't change them

C = 500  # class 'int'
C_ = 500,  # class 'tuple'

# ~ ~ ~ ~ list off a tuple ~ ~ ~ ~ #

''' B = []
    for x in A:
        B.append(x)'''

'''
B = list(A)
'''

# ~ ~ ~ ~ tuple off a list ~ ~ ~ ~ #

''' B = []
    A = tuple(B)'''

# unpacking a multi-dimensional list

Aa = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(*Aa, sep='/n')
# [1,1,1]
# [2,2,2]
# [3,3,3]

for row in Aa:
    print(*row)
    # 1,1,1
    # 2,2,2
    # 3,3,3

for row in Aa:
    print(*row, sep='/t')
    # 1    1    1
    # 2    2    2
    # 3    3    3

# ~ ~ ~ ~ S E T S ~ ~ ~ ~ #

Bb = {1, 2, 3, 4}
print(Bb)
# 2, 3, 1, 4
# order does not matter! non-hashable type

Bbb = {100, 200, 300, 300, 400}
print(Bbb)
# 100, 300, 200, 400
# elements can't repeat!

Bbb.add(100)  # adding an element to a set

Ddict = {}
# class 'dict'
Sset = set(1, 2, 3)
# class = 'set'





























