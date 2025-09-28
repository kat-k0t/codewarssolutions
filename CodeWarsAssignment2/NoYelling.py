#No yelling!
#https://www.codewars.com/kata/587a75dbcaf9670c32000292/python
#My function fixes excess capitalization and spaces. 
#The first 2 lines of the functions fixes capitalization.
#The if statement checks for excess spaces and fixes it if the string has excess spaces.
def filter_words(st):
    decap = st.lower()
    cap = decap.capitalize()
    if "  " in st:
        return " ".join(cap.split())
    else:
        return cap