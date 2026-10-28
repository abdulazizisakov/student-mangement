from utils import (
    get_text,
    get_positive_int,
    get_grade,
    find_student_by_id,
    cprint
)


def add_grade() -> None:
    student_id = get_positive_int("O'quvchi ID si: ")
    student = find_student_by_id(student_id)

    if student_id is None:
        cprint("Bu ID dagi o'quvchi topilmadi!", fore_256='red')
        return

    subject = get_text("Fan nomi: ")
    grade = get_grade("Baho (1-5 gacha): ")

    if subject not in student['grades']:
        student['grades'][subject] = []

    student['grades'][subject].append(grade)

    cprint(f"student['name'] ga  {subject} fanidan  {grade} baho qo'shildi.", fore_256='green')


def show_grades() -> None:
    
    student_id = get_positive_int("O'quvchi ID si: ")
    student = find_student_by_id(student_id)

    if student is None:
        cprint("Bu ID dagi o'quvchi topilmadi!", fore_256='red')
        return

    if not student["grades"]:
        cprint(f"{student["name"]}da hali baholar yo'q", fore_256='yellow')
        return

        print(f"{student['name']} baholari:")
    for subject, grade_list in student["grades"].items():
        print(f"  {subject}: {', '.join(map(str, grade_list))}")