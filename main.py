from utils import show_menu, menus, break_line, cprint
from students import show_all_students, add_students


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
        
        elif choice == '0':
            print("Dastur yakunlandi. Xayr!")
            break

main()
