notes = []
next_id = 1
PROJ_NAME = "*NOTE-BOOK*"


def show_menu():
    print(f"Тебя приветствует {PROJ_NAME}")
    print("=" * 20)
    print("1. Добавить заметку")
    print("2. Показать заметки")
    print("3. Удалить заметку")
    print("=" * 20)
    choice = int(input("Выбери действие 1-3:"))

    if choice == 1:
        add_note()
    elif choice == 2:
        show_notes()
    else:
        print("Ты инвалид! иди в меню!")
        show_menu()


def add_note():
    title = input("Введите имя заметки")
    content = input("Введите содержимое заметки")
    global next_id
    note = {
        'id': next_id,
        'title': title,
        'content': content
    }

    notes.append(note)
    next_id += 1
    print(f"Заметка номер {note['id']} добавлена!")
    show_menu()


def show_notes():
    print(f"Всего заметок {len(notes)}")
    for note in notes:
        print("=" * 20)
        print(f"[{note['id']}] * {note['title']}")
        print(f"{note['content']}")
    show_menu()


def delete_note_by_id():
    pass


show_menu()





