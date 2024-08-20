import json
from datetime import datetime


class TaskTracker:
    Tasks = []

    def __init__(self):
        self.load_all_tasks()

    def load_all_tasks(self):
        """Loads Task list initially."""
        try:
            with open("tasks.json", 'r') as f:
                task_file = json.load(f)
                self.Tasks = task_file['tasks']
        except FileNotFoundError:
            self.Tasks = []

    def get_all_tasks(self):
        """Returns a list of all Tasks."""
        return self.Tasks

    def save_all_tasks(self):
        """Saves Task list to file."""
        json_data = json.dumps({"tasks": self.Tasks}, indent=4, sort_keys=True)
        with open("tasks.json", 'w') as f:
            f.write(json_data)


    def add_new_task(self, description: str):
        """Adds a new task to the Task list."""
        new_id = len(self.Tasks) + 1
        current_time = datetime.now()
        formatted_time = current_time.strftime("%m/%d/%Y %H:%M:%S")
        new_task = { "id": new_id, "description": description, "created_at": formatted_time, "updated_at": formatted_time, "status": 'todo'}
        self.Tasks.append(new_task)
        self.save_all_tasks()
        return new_task

    def get_tasks_by_status(self, status: str):
        """Returns Task list by status."""
        filtered_tasks = filter(lambda task: task['status'] == status, self.Tasks)
        return list(filtered_tasks)

    def update_task_by_id(self, task_id, description):
        """Updated a task description based on id."""
        found = False
        for task in self.Tasks:
            if task['id'] == task_id:
                task['updated_at'] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                task['description'] = description
                found = True
                break
        if found:
           self.save_all_tasks()
        return found

    def mark_task_status_by_id(self, task_id, status):
        """Updated task status based on id."""
        found = False
        for task in self.Tasks:
            if task['id'] == task_id:
                task['updated_at'] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                task['status'] = status
                found = True
                break
        if found:
            self.save_all_tasks()
        return found

    def delete_task_by_id(self, task_id):
        """Deletes a task based on id."""
        found = False
        for task in self.Tasks:
            if task['id'] == task_id:
                self.Tasks.remove(task)
                found = True
                break

        if found:
            self.save_all_tasks()
        return  found