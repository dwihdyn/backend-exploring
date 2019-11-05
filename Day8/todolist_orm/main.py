# === dummy data, copy paste below in python shell ===

# first_user = UserName(owner_name='morning guy')
# first_user.save()

# morn_list = TodoList(name='morning list', list_owner = first_user)
# morn_list.save()

# nt1 = TodoTask(task='wake up', todo_list=morn_list)
# nt1.save()


# basic UI
import models as m

while True:
    enterred_username = str(input('''
    -----------------------------------------------------
            press `ctrl + c` or `ctrl + d` to exit
    -----------------------------------------------------
    welcome!

    enter username
    
    '''))

    enterred_pass = str(input('''

    enter password

    '''))
    current_user = m.UserName.get_or_none(
        m.UserName.owner_name == enterred_username)
    current_pass = m.UserName.get_or_none(m.UserName.password == enterred_pass)
    if current_user != None and current_pass != None:
        print("hi, what would you like to do today ?")
        while True:
            print(
                " ====================================================================== ")
            print(" ")
            print(' ===== UserName ===== ')
            print('1) create new user')
            print('2) delete user')
            print(' ===== TodoList ===== ')
            print('3) create new list')
            print('4) delete list')
            print(' ===== TodoTask ===== ')
            print('5) create new task')
            print('6) delete task')
            print('7) mark task done')
            print(' ===== General ===== ')
            print('8) see UserName table')
            print('9) see TodoList table')
            print('10) see TodoTask table')
            print('11) exit')
            print(" ")
            print("press any key to keep looping")
            print(" ")
            # print('''
            #             Another way
            #             to print
            #             multiple things
            # ''')
            choice = int(input('enter your choice : '))
            print(" ")
            print(
                " ====================================================================== ")

            # create new user
            if choice == 1:
                print(" ")
                new_user = input('enter new user name: ')
                new_pass = input('enter password: ')

                new_name = m.UserName(owner_name=new_user, password=new_pass)
                new_name.save()
                print(" ")
                print('new user successfully created !!')
                print(" ")

            # delete user
            elif choice == 2:
                print(" ")
                print("current available users : ")
                print("id    owner_name")
                for i in m.UserName.select():
                    print(f"{i.id}     {i.owner_name}")
                print(" ")
                sel_user = int(
                    input('enter the onwer id that to be deleted '))
                del_user = m.UserName.delete().where(m.UserName.id == sel_user)
                del_user.execute()
                print(" ")
                print('user successfully deleted !!')
                print(" ")

            # create new list
            elif choice == 3:
                print(" ")
                print("current available users : ")
                print("id    owner_name")
                for i in m.UserName.select():
                    print(f"{i.id}     {i.owner_name}")
                print(" ")

                which_user = int(input('which user id ? : '))
                new_list = input('enter the title of the list: ')

                redirect_which_user = m.UserName.get_by_id(which_user)

                todo_list = m.TodoList(
                    name=new_list, list_owner=redirect_which_user)
                todo_list.save()
                print(" ")
                print('new list successfully created !!')
                print(" ")

            # delete list
            elif choice == 4:
                print(" ")
                print("all lists available : ")
                print("id    name    owner_id")
                for i in m.TodoList.select():
                    print(f"{i.id}     {i.name}     {i.list_owner}")
                print(" ")
                del_input = int(input('enter list id delete : '))
                del_list = m.TodoList.delete().where(m.TodoList.id == del_input)
                del_list.execute()
                print(" ")
                print('list successfully deleted !!')
                print(" ")

            # create new task
            elif choice == 5:
                print(" ")
                print("all lists available : ")
                print("id    name    owner_id")
                for i in m.TodoList.select():
                    print(f"{i.id}     {i.name}     {i.list_owner}")
                print(" ")
                which_list = int(
                    input('enter list_id. which list does this task belongs to ? '))
                user_task = input('please enter a task :  ')

                # help to redirect which todolist should this task go to
                redirect_todo_list = m.TodoList.get_by_id(which_list)

                # add new task to the list
                todo_task = m.TodoTask(
                    task=user_task, todo_list=redirect_todo_list)
                todo_task.save()
                print(" ")
                print('new task successfully created !!')
                print(" ")

            # delete task
            elif choice == 6:
                print(" ")
                print("all tasks available : ")
                print("id    task    completed?     list_id")
                for i in m.TodoTask.select():
                    print(
                        f"{i.id}     {i.task}     {i.completed}     {i.todo_list}")
                print(" ")
                del_input = int(input('enter task id to be delete : '))
                del_task = m.TodoTask.delete().where(m.TodoTask.id == del_input)
                del_task.execute()
                print(" ")
                print('task successfully deleted !!')
                print(" ")

            # mark task done
            elif choice == 7:
                print(" ")
                print("all tasks available : ")
                print("id    task    completed?     list_id")
                for i in m.TodoTask.select():
                    print(
                        f"{i.id}     {i.task}     {i.completed}     {i.todo_list}")
                print(" ")
                done_input = int(input(
                    'enter task id to set as done : '))
                marked_done = m.TodoTask.update(completed='yesss').where(
                    m.TodoTask.id == done_input)
                marked_done.execute()
                print(" ")
                print('task successfully marked as done !!')
                print(" ")

            # see UserName tables
            elif choice == 8:
                print(" ")
                print("current available users : ")
                print("id    owner_name")
                for i in m.UserName.select():
                    print(f"{i.id}     {i.owner_name}")
                print(" ")

            # see TodoList tables
            elif choice == 9:
                print(" ")
                print("all lists available : ")
                print("id    name    owner id")
                for i in m.TodoList.select():
                    print(f"{i.id}     {i.name}     {i.list_owner}")
                print(" ")

            # see TodoTask tables
            elif choice == 10:
                print(" ")
                print("all tasks available : ")
                print("id    task    completed?     list_id")
                for i in m.TodoTask.select():
                    print(
                        f"{i.id}     {i.task}     {i.completed}     {i.todo_list}")
                print(" ")

            # exit
            elif choice == 11:
                print(" ")
                print(' goodbye ')
                print(" ")
                break
    else:
        print('username doesnt exist!!')
