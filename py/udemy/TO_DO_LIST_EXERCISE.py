header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""
print(header)


todos = []
completed = []
while True:
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")
    print("********************")
    print("Enter a command. Type 'h' for help:")
    command = input("> ")
    if command == "q":
        break
    elif command  =="h":
        print("TODO LIST HELP.")
        print("Type q to quit.")
        print("To add a todo, type it to enter.")
        print("To quit press q. To remove from list press number.")
    elif command.isnumeric():
        idx = int(command) - 1
        if idx >= len(todos):
            print("THERE IS NO TODO WITH THAT NUMBER!")
        else:
            done_todo = todos.pop(idx)
            completed.append(done_todo)
    else: 
        todos.append(command)
print("Ok, goodbye!")
if completed:
    print(f"You completed {len(completed)} todos today:")
    for todo in completed:
        print(f"*{todo}")