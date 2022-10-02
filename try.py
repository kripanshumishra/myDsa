def ans( num ):
    if ( num == 0  ):
        return 0
    maxdigit = 0
    num1 = num
    while( num1 ):
        maxdigit= max( num1%10 , maxdigit )
        num1//=10
    return 1+ ans(num-maxdigit)
def main( ):
    inp = int(input())
    print(ans(inp))


if __name__=="__main__":
    main()
