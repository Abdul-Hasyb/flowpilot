class Task:  # a blueprint for making tasks
    def __init__(self, task_id: int, title: str, status: str = "todo") -> None:  # runs automatically when a new task is created
        self.task_id = task_id  # store this task's id (a whole number)
        self.title = title  # store this task's title (text)
        self.status = status  # store this task's status; "todo" if none was given


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

def delete_task(task_id: int) -> None:  # remove a task by its id
    for task in tasks:  # check each task one by one
        if task.task_id == task_id:  # is this the task we want?
            tasks.remove(task)  # take it out of the list
            return  # stop here; the job is done

add_task("Edit client reel")  # add first task -> gets id 1
add_task("Send invoice")  # add second task -> gets id 2
add_task("Reply to outreach leads")  # add third task -> gets id 3

delete_task(2)  # remove "Send invoice"
add_task("Post a reel")  # what id will this get?

for task in list_tasks():  # go through every task, one at a time
    print(task.task_id, task.title, task.status)  # show its id, title and status on one line