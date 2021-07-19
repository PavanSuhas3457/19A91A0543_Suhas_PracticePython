class Student:
    def message(self):
        print('This message is from student class')
class Department(Student):
    def message(self):
        print('This Department Class is being inherited from Student Class')


stud = Student()
stud.message()
depart = Department()
depart.message()
