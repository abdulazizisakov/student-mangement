from colored import cprint


menu_text = """
1. Barcha o‘quvchilarni ko‘rish
2. O‘quvchi qo‘shish
3. O‘quvchi ma’lumotlarini tahrirlash
4. O‘quvchini o‘chirish
5. O‘quvchini ID orqali qidirish
6. O‘quvchini ism orqali qidirish
7. O‘quvchiga baho qo‘shish
8. O‘quvchining baholarini ko‘rish
9. O‘rtacha bahoni ko‘rish
10. O‘quvchilar reytingi
11. Eng yuqori natijali o‘quvchi
0. Chiqish"""


def show_menu() -> None:
    cprint(
        text="===== STUDENT MANAGEMENT SYSTEM =====", fore_256="cyan", back_256="white"
    )


def menus() -> None:
    cprint(
        text=menu_text,
        fore_256="magenta"
    ),
    cprint("0. Chiqish", fore_256="red")


def break_line() -> None:
    cprint("-" * 100, fore_256= "black", back_256= "yellow")


def get_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        cprint("Xatolik! Bo'sh qiymat kiritib bo'lmaydi!", fore_256='red')


def get_positive_int(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        cprint("Xatolik! Musbat butun son kiriting", fore_256="red")


def print_student (student: dict) -> None
    print(
        f"ID: {student['id']} | Ism: {student['name']} | "
        f"Yosh: {student['age']} | Guruh: {student['group']}"
    )