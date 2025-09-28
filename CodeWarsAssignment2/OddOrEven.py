#Odd or Even?
#https://www.codewars.com/kata/5949481f86420f59480000e7/python
#My function sums up all the numbers in an array and checks to see if the sum is odd or even.
#The if statement checks to see if the sum is even.
#After checking if the sum is even it either outputs even if true or odd if false
def odd_or_even(arr):
    num = sum(arr) 
    if num % 2 == 0:
        return "even"
    else:
        return "odd"