def drawTriangleRight(n):
    for i in range(n):
        param = ""
        for j in range(n-i-1):
            param += " "
        for l in range(i):
            param += "#"
        print(param)


drawTriangleRight(10)
