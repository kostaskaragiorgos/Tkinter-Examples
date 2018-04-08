def factorial(n):
    factorial =1 
    for i in range(1,n+1):
        factorial = factorial *i
    return factorial

sum =0
for i in range(1,101):
    for r in range(1,i):
        if factorial(i)/(factorial(r)*factorial(i-r)) > 1000000:
            sum +=1

print("The number of values greater than 1000000",sum)
