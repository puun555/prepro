'''sdsdsdsdsdsd'''
def dis0(numpat):
    '''sdsdsdsdsdsd'''
    for i in range(-numpat, numpat+1):
        for j in range(-numpat, numpat+1):
            if (abs(i)%2 != 0) or abs(j) == numpat:
                print("I", end=' ')
            else:
                print(" ", end=' ')
        print()

def dis1(numpat):
    '''sdsdsdsdsdsd'''
    for i in range(-numpat, numpat+1):
        for j in range(-numpat, numpat+1):
            if i == 0 or j == 0 or abs(i) == abs(j):
                print("I", end=' ')
            else:
                print(" ", end=' ')
        print()

def dis2(numpat):
    '''sdsdsdsdsd'''
    for i in range(-numpat, numpat+1):
        for j in range(-numpat, numpat+1):
            if abs(i) == numpat or abs(j) == numpat \
            or (j == 0 and i == 0) or numpat - 1 - abs(i) == abs(j):
                print("I", end=' ')
            else:
                print(" ", end=' ')
        print()

def dis3(numpat):
    '''sdsdsdsdsdsd'''
    for i in range(-numpat, numpat+1):
        for j in range(-numpat, numpat+1):
            if abs(j) <= abs(i):
                print("I", end=' ')
            else:
                print(" ", end=' ')
        print()

def main():
    '''sdsdsdsdsdsdsdsd'''
    num = int(input())
    check = num%4
    numpat = num//4
    if check == 0:
        dis0(numpat)
    elif check == 1:
        dis1(numpat)
    elif check == 2:
        dis2(numpat)
    elif check == 3:
        dis3(numpat)
main()
