



xvec = [10, 20, 30]
yvec = [7, 5, 3]
zipped = zip(xvec, yvec)
print(zipped)
for x,y in zipped:
    # 10 7
    # 20 5
    # 30 3
    print(x,y)

sum=sum(x*y for x,y in zipped) 
print(sum)


data = 'golf'
list(print(data[i]) for i in range(len(data)-1, -1, -1))