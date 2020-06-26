def isPrime(num): 
      
    if num <= 1 : 
        return False
  
    for i in range(2, num): 
        if num % i == 0: 
            return False
    return True
def ran(m,n):
    for i in range(m,n):
    	if isPrime(i + 1):
    			print(i + 1, end="   ")
    print()

num1=int(input("enter the first range : "))
num2=int(input("enter the second range : "))
ran(num1,num2)

  
