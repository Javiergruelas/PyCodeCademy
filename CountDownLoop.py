# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")


##Countdown Loop
countdown = 10
print("Countdown has begun!")
while countdown >= 0:
  # Loop Body
  # Print if the condition is still true
  print(str(countdown)+"! ")
  # Increment count
  countdown -= 1
print("We have liftoff!")