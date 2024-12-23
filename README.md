# Tasks

Tasks tracking CLI app build using Python.

## Features

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

## Constraints

- Accept user inputs using positional arguments in the command line
- Store data in JSON file
- External libraries or frameworks are not allowed

The idea was taken from: https://roadmap.sh/projects/task-tracker

## Usage

Show help:

```sh
python -m tasks --help
```

Show help for subcommand e.g. `add`:

```sh
python -m tasks add --help
```

Add new task:

```sh
python -m tasks add "Task description"
```

Update task:

```sh
python -m tasks update ID "New task description"
```

Remove task:

```sh
python -m tasks delete ID
```

Change task status:

```sh
python -m tasks mark ID [todo,in-progress,done]
```

List tasks:

```sh
python -m tasks list
```

List tasks by status:

```sh
python -m tasks list [todo,in-progress,done]
```