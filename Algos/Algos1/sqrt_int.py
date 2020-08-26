def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Thought process: I think this is a binary search problem. 
    # You can start with numbers that smaller than or equal to half 
    # the integer as your search space.
    result = number/2
    end = number
    begin = 1
    while abs(result**2 - number) > 0.5:
        
        if result**2 > number:
            result = (begin + result)/2
            
        else:
            result = (end + result)/2
    return result
    

#print ("Pass" if  (3 == sqrt(9)) else "Fail")
#print ("Pass" if  (0 == sqrt(0)) else "Fail")
#print ("Pass" if  (4 == sqrt(16)) else "Fail")
#print ("Pass" if  (1 == sqrt(1)) else "Fail")
#print ("Pass" if  (5 == sqrt(27)) else "Fail")
print(sqrt(8))