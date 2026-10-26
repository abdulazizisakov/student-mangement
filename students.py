import database
from utils import get_text, get_positive_int, print_student, find_student_by_id, cprint


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


def edit_student() -> None:
    student_id = get_positive_int("O'quvchi ID si: ")
    student = find_student_by_id(student_id)

    if student is None:
        cprint("Bu ID dagi o'quvchi topilmadi!", fore_256="red")
        return

    print("Hozirgi ma'lumot: ")
    print_student(student)
    print("O'zgartirmaslik uchun 'Enter'ni bosing")

    new_name = input(f"Yangi ism [{student['name']}]: ").strip()
    if new_name:
        student['name'] = new_name

    while True:
        new_age = input(f"Yangi yosh [{student['age']}]: ").strip()
        if not new_age:
            break
        
        if new_age.isdigit() and int(new_age) > 0:
            student ["age"] = new_age
            break

        cprint("Xatoli! Musbat son kiriting.", fore_256="red")

    new_group = input(f"Yangi guruh [{student['group']}]: ").strip()
    if new_group:
        student ['group'] = new_group

    cprint("Ma'lumotlar yangilandi.", fore_256="green")


def delete_student() -> None:
    student_id = get_positive_int("O'quvchi ID si: ")
    student = find_student_by_id(student_id)

    if student is None:
        cprint("Bu ID dagi o'quvchi topilmadi!", fore_256="red")
        return

    database.students.remove(student)
    cprint(f"'{student['name']}' o'chirildi.", fore_256="green")