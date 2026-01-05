import sys
import os
import json
from datetime import datetime

file_name = 'tasks.json'

def check_file():
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            json.dump([], f)
        return []

    if os.path.getsize(file_name) == 0:
        return []

    with open(file_name, 'r', encoding='UTF-8') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(file_name, 'w', encoding='UTF-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if len(sys.argv) < 2:
    print('Команда не указана')
    sys.exit()

command = sys.argv[1]

if command == 'add':
    if len(sys.argv) < 3:
        print('Описание задачи не указано')
        sys.exit()

    description = sys.argv[2]
    tasks = check_file()

    if not tasks:
        new_id = 1
    else:
        ids = []
        for task in tasks:
            ids.append(task['id'])
        new_id = max(ids) + 1

    task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': now(),
        'updatedAt': now()
    }

    tasks.append(task)
    save_tasks(tasks)

if command == 'list':
    tasks = check_file()
    if len(sys.argv) == 2:
        if not tasks:
            print('Задач ещё нет')
        else:
            for task in tasks:
                print(f"{task['id']}. {task['description']} [{task['status']}] [{task['createdAt']}]")
    elif len(sys.argv) == 3:
        if not tasks:
            print('Задач еще нет')
        else:
            for task in tasks:
                if task['status'] == sys.argv[2]:
                    print(f"{task['id']}. {task['description']}")

if command == 'mark':
    tasks = check_file()
    if len(sys.argv) == 4:
        for task in tasks:
            if task['id'] == int(sys.argv[2]):
                task['status'] = sys.argv[3]
                task['updatedAt'] = now()
                save_tasks(tasks)
                print(f'У задачи {int(sys.argv[2])} статус заменён на {sys.argv[3]}')
    else:
        print('Данные указаны неверно')


if command == 'update':
    tasks = check_file()
    if len(sys.argv) == 4:
        for task in tasks:
            if task['id'] == int(sys.argv[2]):
                task['description'] = sys.argv[3]
                task['updatedAt'] = now()
                save_tasks(tasks)
                print(f'Вы успешно изменили описание у задачи {int(sys.argv[2])}')
    else:
        print('Данные указаны неверно')

if command == 'delete':
    tasks = check_file()
    if len(sys.argv) == 3:
        new_tasks = [task for task in tasks if task['id'] != int(sys.argv[2])]
        if len(tasks) == len(new_tasks):
            print(f'Задача {int(sys.argv[2])} не найдена')
        else:
            save_tasks(new_tasks)
            print(f'Задача {int(sys.argv[2])} была удалена')
    else:
        print('Данные указаны неверно')