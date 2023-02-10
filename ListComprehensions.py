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