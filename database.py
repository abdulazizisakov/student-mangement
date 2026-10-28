next_student_id = 3

students = [
    {
        "id": 1,
        "name": "Ali Valiyevich",
        "age": 16,
        "group": "Python-01",
        "grades": {
            "Python": [5, 4, 5],
            "Englsh": [4, 5]
        }
    },
    {
        "id": 2,
        "name": "Zaynab Karimova",
        "age": 17,
        "group": "Python-02",
        "grades": {
            "Python": [5, 5, 5],
            "Math": [4, 4]
        }
    },
    {
        "id": 3,
        "name": "Abdulaziz Isakov",
        "age": 20,
        "group": "DI 24-09",
        "grades": {
            "Python": [5, 4, 5],
            "Math": [5, 5],
            "Englsh": [4, 4, 5]
        }
    }
]


def get_new_id() -> int:
    global next_student_id
    new_id = next_student_id
    next_student_id += 1
    return new_id