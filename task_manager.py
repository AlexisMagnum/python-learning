import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks( ):
	if os.path.exists(TASKS_FILE):
		with open(TASKS_FILE, 'r') as f:
			return json.load(f)
	return []


def save_tasks(tasks):
	with open(TASKS_FILE, 'w') as f:
		json.dump(tasks, f, indent=2)


def add_task(title):
	tasks = load_tasks( )
	task = {
		'id': len(tasks) + 1,
		'title': title,
		'completed': False
	}
	tasks.append(task)
	save_tasks(tasks)
	print(f"Задача '{title}' добавлена!")


def list_tasks( ):
	tasks = load_tasks( )
	if not tasks:
		print("Нет задач!")
		return

	for task in tasks:
		status = "✓" if task['completed'] else "✗"
		print(f"{task['id']}. [{status}] {task['title']}")


def complete_task(task_id):
	tasks = load_tasks( )
	for task in tasks:
		if task['id'] == task_id:
			task['completed'] = True
			save_tasks(tasks)
			print(f"Задача {task_id} выполнена!")
			return
	print("Задача не найдена!")


if __name__ == "__main__":
	while True:
		print("\n=== Менеджер задач ===")
		print("1. Добавить задачу")
		print("2. Список задач")
		print("3. Завершить задачу")
		print("4. Выйти")

		choice = input("Выберите действие: ")

		if choice == '1':
			title = input("Введите задачу: ")
			add_task(title)
		elif choice == '2':
			list_tasks( )
		elif choice == '3':
			task_id = int(input("ID задачи: "))
			complete_task(task_id)
		elif choice == '4':
			break