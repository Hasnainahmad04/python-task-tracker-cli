import cmd

from TaskTracker import TaskTracker


class TaskCLI(cmd.Cmd):
    app = TaskTracker()
    prompt = '> '
    intro = """
    Welcome to TaskTracker. Type "help" for available commands.
    
    Available commands:
    - add: Adds a new task. Usage: add "[Task description]"
    - list: Lists tasks. Usage: list [status]
    - delete: Deletes a task by ID. Usage: delete 1
    - update: Updates a task by ID. Usage: update 1 "[Task description]"
    - mark: Marks a task status by ID. Usage: mark 1 [status]: status = ['in-progress', 'done']
    - exit: Exits the CLI.
    - help<command>: get more information about a command."""

    def do_add(self, line):

        """Adds a new Task.
        Usage:
        add "Task description"
        Example:
        add "Buy me a coffee"
        """


        if line.strip():
            task = self.app.add_new_task(line.replace("\"", ''))
            print(f"Task added successfully (ID: {task['id']})")
        else:
            print("Failed to add task")

    def do_list(self, line):

        """Lists tasks based on status.
        Usage:
        list -> Lists all tasks
        list todo -> Lists all tasks with status 'todo'
        list in-progress -> Lists all tasks with status 'in-progress'
        list done -> Lists all tasks with status 'done' """

        def list_tasks(task_list):
            if tasks:
                print("Listing Tasks")
                for task in task_list:
                    print(f"[{task['id']}] {task['description']} - {task['status']}")
            else:
                print("Your list is currently empty")

        statuses = ['todo', 'in-progress', 'done']

        if line.strip() == '':
           tasks = self.app.get_all_tasks()
           list_tasks(tasks)
        elif line.strip() in statuses:
            tasks = self.app.get_tasks_by_status(line)
            list_tasks(tasks)
        else:
            print("Invalid Status")

    def do_delete(self, line):
        """Deletes a task."""
        if not line.strip() or not line.strip().isdigit():
            print("Invalid ID")
            return False

        deleted = self.app.delete_task_by_id(int(line))
        if deleted:
            print(f"Task deleted successfully")
        else:
            print("Task could not be found")

    def do_update(self, line):
        """Updates a task by ID
        Usage: update [ID] [Description]
        Example: update 1 "I don't like coffee" """

        try:
            task_id, description = line.split(" ", 1)
            if not task_id.isdigit():
                print("Invalid ID")
                return False
            if description.strip():
                    updated = self.app.update_task_by_id(int(task_id), description.replace("\"", ''))
                    if updated:
                        print(f"Task updated successfully")
                    else:
                        print("Task could not be found")
        except ValueError as e:
            return False

    def do_mark(self, line):
        """Marks a task Status by ID.
        usage: mark [ID] [status]
        Example: mark 1 done"""

        try:
            task_id, status = line.split(" ", 1)
            if not task_id.isdigit():
                print("Invalid ID")
                return False
            if status.strip() in ['in-progress', 'done']:
               updated = self.app.mark_task_status_by_id(int(task_id), status)
               if updated:
                   print(f"Task Status updated successfully")
               else:
                   print("Task could not be found")
        except ValueError:
            return False


    def do_exit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    TaskCLI().cmdloop()