def smallmin():
    sum = 0
    for i in range(1,232792561):
        for j in range(1,21):
            if i%j ==0:
                sum +=1
            else:
                sum = 0
            if sum == 20:
                print (i, "is the  smallest positive number that is evenly divisible by all of the numbers from 1 to 20")
