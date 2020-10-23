#The range() function is used to generate a sequence of numbers over time. 
#Syntax:range([start,] stop [, step]) -> range object
#start	(optional) Starting point of the sequence. It defaults to 0.
#stop (required)	Endpoint of the sequence. This item will not be included in the sequence.
#step (optional)	Step size of the sequence. It defaults to 1.

print(range(5))
# list() call is not required in Python 2 
print(list(range(5))) 
#Here range() is called with two arguments, 5 and 10. As a result, it will generate a sequence of numbers from 5 up to 10 (but not including 10).
print(list(range(5,10)))

#The range() function is commonly used with for loop to repeat an action certain number of times. 
#For example, in the following listing, we use range() to execute the loop body 5 times.
print("count from 0 to 4")
for i in range(5):
    print(i)
#This code is functionally equivalent to the following:
#However, in the actual code, you should always use range() because it is concise, flexible and performs better.
print("this code <=> to above code")
for i in [0, 1, 2, 3, 4]:
    print(i)

print("this code <=> to above code")
n=list(range(4,9))
print("list",n)
print("count down from 10 to 6")
for i in range(10,5,-1):
    print(i)


