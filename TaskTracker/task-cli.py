import sys
import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def generate_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def add_task(description):
    tasks = load_tasks()
    task_id = generate_id(tasks)
    now = datetime.now().isoformat()
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task updated successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Task deleted successfully (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found")

def mark_in_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as in progress (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found")

def mark_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as done (ID: {task_id})")
            return
    print(f"Task with ID {task_id} not found")

def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [t for t in tasks if t['status'] == status]
    if not tasks:
        print("No tasks found")
        return
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created: {task['createdAt']}")
        print(f"Updated: {task['updatedAt']}")
        print("---")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task-cli.py <command> [args]")
        return

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: python task-cli.py add <description>")
            return
        description = sys.argv[2]
        add_task(description)
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: python task-cli.py update <id> <description>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid ID")
            return
        description = sys.argv[3]
        update_task(task_id, description)
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: python task-cli.py delete <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid ID")
            return
        delete_task(task_id)
    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Usage: python task-cli.py mark-in-progress <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid ID")
            return
        mark_in_progress(task_id)
    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Usage: python task-cli.py mark-done <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Invalid ID")
            return
        mark_done(task_id)
    elif command == 'list':
        status = sys.argv[2] if len(sys.argv) > 2 else None
        if status and status not in ['done', 'todo', 'in-progress']:
            print("Invalid status. Use done, todo, or in-progress")
            return
        list_tasks(status)
    else:
        print("Unknown command")

if __name__ == '__main__':
    main()