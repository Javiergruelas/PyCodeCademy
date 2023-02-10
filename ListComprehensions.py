grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = []

for grade in grades:
  scaled_grades.append(grade + 10)

print(scaled_grades)

# a cleaner and shorter way to produce the same outcome could be: 

gradesTwo = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_gradesTwo = [grade + 10 for grade in gradesTwo]
print(scaled_gradesTwo)



##We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.
##Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

#Create a list called single_digits that consists of the numbers 0-9 (inclusive).
single_digits = list(range(0,10))

#Before the loop, create a list called squares. Assign it to be an empty list to begin with.
squares = []

#Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.
cubes = [digit**3 for digit in single_digits]

#Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.

for digit in single_digits:
  print(digit)
  squares.append(digit**2)

print(squares)
print(cubes)

