#Pull your words together, man!
#https://www.codewars.com/kata/59ad7d2e07157af687000070/python
#My function checks to see if the first string in array is lower case.
#If it is it capitalizes it.
#It then joins the array into one string and adds a period at the end.
def sentencify(words):
    if words[0].islower():
        words[0] = words[0].capitalize()
    s = " ".join(words)
    p = s + "."
    return p