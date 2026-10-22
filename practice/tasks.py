class Task:  # a blueprint for making tasks
    def __init__(self, task_id: int, title: str, status: str = "todo") -> None:  # runs automatically when a new task is created
        self.task_id = task_id  # store this task's id (a whole number)
        self.title = title  # store this task's title (text)
        self.status = status  # store this task's status; "todo" if none was given


class TaskNotFoundError(Exception):  # our own error type for "no task with this id"
    pass  # nothing extra needed; the name explains the error


class InvalidStatusError(Exception):  # error for a status that isn't allowed
    pass  # the name explains the error


ALLOWED_STATUSES = {"todo", "in_progress", "done"}  # the only statuses a task can have

tasks: list[Task] = []  # a list that holds all tasks; starts empty
next_id = 1  # the id the next new task will get; only ever goes up


def add_task(title: str) -> Task:  # create a new task and save it
    global next_id  # we want to change next_id, which lives outside this function
    task = Task(next_id, title)  # use the counter as this task's id
    tasks.append(task)  # put the new task at the end of the list
    next_id += 1  # move the counter up by 1 for the next task
    return task  # hand the new task back


def list_tasks() -> list[Task]:  # get all saved tasks
    return tasks  # hand back the whole list


def find_task(task_id: int) -> Task:  # get one task by its id
    for task in tasks:  # check each task one by one
        if task.task_id == task_id:  # is this the one?
            return task  # found it: hand it back and stop
    raise TaskNotFoundError(f"Task {task_id} not found")  # loop ended without finding it: raise our error


def update_status(task_id: int, new_status: str) -> Task:  # change a task's status
    if new_status not in ALLOWED_STATUSES:  # is this status on the allowed list?
        raise InvalidStatusError(f"'{new_status}' is not a valid status")  # no: reject it
    task = find_task(task_id)  # reuse find_task; it raises TaskNotFoundError if the task is missing
    task.status = new_status  # change the status
    return task  # hand back the updated task


def delete_task(task_id: int) -> None:  # remove a task by its id
    for task in tasks:  # check each task one by one
        if task.task_id == task_id:  # is this the task we want?
            tasks.remove(task)  # take it out of the list
            return  # stop here; the job is done


add_task("Edit client reel")  # id 1
add_task("Send invoice")  # id 2
add_task("Reply to outreach leads")  # id 3

update_status(1, "done")  # valid status on an existing task
print(find_task(1).title, find_task(1).status)  # -> Edit client reel done

try:  # attempt an invalid status
    update_status(2, "finished")  # "finished" isn't allowed
except InvalidStatusError as error:  # catch the invalid-status error
    print(f"Error: {error}")  # friendly message

try:  # attempt a task that doesn't exist
    update_status(99, "done")  # there is no task 99
except TaskNotFoundError as error:  # catch the not-found error
    print(f"Error: {error}")  # friendly message