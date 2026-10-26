from utils import show_menu, menus, break_line, cprint
from students import show_all_students, add_students, edit_student, delete_student


def main() -> None:
    while True:
        show_menu()
        menus()
        choice = input("> ").strip()
        break_line()

        if choice == '1':
            show_all_students()
        
        elif choice == '2':
            add_students()

        elif choice == '3':
            edit_student()

        elif choice == '4':
            delete_student()
        
        elif choice == '0':
            print("Dastur yakunlandi. Xayr!")
            break

main()
