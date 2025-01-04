# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.group = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.group = "A"
    student2.name = "Olivia"
    student2.age = 21
    student2.group = "B"
    student3.name = "Ava"
    student3.age = 20
    student3.group = "A"
    # printing the object attributes

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, group {student1.group}')
    print(f'{student2.name}, {student2.age} years old, group {student2.group}')
    print(f'{student3.name}, {student3.age} years old, group {student3.group}')
    
if __name__ == "__main__":
    main()