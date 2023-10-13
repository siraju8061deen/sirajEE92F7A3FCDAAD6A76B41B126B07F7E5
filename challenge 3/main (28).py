class student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def _repr_(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students1 = [
    student("Alice", "A123", 3.75),
    student("Bob", "B456", 3.62),
    student("Charlie", "C789", 3.89),
]

students2 = [
    student("David", "D101", 3.45),
    student("Eve", "E202", 3.92),
    student("Frank", "F303", 3.75),
]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

print("Sorted Students List 1:")
for student in sorted_students1:
    print(student)

print("\nSorted Students List 2:")
for student in sorted_students2:
    print(student)