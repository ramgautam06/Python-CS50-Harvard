import csv 

def get_house(student):
    return student["house"]

def reading_csv_file():
    students = [] # list of dictionary 
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name" : name , "house": house}
            students.append(student)
    
    for student in sorted(students, key=get_house, reverse=True):
        print(f"{student['name']} is in {student['house']}")
    print()

    #using lambda function 
    for student in sorted(students, key= lambda student:student['house'], reverse=True):
        print(f"{student['name']} is in {student['house']}")

def reading_csv_using_libraray():
    students = []
    with open('students.csv') as file:
        reader = csv.reader(file)
        for name, home in reader:
            students.append({"name": name, "home":home})
    
    for student in sorted(students, key=lambda x : x['name']):
        print(f"{student['name']} is from {student['home']}")

def reading_csv_as_dictionary():
    students = []
    with open("students.csv") as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            students.append({"name": row["name"], 
                             "home": row["home"]})
    
    for student in sorted(students, key = lambda stud: stud['name']):
        print(f"{student['name']} is from {student['home']}")

def writing_csv_file():
    name = input("What's your name? ")
    home = input("Where's your home? ")

    with open("homes.csv", "a") as file:
        # writer = csv.writer(file)
        # writer.writerow([name, home])
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name":name, "home": home})

def main():
    # reading_csv_file()
    # reading_csv_using_libraray()
    # reading_csv_as_dictionary()
    writing_csv_file()

if __name__=="__main__":
    main()