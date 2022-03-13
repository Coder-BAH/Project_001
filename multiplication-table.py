number = int(input("Enter a number to find the multiplication table: "))
for i in range (1, 11) :
    product = i*number
    print (i, 'x' , number , "=" , product)