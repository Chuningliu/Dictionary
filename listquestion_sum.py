# list=[[1,2,3],[4,5,6],[7,8,9],[3,3,3]]
# i=0
# b=[]
# while i<len(list):
#     a=sum(list[i])
#     b.append([a])
#     i+=1
# print(b)


a=[[1,4],[5,2],[7,6]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j+=1
    b.append(sum)
    i+=1
print(b)






    