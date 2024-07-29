import sys

MAX = 1000000

savechartTemp = [1]*(MAX+1)
savechartReal = [0]*(MAX+1)
savechartReal[1] = 1


for i in range(2,(MAX+1)):
    for j in range(1,(MAX//i)+1):
        savechartTemp[j*i] = savechartTemp[j*i] + i

    savechartReal[i] = savechartReal[i-1] + savechartTemp[i]

x = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(x)]

for i in data:
    n = int(i)
    print(savechartReal[n])