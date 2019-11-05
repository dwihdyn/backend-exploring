# === dummy data, copy paste below in python shell

# first_user = UserName(owner_name='do wee')
# first_user.save()

# night_list = TodoList(name='night list')
# night_list.save()

# nt1 = TodoTask(task='go sleep', todo_list=night_list)
# nt1.save()


# basic UI
import models as m


print('hi, what would you like to do today ?')
while True:
    print(" ")
    print(" please type everything in lower case ")
    print('1) create new list')
    print('2) create new task')
    print('3) exit')
    print('4) delete task')
    print('5) delete list')
    print('6) marked task done')
    print(" ")
    print("press any key to keep looping")
    print(" ")
    # print('''
    #             Another way
    #             to print
    #             multiple things
    # ''')
    choice = int(input('enter your choice : '))

    # create new list
    if choice == 1:
        print(" ")
        new_list = input('enter the title of the list: ')
        todo_list = m.TodoList(name=new_list)
        todo_list.save()
        print(" ")
        print('new list successfully created !!')
        print(" ")

    # create new task
    elif choice == 2:
        print(" ")
        print('lists :')
        print('1) Morning Routine List')
        print('2) Night List')
        print(" ")
        which_list = int(input('which list does this task belongs to ? '))
        user_task = input('please enter a task :  ')

        # help to redirect which todolist should this task go to
        redirect_todo_list = m.TodoList.get_by_id(which_list)

        # add new task to the list
        todo_task = m.TodoTask(task=user_task, todo_list=redirect_todo_list)
        todo_task.save()
        print(" ")
        print('new task successfully created !!')
        print(" ")

    # exit
    elif choice == 3:
        print(" ")
        print(' goodbye ')
        print(" ")
        break

    # delete task
    elif choice == 4:
        print(" ")
        del_input = input('enter which task to delete (word by word type) : ')
        del_task = m.TodoTask.delete().where(m.TodoTask.task == del_input)
        del_task.execute()
        print(" ")
        print('task successfully deleted !!')
        print(" ")

    # delete list
    elif choice == 5:
        print(" ")
        del_input = input('enter which list to delete (word by word type) : ')
        del_list = m.TodoList.delete().where(m.TodoList.name == del_input)
        del_list.execute()
        print(" ")
        print('list successfully deleted !!')
        print(" ")

    # mark task done (t done, f not done)
    elif choice == 6:
        print(" ")
        done_input = input(
            'enter which task to set as done (word by word type) : ')
        marked_done = m.TodoTask.update(completed='yesss').where(
            m.TodoTask.task == done_input)
        marked_done.execute()
        print(" ")
        print('task successfully marked as done !!')
        print(" ")
