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