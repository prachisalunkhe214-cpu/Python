"""Write the code for even number using function"""
def count_even(n):
    count=0
    for i in range(1,n+1):
        if i%2==0:
            print(i)
            count +=1
    return count
result=count_even(20)
result=count_even(30)
print ( "total count",result)
