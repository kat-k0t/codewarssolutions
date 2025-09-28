#Simple Fun #152: Invite More Women?
#https://www.codewars.com/kata/58acfe4ae0201e1708000075/python
#My function counts the amount of men (1) and women (-1) in the list.
#It then checks to see if the amount of women is greater than or equal to the amount of men. 
#If the if statement is true than it returns false to indicate its not nessecary to invite more women.
def invite_more_women(arr):
    men = arr.count(1)
    women = arr.count(-1)
    if women >= men:
        return False
    else:
        return True