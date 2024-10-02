#Empty list stored in a variable named "todo".
todos = []

# Ensures that the code below will run whilst TRUE (as in always unless defined as false).
while True:
    # Asks user for input to defined question and stores in variable named "user_action".
    user_action = input("Type add, show, edit, complete or exit: ")
    # Updates variable "User_action" and strips data type of all white spacing.
    user_action = user_action.strip()
    # match & case function that works same was a switch & case in JS.
    match user_action:
        # Defines each case (scenario).
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            # Takes data that is stored in variable "todo" and the appends to list names "todos".
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            # Adds a numeric value to each item with the list "todos"
            for index, item in enumerate(todos):
                # Users and "f" string to insert "-" between both variables that are printed in output.
                # Also adds 1 to enumerated value to avoid confusion to the user.
                row = f"{index + 1}-{item}"
                # Prints perviously defines "f" string.
                print(row)
        case 'edit':
            # Asks user for input and converts value to an integer data type.
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            # Takes user anser from previous input question and refers to corresponding list item.
            # The updates that index value with new item request in previous question.
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            # Takes numeric answer from previous question and refers it to list index.
            # Then removes the value linked to the index number.
            todos.pop(number -1)
        case 'exit':
            # Ends "match" funtion. Then moves on to next line of code.
            break

print("Bye!")


    

