def powerdef():
    sumsqaresp = 0
    sumsqarep = 0

    for i in range(1,101):
        sumsqaresp += i**2
        sumsqarep += i

    lastsum = sumsqarep**2
    return(lastsum - sumsqaresp)
        

print("the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is",powerdef())
