import json
from priority_ai import assign_priority
from reminder import send_reminder

TASK_FILE = "tasks.json"


# Функція для завантаження задач з файлу
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Функція для збереження задач у файл
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=2)


# Функція для додавання задачі
def add_task():
    text = input("Введіть текст задачі: ")
    priority = assign_priority(text)
    task = {"text": text, "priority": priority}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Задача додана з пріоритетом: {priority}")
    send_reminder(text)


# Функція для виведення списку задач
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список задач порожній.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['text']} [Пріоритет: {task['priority']}]")


# Функція для видалення задачі
def remove_task():
    list_tasks()
    index = int(input("Введіть номер задачі для видалення: ")) - 1
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Видалено задачу: {removed['text']}")
    else:
        print("Невірний номер задачі.")


# Головна функція для управління меню
def main():
    menu_actions = {
        "1": add_task,
        "2": list_tasks,
        "3": remove_task,
        "4": lambda: None,  # Заглушка для обработки выхода
    }

    while True:
        print("\nМеню:")
        print("1. Додати задачу")
        print("2. Показати задачі")
        print("3. Видалити задачу")
        print("4. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "4":
            break
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print("Невірний вибір!")


if __name__ == "__main__":
    main()
