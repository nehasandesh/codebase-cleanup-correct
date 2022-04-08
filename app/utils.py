



def to_usd(my_price):

    """
    this is a docstring. it tells us what this function is about
    example of invoking the function.
    Invoke like this: to_usd(9.999)
    """

    return '${:,.2f}'.format(my_price)


#if this code is in the global scop of a file we are trying to import from, it will throw errors
#price = input("Please choose a price like 4.9999")

#print(to_usd(float(price)))

if __name__ == "__main__":

    #if this code is in the global scop of a file we are trying to import from, it will throw errors
    price = input("Please choose a price like 4.9999")

    print(to_usd(float(price)))
