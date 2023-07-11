student_height = input("Input a list of student heights").split(",")
print(student_height)
print(type(student_height))
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])

total_height=0
for height in student_height:
    total_height+= height
print(total_height)

num_of_student=0
for n in range(0,len(student_height)):
    num_of_student+=n
print(num_of_student)

#calculating average height
avg_height= total_height/num_of_student
print(avg_height)



#avg_height = sum(student_height)/len(student_height)
#print(avg_height)

