class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # оконченные курсы
        self.courses_in_progress = []  # курсы на данный момент
        self.grades = {}  # оценки

    def rate_hw(self, lecturer, course, grade):  # оценки выставляемые студентами лекторам
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