def main():
    sec = {}
    section = int(input("Enter number of sections :"))
    stunum = int(input("Enter number of students :"))
    for _ in range(stunum):
        inf = input()
        sn,sect = inf.split()
        sec[sect] = sn

    
    print(sec[sect])

        
main()