'''min'''
def main():
    '''asasasas'''
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())

    if num1 <= num2 and num1 <= num3 and num1 <= num4:
        print(str(num1) + ' is Min.')
    elif num2 <= num1 and num2 <= num3 and num2 <= num4:
        print(str(num2) + ' is Min.')
    elif num3 <= num1 and num3 <= num2 and num3 <= num4:
        print(str(num2) + ' is Min.')
    else:
        print(str(num3) + ' is Min.')
main()
