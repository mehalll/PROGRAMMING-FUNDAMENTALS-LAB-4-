
print("\nArithmetic Sequence\n\n")

def arithmetic_sq(y,z):
    
    n = eval(input("Please enter the number of the term you want to find: "))
    an = y+((n-1)*z)
    print("The",str(n),"th term in the given sequence is              :",str(an))
    user=input("\nDo you want to find another term? (Press 'y' to continue, 'q' to quit):")
    if user=='y':
        arithmetic_sq(y,z)
    else:
        print("Goodbye!")
