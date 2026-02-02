# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage your tasks. This project helps practice programming skills including filesystem operations, user input handling, and building CLI applications.

## Features

- Add, update, and delete tasks
- Mark tasks as in progress or done
- List all tasks or filter by status (done, todo, in-progress)

## Requirements

- Python 3.x
- No external libraries required

## Installation

1. Clone or download the project.
2. Ensure Python is installed on your system.

## Usage

Run the CLI using Python:

```bash
python task-cli.py <command> [arguments]
```

### Commands

- **Add a new task:**
  ```
  python task-cli.py add "Buy groceries"
  ```
  Output: Task added successfully (ID: 1)

- **Update a task:**
  ```
  python task-cli.py update 1 "Buy groceries and cook dinner"
  ```

- **Delete a task:**
  ```
  python task-cli.py delete 1
  ```

- **Mark a task as in progress:**
  ```
  python task-cli.py mark-in-progress 1
  ```

- **Mark a task as done:**
  ```
  python task-cli.py mark-done 1
  ```

- **List all tasks:**
  ```
  python task-cli.py list
  ```

- **List tasks by status:**
  ```
  python task-cli.py list done
  python task-cli.py list todo
  python task-cli.py list in-progress
  ```

## Task Properties

Each task has the following properties stored in `tasks.json`:

- `id`: Unique identifier
- `description`: Task description
- `status`: Status (todo, in-progress, done)
- `createdAt`: Creation timestamp
- `updatedAt`: Last update timestamp

## Error Handling

The application handles common errors such as invalid IDs, missing arguments, and unknown commands gracefully.