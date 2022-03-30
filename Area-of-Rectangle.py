# AreaRectangle

def AreaRectangle(width, length) :
    Area = width * length
    Perimeter = 2 * (width + length)
    print("\n Area of a Rectangle is: %.2f" %Area)
    print(" Perimeter of Rectangle is: %.2f" %Perimeter)
    
width = float(input('Enter the Width: '))
length = float(input('Please Enter the Length: '))
AreaRectangle(width, length)
