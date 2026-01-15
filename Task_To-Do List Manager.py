tasks = []


def add_task():
    title = input(f'Title: ')
    description = input(f'Description: ')
    priority = input(f'Prioriy (Low,Medium,High): ')
    status = input(f'Status (Pending/In-Progress/Completed): ')
    task = {
        'title': title,
        'description': description,
        'priority': priority,
        'status': status
    }
    tasks.append(task)


def view_taks():
    if len(tasks) == 0:
        print(f'Sorry tasks List is empty. Add some')
        return
    i = 1
    for t in tasks:
        print(f'Task{i}'.center(20, '-'))
        print(f'''Title: {t['title']}
Description: {t['description']}
Prority: {t['priority']}
Status: {t['status']}
''')
        i += 1


def update_taks():
    if len(tasks) == 0:
        print(f'Tasks list is empty')
        return
    i = 0
    while True:
        user_task = input(f'Title: ').lower()
        for task in tasks:
            if user_task == task['title'].lower():
                new_status = input(
                    f'Change status (Pending/In-Progress/Completed)')
                task['status'] = new_status
                print(f'Status updates')
                return
        i += 1
        print(f'Title not found')
        if i == 3:
            print(f'Limit reach back to main menu')
            return


def delete_task():
    if len(tasks) == 0:
        print(f'Tasks list empty')
        return
    i = 0
    while True:
        user_title = input(
            f'Enter the title of the task you want to delete').lower()
        for task in tasks:
            if user_title == task['title'].lower():
                tasks.remove(task)
                return
        print(f'Title not found')
        i += 1
        if i == 3:
            print(f'Limit reach')
            return


def search_task():
    if len(tasks) == 0:
        print(f'Tasks List is empty')
        return
    while True:
        choice = int(input(f'''1:Search by Title
2:Search by Priority
3:Seach by Status
4:Exit
'''))
        if choice == 1:
            search_title = input('Title: ').lower()
            for task in tasks:
                if search_title == task['title'].lower():
                    print(f'''Title: {task['title']}
Description: {task['description']}
Priority: {task['priority']}
Status: {task['status']}
''')
                else:
                    print(f'Title does not exits')
        elif choice == 2:
            while True:
                priority_choice = int(input(f'''1:Low
2:Medium
3:High
4:Exit
'''))
                if priority_choice == 1:
                    found = False
                    for task in tasks:
                        print(' ')
                        if task['priority'].lower() == 'low':
                            print(f'''Title: {task['title']}
Priority:{task['priority']}
Status:{task['status']}
''')
                            found = True
                    if not found:
                        print(f'There are not any tasks with low priority')
                elif priority_choice == 2:
                    found = False
                    for task in tasks:
                        if task['priority'].lower() == 'medium':
                            print(' ')
                            print(f'''Title: {task['title']}
Priority:{task['priority']}
Status:{task['status']}
''')
                            found = True
                    if not found:
                        print(f'There are not any tasks with medium priority')
                elif priority_choice == 3:
                    found = False
                    for task in tasks:
                        print(' ')
                        if task['priority'].lower() == 'high':
                            print(f'''Title: {task['title']}
Priority:{task['priority']}
Status:{task['status']}
''')
                            found = True
                    if not found:
                        print(f'There are not any tasks with high priority')
                elif priority_choice == 4:
                    break
        elif choice == 3:
            while True:
                choice = int(input(f'''1:Pending
2:In-progress
3:Completed
4:Exit'''))
                if choice == 1:
                    found = False
                    for task in tasks:
                        if task['status'].lower() == 'pending':
                            print(f'''Title: {task['title']}
Pririoty:{task['priority']}
status: {task['status']}
''')
                            found = True
                if not found:
                    print(f'There are no tasks with status in pending')

                elif choice == 2:
                    found = False
                    for task in tasks:
                        if task['status'].lower() == 'in progress':
                            print(f'''Title: {task['title']}
Pririoty:{task['priority']}
status: {task['status']}
''')
                            found = True
                    if not found:
                        print(f'There are no tasks with status in progress')
                elif choice == 3:
                    found = False
                    for task in tasks:
                        if task['status'].lower() == 'completed':
                            print(f'''Title: {task['title']}
Pririoty:{task['priority']}
status: {task['status']}
''')
                            found = True
                    if not found:
                        print(f'There are no tasks with status completed')
                elif choice == 4:
                    break
        elif choice == 4:
            break


def extra():
    while True:
        choice = int(input(f'''1:Completed and Pending Tasks
2: Tasks Priority Base (High,Medium,Low)
3: Clear completed tasks
4: Exit
'''))
        if choice == 1:
            complete = []
            pending_taks = []
            for task in tasks:
                if task['status'].lower() == 'completed':
                    complete.append(task)
                if task['status'].lower() == 'pending':
                    pending_taks.append(task)
            print(f'Completed Task: {len(complete)}')
            print(f'pending Taks: {len(pending_taks)}')
        elif choice == 2:
            for task in tasks:
                if task['priority'].lower() == 'high':
                    print(f'''Title: {task['title']}
Priority: {task['priority']}
''')
            for task in tasks:
                if task['priority'].lower() == 'medium':
                    print(f'''Title: {task['title']}
Priority: {task['priority']}
''')
            for task in tasks:
                if task['priority'].lower() == 'low':
                    print(f'''Title: {task['title']}
Priority: {task['priority']}
''')
        elif choice == 3:
            keep_tasks = []
            for task in tasks:
                if task['status'].lower() != 'completed':
                    keep_tasks.append(task)
            tasks.clear()
            tasks.extend(keep_tasks)
        elif choice == 4:
            break


while True:
    choice = int(input(f'''1:Add a Task
2:View All Tasks
3:Update Task Status
4:Delete a Task
5:Search Tasks
6:Extra
7:Exit
'''))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_taks()
    elif choice == 3:
        update_taks()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        search_task()
    elif choice == 6:
        extra()
    elif choice == 7:
        break
