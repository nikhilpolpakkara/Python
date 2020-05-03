def problem1_3(n):
    if n<1:
        x=1
        Sum = 0
        while x>n-1:
            Sum = x+Sum
            x=x-1
        print(Sum)
    else:
        x = 1
        Sum = 0
        while x < n+1:
            Sum = x+Sum
            x= x+1        
        print(Sum)