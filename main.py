let=int(input("Enter Number: "));
factorial=1;
if let <=0:
    print("Factorial is not defined for zero and negative numbers")
else:
   for i in range(1,let+1):
    factorial=factorial*i 
    print("The factorial of", let, "is:", factorial)

