# Часть 2. Журнал оценок

journal = {
    "Али": [5, 4, 5],
    "Мадина": [3, 4],
    "Тимур": [2, 3, 3]
}

while True:
    print("\n===== ЖУРНАЛ ОЦЕНОК =====")
    print("1 — Показать всех учеников")
    print("2 — Добавить ученика")
    print("3 — Поставить оценку")
    print("4 — Средний балл ученика")
    print("5 — Лучший ученик")
    print("6 — Список отстающих")
    print("7 — Удалить ученика")
    print("8 — Статистика группы")
    print("0 — Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        if not journal:
            print("Учеников пока нет")
        else:
            for name, grades in journal.items():
                print(name + ":", grades)

    elif choice == "2":
        name = input("Имя ученика: ")
        if name in journal:
            print("Такой ученик уже есть")
        else:
            journal[name] = []
            print("Ученик добавлен!")

    elif choice == "3":
        name = input("Имя ученика: ")
        if name not in journal:
            print("Ученика нет")
        else:
            grade = input("Оценка (1-5): ")
            if grade in ["1", "2", "3", "4", "5"]:
                journal[name].append(int(grade))
                print("Оценка добавлена!")
                print(name, ":", journal[name])
            else:
                print("Неверная оценка")

    elif choice == "4":
        name = input("Имя ученика: ")
        if name not in journal:
            print("Ученика нет")
        elif not journal[name]:
            print("У ученика нет оценок")
        else:
            avg = sum(journal[name]) / len(journal[name])
            print("Средний балл", name, ":", round(avg, 2))

    elif choice == "5":
        best_name = ""
        best_avg = -1

        for name, grades in journal.items():
            if not grades:
                continue

            avg = sum(grades) / len(grades)

            if avg > best_avg:
                best_avg = avg
                best_name = name

        if best_name:
            print("Лучший ученик:", best_name, "-", round(best_avg, 2))
        else:
            print("Нет оценок")

    elif choice == "6":
        found = False
        print("Отстающие (средний ниже 3.5):")

        for name, grades in journal.items():
            if grades:
                avg = sum(grades) / len(grades)
                if avg < 3.5:
                    print(name, "—", round(avg, 2))
                    found = True

        if not found:
            print("Отстающих нет")

    elif choice == "7":
        name = input("Имя ученика: ")
        if name in journal:
            del journal[name]
            print("Ученик удалён")
        else:
            print("Ученика нет")

    elif choice == "8":
        if not journal:
            print("Журнал пустой")
        else:
            all_grades = []

            for grades in journal.values():
                all_grades.extend(grades)

            print("Учеников:", len(journal))
            print("Всего оценок:", len(all_grades))

            if all_grades:
                print("Общий средний балл:",
                      round(sum(all_grades) / len(all_grades), 2))
                print("Встречаются оценки:", set(all_grades))
            else:
                print("Оценок пока нет")

    elif choice == "0":
        print("До свидания!")
        break

    else:
        print("Нет такого пункта меню")



