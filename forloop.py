import math

#For loop file
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#   student_heights.append(student_heights[n])

total_sum_of_heights = 0

for x in student_heights:
    total_sum_of_heights += x

total_height = 0
for y in student_heights:
    total_height += 1

average = math.floor(total_sum_of_heights / total_height)

print(student_heights)
print(f"total height = {total_sum_of_heights}")
print(f"number of students = {total_height}")
print(f"average height = {average}")


#Geeting largest number from list

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = float(student_scores[n])


high_score = 0
for x in student_scores:
    if high_score < x:
        high_score = x

print(f"The highest score in the class is: {high_score}")


#creating a function using loops to add even numbers
target = int(input())

sum_of_even = 0

for i in range(0, target + 1, 1):
    sum_of_even += i

print(sum_of_even)



