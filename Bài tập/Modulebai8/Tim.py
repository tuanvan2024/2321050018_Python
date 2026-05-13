def Timmax(n):
    lonNhat = 0
    for c in str(n):
        if int(c) > lonNhat:
            lonNhat = int(c)
    return lonNhat