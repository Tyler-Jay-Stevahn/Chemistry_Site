import time
import decimal


# values given
a = '048.800'
b = '576'
d = '210'
c = ['100', '1.1', '0.0000000000008', '4.000008', '45', '808', '158.575', '9.008', '0.0005', '4.3005', '350.0']
# print values and length
#print(a, len(str(a))-1)
#print(b, len(str(b))-1)

def determine_sig_fig(a):
    #print(len(a) - 1)
    #print(a_sig_fig, b_sig_fig)
    if '.' in a:
        c = str(a)
        #print(c)
        c = str(c).lstrip("0")
        c = str(c).lstrip(".")
        c = str(c).lstrip("0")
        c = str(c).replace(".", "")
        len_c = len(c)  
        total_spaces = len_c
        print(a, "has", total_spaces, "significant digits")
        return total_spaces
    else:
        if a[-1:] == "0":
            print(a, "has an unknown number of significant digits")
            total_spaces = 50
            return total_spaces
        else:
            total_spaces = len(a)
            print(a, "has", total_spaces, "significant digits")
            return total_spaces


        
def value_to_decimal(value, decimal_places):
    decimal.getcontext().rounding = decimal.ROUND_HALF_UP  # define rounding method
    return decimal.Decimal(str(float(value))).quantize(decimal.Decimal('1e-{}'.format(decimal_places)))


def multiply_sig_fig(a, b):
    #started with two values
    a_dec = decimal.Decimal(str(a))
    b_dec = decimal.Decimal(str(b))
    # make them into decimals
    a_places = determine_sig_fig(a)
    b_places = determine_sig_fig(b)
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

multiply_sig_fig(a, b)
#add_sig_fig(a, b)
#sub_sig_fig(a, b)
'''for i in c:
    determine_sig_fig(i)'''