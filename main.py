import os, time

listOfThings = []


def printList():
  os.system("clear")
  counter = 1
  print("To Do List")
  for item in listOfThings:
    print(f"{counter}: {item}")
    counter += 1
  time.sleep(3)

while True:
  print("To Do List Manager:")
  print()
  action = input("1.View\n2.Add\n3.Remove\n4.Edit\n5.Delete List\n> ")
  if action == "1":
    printList()
    time.sleep(1)
  elif action == "2":
    item = input("> ")
    listOfThings.append(item)
    time.sleep(.5)
  elif action == "3":
    os.system("clear")
    printList()
    task = input("> ")
    if task in listOfThings:
      approval = input(f"Are you sure you want to remove {task}? ")
      if approval == "yes":
        listOfThings.remove(task)
    else:
      print("Sorry this doesn't exist in your list")
      time.sleep(3)
  elif action == "4":
    printList()
    edit = input("Which item do you want to edit?\n> ")
    if edit in listOfThings:
      print(edit)
      new_edit = input("New edit\n> ")
      listOfThings.remove(edit)
      listOfThings.append(new_edit)
  elif action == "5":
    approval = input("Are you sure you want to delete this list completely?\n> ")
    if approval == "yes":
      listOfThings.clear()
    else:
      continue
  os.system("clear")
