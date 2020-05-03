def problem2_7():
    side1 = input("Enter length of side one:")
    side2 = input("Enter length of side two:")
    side3 = input("Enter length of side three:")
    s1 = float(side1)
    s2 = float(side2)
    s3 = float(side3)
    s = 0.5*(s1+s2+s3)
    Area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
    print("Area of a triangle with sides",s1,s2,s3,"is",Area)