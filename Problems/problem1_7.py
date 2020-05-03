def problem1_7():
   b1_str = input("Enter the length of one of the bases: ")
   b1 = float(b1_str)
   b2_str = input("Enter the length of the other base: ")
   b2 = float(b2_str)
   h_str = input("Enter the height: ")
   h = float(h_str)
   Area = (1/2)*(b1+b2)*h
   print("The area of a trapezoid with bases",b1,"and",b2,"and height",h,"is",Area)
   