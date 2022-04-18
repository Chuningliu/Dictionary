# Create a dictionary with the roll number,names and marks of n students 
# in a class and display the names of the students which have marks above 75.
n=int(input("Enter the number of students:-"))
d={}
for i in range(n):
    r=int(input("Enter the roll number:-"))
    n=input("Enter the names:-")
    m=int(input("Enter the marks:-"))
    l=[n,m]
    d[r]=l
print(d)
for key in d:
    if d[key][1]>75:
        print(d[key][0],m)