## Task Tracker CLI
A simple CLI tool for task management (todo/in-progress/done) that persists data to tasks.json.

## Description
A lightweight command-line utility to create, update, delete, and filter tasks.

## Features
Add a task: `add "description"`
Update description: `update <id> "new description"`
Delete a task: `delete <id>`
Mark status: `mark <id> <status> (todo, in_progress, done)`
List tasks: `list or list <status>`
Automatically saves data to tasks.json
Each task includes an id, description, status, createdAt, and updatedAt

## Requirements
Python 3.8+

## Installation
Clone the repository or copy the project files into a directory.
