# CS175
# Maggie Volker

integer1 = int(input("Please enter an integer: "))
integer2 = int(input("Please enter another integer: "))

sum = (integer1 + integer2)
difference = (integer1 - integer2)
product = integer1 * integer2
average = (integer1 + integer2)/2
print(f"The sum of the two integers is {sum}, the difference of the two integers is {difference}, the product of the two integers is {product}, and the average of the two integers is {average}.")
distance = abs(difference)
maximum = max(integer1, integer2)
minimum = min(integer1, integer2)
print(f"The distance between the two integers is {distance}, the maximum of the two integers is {maximum}, and the minimum of the two integers is {minimum}.")
