import json
import os
from datetime import datetime


class DatabaseManager:
    def __init__(self, filename):
        self.__filename = filename

    def __enter__(self):
        if os.path.exists(self.__filename):
            with open(self.__filename) as connection:
                self.__tasks = json.load(connection)
        else:
            self.__tasks = []

        return self

    @staticmethod
    def __gen_datetime():
        return datetime.now().strftime("%F %T.%f")[:-3]

    def add(self, description):
        if len(self.__tasks) > 0:
            id = max([entry["id"] for entry in self.__tasks]) + 1
        else:
            id = 0

        current_datetime = self.__gen_datetime()

        self.__tasks.append(
            {
                "id": id,
                "description": description,
                "status": "todo",
                "createdAt": current_datetime,
                "updatedAt": current_datetime,
            }
        )

    def update(self, id, description):
        task = next(entry for entry in self.__tasks if entry["id"] == id)
        current_datetime = self.__gen_datetime()
        task["description"] = description
        task["updatedAt"] = current_datetime

    def delete(self, id):
        task = next(entry for entry in self.__tasks if entry["id"] == id)
        self.__tasks.remove(task)

    def mark(self, id, status):
        task = next(entry for entry in self.__tasks if entry["id"] == id)
        current_datetime = self.__gen_datetime()
        task["status"] = status
        task["updatedAt"] = current_datetime

    def list(self, status):
        if status is None:
            return self.__tasks

        return [entry for entry in self.__tasks if entry["status"] == status]

    def __exit__(self, type, value, traceback):
        with open(self.__filename, "w") as connection:
            json.dump(self.__tasks, connection, indent=2, ensure_ascii=False)
