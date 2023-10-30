class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # законченые курсы
        self.courses_in_progress = []  # курсы на данный момент
        self.grades = {}  # оценки

    def rate_hw(self, lecturer, course, grade): # оценки выставляемые студентами лекторам
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grades in course_grades:
                course_sum += grades
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок нет!'
        else:
            return f"{mid_sum / len(self.grades.values()):.2f}"

    def __str__(self):
        self.courses_in_progress = ", ".join(self.courses_in_progress)
        self.finished_courses = ", ".join(self.finished_courses)
        return (f"Имя:{self.name}\nФамилия:{self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grades()}\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")

    def __eq__(self, student):
        if not isinstance(student, Student):
            print(f'Такого преподавателя нет, сравнение невозможно!')
            return
        else:
            return self.average_grades() == student.average_grades()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет, сравнение невозможно!')
            return
        return self.average_grades() > other.average_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # прикрепленные курсы


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grades in course_grades:
                course_sum += grades
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок нет!'
        else:
            return f"{mid_sum / len(self.grades.values()):.2f}"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}"

    def __gt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print('Такого преподавателя нет, сравнение невозможно!')
            return
        return self.average_grades() > lecturer.average_grades()

    def __eq__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print(f'Такого преподавателя нет, сравнение невозможно!')
            return
        else:
            return self.average_grades() == lecturer.average_grades()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):  # оценки за дз
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя:{self.name}\nФамилия:{self.surname}"


# студенты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

new_best_student = Student('Harry', 'Potter', 'your_gender')
new_best_student.courses_in_progress += ['Python']
new_best_student.courses_in_progress += ['Git']
new_best_student.finished_courses += ['Введение в программирование']

# Менторы
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

# проверяющие
any_reviewer = Reviewer("Danny", "Murat")
any_reviewer.courses_attached += ['Python']

# оценки студентам
any_reviewer.rate_hw(best_student, 'Python', 10)
any_reviewer.rate_hw(best_student, 'Python', 10)
any_reviewer.rate_hw(best_student, 'Python', 10)

any_reviewer.rate_hw(new_best_student, 'Python', 10)
any_reviewer.rate_hw(new_best_student, 'Python', 10)
any_reviewer.rate_hw(new_best_student, 'Python', 10)

# лекторы
any_lecturer = Lecturer("Diana", "Still")
any_lecturer.courses_attached += ['Python']

new_any_lecturer = Lecturer("Petter", "Parker")
new_any_lecturer.courses_attached += ['Python']

# оценки лекторам
best_student.rate_hw(any_lecturer, 'Python', 10)
best_student.rate_hw(any_lecturer, 'Python', 10)
best_student.rate_hw(any_lecturer, 'Python', 10)

new_best_student.rate_hw(new_any_lecturer, 'Python', 10)
new_best_student.rate_hw(new_any_lecturer, 'Python', 10)
new_best_student.rate_hw(new_any_lecturer, 'Python', 10)

# вывод информации на экран
print(best_student.grades)
print(any_lecturer.grades)

print(any_reviewer)
print(any_lecturer)
print(best_student)


print(any_lecturer.__eq__(new_any_lecturer))
print(best_student.__eq__(new_best_student))

print(any_lecturer.__gt__(new_any_lecturer))
print(best_student.__gt__(new_best_student))