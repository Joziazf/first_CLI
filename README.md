# Task Tracker CLI

Простой CLI-проект для управления задачами (todo/in-progress/done), хранящий данные в `tasks.json`.

## Описание
Небольшой инструмент командной строки для создания, обновления, удаления и фильтрации задач. 

## Возможности
- Добавить задачу: `add "description"`
- Обновить описание: `update <id> "new description"`
- Удалить задачу: `delete <id>`
- Пометить статус: `mark <id> <status>` (`todo`, `in_progress`, `done`)
- Список задач: `list` или `list <status>`
- Автоматическое хранение в `tasks.json`
- Каждая задача имеет `id`, `description`, `status`, `createdAt`, `updatedAt`

## Требования
- Python 3.8+

## Установка
1. Клонируйте репозиторий или скопируйте файлы проекта в папку.
