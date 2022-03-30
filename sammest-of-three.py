# Sammest of three

a,b,c = input("Enter three numbers followed by  : ").split()

print("First number :",a)
print("Second number :",b)
print("Third number :",c)
if a==b==c :
    print("Entered numbers are equal!!!")
elif a < b and a < c:
    print(a," is smallest")
elif b < a and b < c :
    print(b," is smallest")
else :
    print(c," is smallest")

