import json

print("=== Добро пожаловать в систему управления библиотекой ===")
print(" ")

books = []

def load_from_file():
    global books
    try:
        with open("library.json", "r", encoding="utf-8") as file:
            books = json.load(file)
        print("Данные успешно загружены из файла.")
    except FileNotFoundError:
        print("Файл с данными не найден. Начинаем с пустой библиотеки.")
    except json.JSONDecodeError:
        print("Ошибка при чтении файла. Файл может быть поврежден.")
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")

def save_to_file():
    try:
        with open("library.json", "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
        print("Данные успешно сохранены в файл.")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def add_book():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    new_book = {"title": title, "author": author, "status": "доступна"}
    books.append(new_book)
    print(f"Книга '{title}' успешно добавлена.")

def remove_book():
    title = input("Введите название книги для удаления: ")
    for book in books:
        if book['title'].lower() == title.lower():
            books.remove(book)
            print(f"Книга '{title}' успешно удалена.")
            return
    print(f"Книга с названием '{title}' не найдена.")

def display_books():
    if not books:
        print("В библиотеке пока нет книг.")
    else:
        for book in books:
            print(f"'{book['title']}' by {book['author']} - {book['status']}")

def search_book():
    title = input("Введите название книги для поиска: ")
    for book in books:
        if book['title'].lower() == title.lower():
            print(f"'{book['title']}' by {book['author']} - {book['status']}")
            return
    print(f"Книга с названием '{title}' не найдена.")

def change_book_status():
    title = input("Введите название книги для изменения статуса: ")
    for book in books:
        if book['title'].lower() == title.lower():
            new_status = "взята" if book['status'] == 'доступна' else 'доступна'
            book['status'] = new_status
            print(f"Статус книги '{book['title']}' изменен на '{new_status}'.")
            return
    print(f"Книга с названием '{title}' не найдена.")

load_from_file()
while True:
    try:
        print("""Выберите действие:
            1. Добавить новую книгу
            2. Удалить книгу
            3. Показать все книги
            4. Найти книгу
            5. Изменить статус книги
            6. Выйти""")
        user_choice = int(input("Выберите действие (1-6): \n"))

        if user_choice == 1:
            add_book()
        elif user_choice == 2:
            remove_book()
        elif user_choice == 3:
            display_books()
        elif user_choice == 4:
            search_book()
        elif user_choice == 5:
            change_book_status()
        elif user_choice == 6:
            save_to_file()
            print('Спасибо за использование системы управления библиотекой. До свидания!')
            exit()
    except ValueError:
        print('Некорректный выбор. Пожалуйста, выберите число от 1 до 6.')
