import ai
import ai2
import touching
# S=[[0,19,4],
#    [1,19,4],
#    [2,19,4],
#    [3,19,4],
#    [4,19,1],
#    [5,19,1],
#    [6,19,1],
#    [7,19,1],
#    [8,19,7],
#    [0,18,4],
#    [1,18,4],
#    [2,18,4],
#    [3,18,4],
#    [4,18,1],
#    [5,18,1],
#    [6,18,1],
#    [7,18,1],
#    [8,18,7],
#    [0,17,4],
#    [1,17,4],
#    [2,17,4],
#    [3,17,4],
#    [4,17,1],
#    [5,17,1],
#    [6,17,1],
#    [7,17,1],
#    [8,17,7],
#    [0,16,4],
#    [1,16,4],
#    [2,16,4],
#    [3,16,4],
#    [4,16,1],
#    [5,16,1],
#    [6,16,1],
#    [7,16,1],
#    [8,16,7],
#    ]

# S1=[[0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [0,0,0,0,0,0,0,0,0,0],
#    [1,1,1,1,0,0,0,0,0,0]]
S=[]
A=[[0,20,5],[1,20,5],[1,21,5],[2,21,5]]

# #a=grid.Grid(S)
# SSS=ai2.bestPosition(S1,A)
# SS=ai.bestPosition(S,A)
# print(SSS)
# print(SS)
# print(A)
# print(S)

print(touching.Touching(S,A))
print(touching.Lost(S,A))
print(touching.mindistance(S,A))


