'''asasasas'''
def main():
    '''sdsdsdsds'''
    minutes = int(input())
    ansminutes = minutes%60
    hourr = minutes//60
    anshourr = hourr%24
    ansdays = hourr//24
    print("%02d/%02d/%02d"%(ansdays, anshourr, ansminutes))
main()
