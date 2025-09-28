#Easy Time Convert
#https://www.codewars.com/kata/5a084a098ba9146690000969/python
#My function converts minutes into a hh:mm format.
#If the number is <= 0 it returns 00:00.
#if not it then converts it into hours and minutes.
#it checks to see if the number for hrs or min is one or 2 digits and then supplements an extra 0 if necessary.
def time_convert(num):
    if num <= 0:
        return "00:00"
    hrs = num // 60
    mins = num % 60
    if hrs < 10:
        hh = f"0{hrs}:"
    else:
        hh = f"{hrs}:"
    if mins < 10:
        mm = f"0{mins}"
    else:
        mm = f"{mins}"
    return hh + mm