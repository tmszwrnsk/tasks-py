import argparse

from tasks.database import DatabaseManager

parser = argparse.ArgumentParser(prog="tasks")
subparsers = parser.add_subparsers(dest="action", required=True)

parser_add = subparsers.add_parser("add", help="add task")
parser_add.add_argument("description", type=str, help="task description")

parser_update = subparsers.add_parser("update", help="update task")
parser_update.add_argument("id", type=int, help="task id")
parser_update.add_argument("description", type=str, help="new task description")

parser_delete = subparsers.add_parser("delete", help="delete task")
parser_delete.add_argument("id", type=int, help="task id")

parser_mark = subparsers.add_parser("mark", help="change task status")
parser_mark.add_argument("id", type=int, help="task id")
parser_mark.add_argument(
    "status", choices=["todo", "in-progress", "done"], help="new task status"
)

parser_list = subparsers.add_parser("list", help="list tasks")
parser_list.add_argument(
    "status",
    nargs="?",
    choices=["todo", "in-progress", "done"],
    default=None,
    help="filter tasks by status",
)

args = parser.parse_args()

with DatabaseManager("database.json") as database:

    if args.action == "add":
        database.add(args.description)

    elif args.action == "update":
        database.update(args.id, args.description)

    elif args.action == "delete":
        database.delete(args.id)

    elif args.action == "mark":
        database.mark(args.id, args.status)

    elif args.action == "list":
        tasks = database.list(args.status)
        if tasks:
            longest_id = max(2, max(len(str(entry["id"])) for entry in tasks))
            longest_description = max(len(entry["description"]) for entry in tasks)
            longest_status = max(6, max(len(entry["status"]) for entry in tasks))
            print(
                "{0:>{1}}   {2:>{3}}   {4:>{5}}   {6:>{7}}   {8:>{9}}".format(
                    "ID",
                    longest_id,
                    "TASK",
                    longest_description,
                    "STATUS",
                    longest_status,
                    "CREATED AT",
                    23,
                    "UPDATED AT",
                    23,
                )
            )
            for task in tasks:
                print(
                    "{0:>{1}}   {2:>{3}}   {4:>{5}}   {6}   {7}".format(
                        task["id"],
                        longest_id,
                        task["description"],
                        longest_description,
                        task["status"],
                        longest_status,
                        task["createdAt"],
                        task["updatedAt"],
                    )
                )
