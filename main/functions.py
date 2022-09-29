import time
import decimal


# values given
a = 1548.8552574
b = 5576.24895464

# print values and length
print(a, len(str(a))-1, )
print(b, len(str(b))-1)

def determine_sig_fig(a, b):
    print(a)
    print(b)

        
def value_to_decimal(value, decimal_places):
    decimal.getcontext().rounding = decimal.ROUND_HALF_UP  # define rounding method
    return decimal.Decimal(str(float(value))).quantize(decimal.Decimal('1e-{}'.format(decimal_places)))


def multiply_sig_fig(a, b):
    #started with two values
    a_dec = decimal.Decimal(str(a))
    b_dec = decimal.Decimal(str(b))
    # make them into decimals
    a_places = abs(a_dec.as_tuple().exponent)
    b_places = abs(b_dec.as_tuple().exponent)
    print(a_places)
    print(b_places)
    if a_places < b_places:
        total_spaces = a_places
    else:
        total_spaces = b_places
    print("need" , total_spaces, "significant digits")
    d = a * b
    
    len_a = len(str(d)) - 1
    #print(len_a, len(str(d)))

    d = d/(10**len_a)
    #print(d, total_spaces)
    #e = value_to_decimal(d, total_spaces)
    e = round(d, total_spaces)
    print(f"The result is {d:.{total_spaces-1}e}")


def add_sig_fig(a, b):
    a_dec = decimal.Decimal(str(a))
    b_dec = decimal.Decimal(str(b))
    # make them into decimals
    a_places = abs(a_dec.as_tuple().exponent)
    b_places = abs(b_dec.as_tuple().exponent)
    print(a_places)
    print(b_places)
    if a_places < b_places:
        total_spaces = a_places
    else:
        total_spaces = b_places
    print("need" , total_spaces, "significant digits")
    c = a + b
    
    e = round(c, total_spaces)
    print(c)
    print(e, total_spaces)


def sub_sig_fig(a, b):
    a_dec = decimal.Decimal(str(a))
    b_dec = decimal.Decimal(str(b))
    # make them into decimals
    a_places = abs(a_dec.as_tuple().exponent)
    b_places = abs(b_dec.as_tuple().exponent)
    print(a_places)
    print(b_places)
    if a_places < b_places:
        total_spaces = a_places
    else:
        total_spaces = b_places
    print("need" , total_spaces, "significant digits")
    c = a - b
    
    e = round(c, total_spaces)
    print(c)
    print(e, total_spaces)

#multiply_sig_fig(a, b)
#add_sig_fig(a, b)
#sub_sig_fig(a, b)