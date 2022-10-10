list1 = []
k = 1
n = int(input("Please enter the number of numbers you want to enter: "))
while k <= n :
    n1= int(input("Please enter the number of number: "))
    list1.append(n1)
    k += 1
    
list1.sort()
largest = list1[n-1]

print("The largest number is: ", largest)
