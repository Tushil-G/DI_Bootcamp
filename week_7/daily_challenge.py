import numpy as np

M=np.random.randint(2, 49)
N=np.random.randint(2, 39)
if M<50 and N<40:
# print(M)
# print(N)
    table = np.random.randint(1, 100, size=(M,N))
    # print(table[:2])
    # print(table[:,2])
    # table[-1] = 7
    # print(table)
    table[:,-1] = table[:,0] + table[:,1]
    print(table)







