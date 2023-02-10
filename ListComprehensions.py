grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = []

for grade in grades:
  scaled_grades.append(grade + 10)

print(scaled_grades)

# a cleaner and shorter way to produce the same outcome could be: 

gradesTwo = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_gradesTwo = [grade + 10 for grade in gradesTwo]
print(scaled_gradesTwo)