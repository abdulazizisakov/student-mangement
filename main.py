from utils import show_menu, menus, break_line, cprint
from students import (
    show_all_students, 
    add_students, 
    edit_student, 
    delete_student,
    search_by_id,
    search_by_name)
from grades import add_grade, show_grades 
from reports import show_average, show_ranking, show_top_student


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

        elif choice == '5':
            search_by_id()

        elif choice == '6':
            search_by_name()

        elif choice == '7':
            add_grade()

        elif choice == '8':
            show_grades()

        elif choice == '9':
            show_average()

        elif choice == '10':
            show_ranking()

        elif choice == '11':
            show_top_student()
        
        elif choice == '0':
            print("Dastur yakunlandi. Xayr!")
            break

        else:
            cprint("Bunday menu mavjud emas!", fore_256='red')

main()
