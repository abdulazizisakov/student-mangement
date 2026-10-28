import database
from utils import get_positive_int, find_student_by_id, cprint


def get_all_grades(student: dict) -> list:
    all_grades = []
    for grade_list in student["grades"].values():
        all_grades.extend(grade_list)
    return all_grades


def calculate_average(student: dict) -> float | None:
    all_grades = get_all_grades(student)
    if not all_grades:
        return None
    return sum(all_grades) / len(all_grades)


def calculate_subject_averages(student: dict) -> dict:
    averages = {}
    for subject, grade_list in student["grades"].items():
        if grade_list:
            averages[subject] = sum(grade_list) / len(grade_list)
    return averages


def show_average() -> None:
    student_id = get_positive_int("O'quvchi ID si: ")
    student = find_student_by_id(student_id)

    if student is None:
        cprint("Bu ID dagi o'quvchi topilmadi.", fore_256="red")
        return

    average = calculate_average(student)
    if average is None:
        cprint("Baholar mavjud emas.", fore_256="yellow")
        return

    print(f"{student['name']} umumiy o'rtacha bahosi: {average:.2f}")
    print("Fanlar kesimida:")
    for subject, subject_average in calculate_subject_averages(student).items():
        print(f"  {subject}: {subject_average:.2f}")


def build_ranking() -> tuple:
    with_grades = []
    without_grades = []

    for student in database.students:
        average = calculate_average(student)
        if average is None:
            without_grades.append(student)
        else:
            with_grades.append((student, average))

    with_grades.sort(key=lambda item: (-item[1], item[0]["name"].lower()))
    return with_grades, without_grades


def show_ranking() -> None:
    if not database.students:
        cprint("O'quvchilar ro'yxati bo'sh.", fore_256="yellow")
        return

    with_grades, without_grades = build_ranking()

    print("--- Reyting ---")
    rank = 0
    previous_average = None
    for position, (student, average) in enumerate(with_grades, start=1):
        if previous_average is None or round(average, 2) != round(previous_average, 2):
            rank = position
        previous_average = average
        print(f"{rank}. {student['name']} ({student['group']}) - {average:.2f}")

    if without_grades:
        print("Bahosi yo'q o'quvchilar:")
        for student in without_grades:
            print(f"  - {student['name']} ({student['group']})")


def show_top_student() -> None:
    with_grades, _ = build_ranking()

    if not with_grades:
        cprint("Hech bir o'quvchida baho yo'q.", fore_256="yellow")
        return

    top_average = round(with_grades[0][1], 2)
    print(f"Eng yuqori o'rtacha: {top_average:.2f}")
    for student, average in with_grades:
        if round(average, 2) == top_average:
            print(f"  * {student['name']} ({student['group']})")