# list 
students = ["Harry", "Ron", "Ram"]
for student in students:
    print(student, end=" ")
print()

for i in range(len(students)):
    print(i+1, students[i])

# Dictionary 
students_dic = {
    "Hermione" : "Gryffindor", 
    "Harry" : "Gryffindor", 
    "Ron" : "Gryffindor", 
    "Draco" : "Slytherin",
}

for student in students_dic:
    print(student, students_dic[student], sep = ",")

