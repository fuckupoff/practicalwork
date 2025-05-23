class Student:
    def __init__(self, surname, birthday, group, grades):
        self.surname = surname
        self.birthday = birthday
        self.group = group
        self.grades = grades
    
    def change_surname(self, new_surname):
        self.surname = new_surname
        print(f"Surname change: {new_surname}")

    def change_birthday(self, new_birthday):
        self.birthday = new_birthday
        print(f"Birthday change: {new_birthday}")

    def change_group(self, new_group):
        self.group = new_group
        print(f"Group change: {new_group}")

    def print_info(self):
        print(f'Info about student: \nSurname: {self.surname}\nBirthday: {self.birthday}\nGroup: {self.group}\nGrade: {", ".join(map(str, self.grades))}')

students = [
    Student("Antonow", "17.04.2007", "634", [4, 5, 4, 3, 4]),
    Student("Ivanov", "11.09.2001", "494", [3, 4, 5, 3, 4]),
    Student("Grechyk", "12.06.2006", "722", [5, 5, 5, 5, 5])
]

for student in students:
    student.print_info()
