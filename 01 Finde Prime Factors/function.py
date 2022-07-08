def findPrimeFactors(myNumber):
    if isinstance(myNumber, int) and myNumber>0:
        print("Value providedis integer and greater than 0")
        factors = list()
        divisor = 2
        print("start here")
        print("divisor: " + "{}".format(divisor))
        while (divisor<=myNumber):
            if (myNumber % divisor) == 0:
                factors.append(divisor)
                myNumber = myNumber//divisor
            else:
                divisor += 1
        print(*factors)
        return factors







findPrimeFactors(30)