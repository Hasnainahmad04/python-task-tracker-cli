# TaskTracker

**TaskTracker** is a simple command-line interface (CLI) tool for managing tasks. It allows you to add, list, update, and delete tasks, all stored in a `json` file.

## Features

- **Add New Tasks**:  add new tasks with a description and default status of `todo`.
- **List Tasks**: View all tasks or filter tasks by status (`todo`, `in-progress`, `done`).
- **Update Task Description**: Update the description of an existing task by its ID.
- **Update Task Status**: Change the status of a task (`todo`, `in-progress`, `done`) by  its ID.
- **Delete Tasks**: Delete a tasks by it's ID


## Usage

### Running the CLI

To start the TaskTracker CLI, run the following command:

```bash
python app.py
```

### Add a new Task
Adds a new task to the list
```bash
add [task description]
```

### List Tasks
To list all tasks, use the `list` command:
```bash
list
```
To list task by status, use:
```bash
list [status]
e.g: list todo
```
### Update Task 
To update a task: use the `update` command
```bash
update [ID] [new description]
```

### Change Task Status
To Change task status, use the `mark` command
```shell
mark [ID] [status]
usage: mark 1 done
```

### Delete
To delete an existing task, use the `delete` command
```shell
delete [ID]
usage: delete 1
```

### Exit
use the `exit` command when you are done.

## Project Link
Project Link: [Task Tracker](https://roadmap.sh/projects/task-tracker) by [roadmap.sh](https://roadmap.sh)

