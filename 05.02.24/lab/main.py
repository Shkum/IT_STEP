from museum_app import MuseumApp
if __name__ == "__main__":
    app = MuseumApp()

    while True:
        print("\nМеню:")
        print("1. Додати експонат")
        print("2. Видалити експонат")
        print("3. Редагувати інформацію про експонат")
        print("4. Перегляд повної інформації про експонат")
        print("5. Виведення інформації про всі експонати")
        print("6. Перегляд інформації про людей, які мають відношення до певного експонату")
        print("7. Перегляд інформації про експонати, що мають відношення до певної людини")
        print("8. Перегляд набору експонатів на основі певного критерію")
        print("0. Вихід")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            exhibit_data = {
                'name': input("Введіть назву експонату: "),
                'description': input("Введіть опис експонату: "),
                'category': input("Введіть категорію експонату: "),
                'related_people': input("Введіть імена людей через кому, які мають відношення до експонату (натисніть Enter, якщо немає): ").split(',')
            }
            app.add_exhibit(exhibit_data)
        elif choice == "2":
            exhibit_id = input("Введіть ID експонату для видалення: ")
            app.delete_exhibit(exhibit_id)
        elif choice == "3":
            exhibit_id = input("Введіть ID експонату для редагування: ")
            new_data = {
                'name': input("Введіть нову назву експонату (натисніть Enter, якщо не хочете змінювати): "),
                'description': input("Введіть новий опис експонату (натисніть Enter, якщо не хочете змінювати): "),
                'category': input("Введіть нову категорію експонату (натисніть Enter, якщо не хочете змінювати): "),
                'related_people': input("Введіть нові імена людей через кому, які мають відношення до експонату (натисніть Enter, якщо не хочете змінювати): ").split(',')
            }
            app.edit_exhibit(exhibit_id, new_data)
        elif choice == "4":
            exhibit_id = input("Введіть ID експонату для перегляду повної інформації: ")
            result = app.view_exhibit_info(exhibit_id)
            print(f"Інформація про експонат {exhibit_id}: {result}")
        elif choice == "5":
            results = app.view_all_exhibits()
            print(f"Інформація про всі експонати: ")
            for result in results:
                print(result)
        elif choice == "6":
            exhibit_id = input("Введіть ID експонату для перегляду інформації про людей, які мають відношення: ")
            result = app.view_related_people(exhibit_id)
            print(f"Інформація про людей, які мають відношення до експонату {exhibit_id}: {result}")
        elif choice == "7":
            person_name = input("Введіть ім'я людини для перегляду інформації про пов'язані експонати: ")
            result = app.view_related_exhibits(person_name)
            print(f"Інформація про експонати, які мають відношення до людини {person_name}: {result}")
        elif choice == "8":
            category = input("Введіть категорію для перегляду експонатів: ")
            results = app.view_exhibits_by_category(category)
            print(f"Експонати у категорії {category}:")
            for result in results:
                print(result)
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")