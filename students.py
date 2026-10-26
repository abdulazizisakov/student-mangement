import database
from utils import get_text, get_positive_int, print_student, cprint


def show_all_students() -> None:
    if not database.students:
        cprint("O'quchilar ro'yxati bo'sh.", fore_256="yellow")
        return
    for student in database.students:
        print_student(student)


def add_students() -> None:
    name = get_text("Ism: ")
    age = get_positive_int("Yosh: ")
    group = get_text("Guruhi: ")

    student = {
        "id": database.get_new_id(),
        "name": name,
        "age": age,
        "group": group,
        "grades": {},
    }
    database.students.append(student)
    cprint(f"O'quvchi qo'shildi.  ID: {student['id']}", fore_256="green")
