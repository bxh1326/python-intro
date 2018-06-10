def countCase(param):
    uppercaseCount = 0
    lowercaseCount = 0
    for ch in param:
        if ch.isupper():
            uppercaseCount += 1
        if ch.islower():
            lowercaseCount += 1
    print("Uppercase Count: " + str(uppercaseCount))
    print("Lowercase Count:" + str(lowercaseCount))

countCase("I enjoy learning Python in Chinese School")

