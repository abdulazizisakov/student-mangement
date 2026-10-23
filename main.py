from utils import show_menu, break_line


def main() -> None:
    while True:
        show_menu()
        choice = input("> ")
        break_line()


main()
