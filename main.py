from utils import show_menu, menus, break_line


def main() -> None:
    while True:
        show_menu()
        menus()
        choice = input("> ")
        break_line()


main()
