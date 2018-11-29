def exponent(x ,y):
    if (y == 0):
        return 1
    elif (y == 1):
		return x
    else:
		if (y%2==1):
        	 k= x*exponent(x,(y+1)/2)
        	 return k
		elif (y%2==0):
			 k= x*exponent(x,(y-2)/2)
			 return k*k
x = input("enter the base:")
y = input("enter the power:")
print exponent(x,y)

