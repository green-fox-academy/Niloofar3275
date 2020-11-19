    Todo is an app that you can use to keep up with your daily tasks. You can add or delete tasks and you can check if you already did a task.

1. run the application with the python todo_app.py -l command
expected: if we have some tasks in file.txt then app print your task
for example :
1-[] Walk the dog

2-[] Buy milk

3-[] Do homework

or if we don't have any task the app should print "No todos for today " since you haven't added any task yet.
2. run the application with the python todo_app.py -a "Feed the monkey" command
expected: the app will add feed the monkey to file.txt and print "add feed the monkey to the list"
or if run the application with the python todo_app.py -a print " Unable to add: no task provided" since you haven't added any task yet.
3. run the application with the python todo_app.py -r task number command
expected: Then the app should remove the specific task from the file.txt
for example :python todo_app.py -r 2
then the app remove the second task from the file
4. run the application with the python todo_app.py -r command
expected: the app will print "Unable to remove: no index provided"
5.  run the application with the python todo_app.py -r any number command
if any number is higher than tasks number expected: the app will print "Unable to remove: index is out of bound"
6. run the application with the python todo_app.py -r a word command
expected: the app will print "Unable to remove: index is not a number"
7. run the application with the python todo_app.py -c task number command
expected: Then the app should check the specific task from the file.txt
8. run the application with the python todo_app.py -c task number command
expected: Then the app should remove the specific task from the file.txt
for example :python todo_app.py -c 2
then the app remove the second task from the file
9. run the application with the python todo_app.py -c command
expected: the app will print "Unable to remove: no index provided"
10.  run the application with the python todo_app.py -c any number command
if any number is higher than tasks number expected: the app will print "Unable to remove: index is out of bound"
11. run the application with the python todo_app.py -c a word command
expected: the app will print "Unable to remove: index is not a number" 