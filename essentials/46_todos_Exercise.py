
print(
"""
  _____         _          
 |_   _|__   __| | ___  ___
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \___\
   |_|\___/ \__,_|\___/|___/
"""
)

user_input = ""
todos = []
done_todos = []

while True:
    if( len(todos) > 0 ):
        print("ToDos : ")
        task_number = 1
        for task in todos:
            print(f"{task_number}. {task}")
            task_number += 1

    print("*******************************************************")
    user_input = input("Enter a command (Type 'h' for help 'q' for quit) : ").strip()

    if "q" == user_input.lower() :
        break

    if "h" == user_input.lower() :
        print("""
TODO LIST HELP
Type 'q' to quit
To add a todo to the list, type it and hit enter
To complete a todo enter its number
""")
        continue

    if user_input.isnumeric():
        task_number = int(user_input)
        if len(todos) == 0:
            print("There are no tasks in the Todo-list to mark completed")

        if task_number >= 1 and task_number <= len(todos):
            task = todos.pop(task_number-1)
            print(f"'{task}' Done !")
            done_todos.append(task)
        else:
            print("No such task to mark done!")

        continue

    else:
        todos.append(user_input)



if( len(done_todos) > 0 ):
    print(f"Today you completed {len(done_todos)} Todos: ")
    for task in done_todos:
        print(f"* {task}")
else:
    print("Today you have not completed any ToDos")

if( len(todos) > 0 ):
    print("Remaining ToDos : ")
    task_number = 1
    for task in todos:
        print(f"{task_number}. {task}")
        task_number += 1
else:
    print("You have no remaining ToDos!")
