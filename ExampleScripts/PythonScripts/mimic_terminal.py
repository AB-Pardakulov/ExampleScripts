import os
import time
import random
import tkinter
from tkinter import ttk 
import datetime
from colorama import Fore
import nltk
nltk.download('words')
from nltk.corpus import words
word_list = words.words()
print("The Password is -> 1234 \nIn order to skip the password, type yes at the start \nIn order to receive a list of commands once authorized, type help \nSome commands can be used simultaneously in the same input")
time.sleep(2.5)
def find_time(d_t):
  time_var = datetime.datetime.now()
  time_year = str(time_var.year)
  time_month = str(time_var.month)
  time_day = str(time_var.day)
  time_hour = str(time_var.hour)
  time_minute = str(time_var.minute)
  time_second = str(time_var.second)
  if (len(time_hour) == 1):
    time_hour = "0" + time_hour
  if (len(time_minute) == 1):
    time_minute = "0" + time_minute
  if (len(time_second) == 1):
    time_second = "0" + time_second
  date = "Today is " + time_month+"/"+time_day+"/"+time_year
  time = "The time is " + time_hour+":"+time_minute+":"+time_second + " (UTC)"
  if (d_t == "date"):
    return date
  if (d_t == "time"):
    return time
def print_custom(string, color, space):
  if (color == 0):
    if (space == True):
      print()
    print(string)
    if (space == True):
      print()
  else:
    if (space == True):
      print()
    print(color + string)
    if (space == True):
      print()
def make_up_funny_filenames(amount):
  addons = ["-utils", ".md", ".txt", ".appimage", "-configs", "_res", "ui", "co", "_merge", "Cache.sln", ".py", "_01.cpp", ".corrupt", ".htm", ".dem", ".asm", "_idx", ".flv", ".gif", "_xls", ".xls", ".svg", "--bin", ".terr", ".cpp", ".c", ".fbx", ".xml", "-temp", "-dlc", "sdk", ".rar", ".zip", "-compress", ".dll", ".docx", "-main", ".csv", "64", "32", "*"]
  function_list = []
  for i in range(amount):
    random_file = random.randint(0, len(word_list) - 1)
    random_file = word_list[random_file]
    random_addon = random.randint(0, len(addons) - 1)
    random_file = random_file + addons[random_addon]
    function_list.append(random_file.lower())
  return function_list
for i in range(30):
  os.system("clear")
  random_word0 = random.randint(1,len(word_list) - 1)
  print_custom(word_list[random_word0], Fore.GREEN, False)
  print_custom("Confirming Functions" + "." * (i%5), Fore.RED, False)
  time.sleep(0.05)
my_secret = os.environ['peng']
tester = input(Fore.BLUE + "Are you testing this program? \nRespond with 'yes' in order to skip the password. \nResponse: ")
tester = tester.lower()
if ("yes" in tester):
  access_level = 2
else: 
  access_level = 0
# Password needed whenever access_level is 0
locked = False
# Locked variable only used whenever the lock function is used within the terminal 
while (access_level == 0):
  password_response = input("PASSWORD: ")
  if (password_response == "1234"):
    print_custom("You're in!", Fore.GREEN, False)
    access_level = 1
  else:
    print_custom("Access Denied", Fore.RED, False)
if (access_level == 1):
  print_custom("Human Verification: ", Fore.WHITE, False)
while (access_level == 1): 
  input1 = input(Fore.WHITE + "What is the difference between a stone and a tree? ")
  input1 = input1.lower()
  time.sleep(0.1)
  if ("liv" in input1 or "lif" in input1 or "organ" in input1):
    print_custom("You are a human", Fore.GREEN, False)
    print_custom("Success! Human Verified", Fore.WHITE, False)
    access_level = 2
  elif ("0" in input1 or "1" in input1):
    print_custom("You are a robot", Fore.RED, False)
  else:
    print_custom("Try Again.", Fore.RED,False)
current_dir = "nothing"
main_dir_names = ["cd", "cd ", "cd/", "cd /"]
sys = make_up_funny_filenames(500)
boot = make_up_funny_filenames(25)
nabeeh = make_up_funny_filenames(5)
help = ["nothing_here", "placeholder*"]
nabeeh.append("nabeeh_himself")
nabeeh.append("placeholder*")
NonEmptyDirs = ["sys", "home", "boot", "nabeeh", "help"]
dir1 = ["home","nabeeh","boot","help","sys","placeholder*"]
home = ["downloads","browser","images","desktop","placeholder*"]
available_commands = ["cd (directory name)", "ls", "help", "su", "lock", "ui", "curses_ui", "apt", "install (program name)", "time", "print all words", "search (query)", "find word (query)"]
search_repofiles = make_up_funny_filenames(275000)
if (access_level == 2):
  print_custom("Access Level is now 2, you now have administrator controls...", Fore.WHITE, False)
  print_custom("Type 'help' to receive a list of commands", Fore.WHITE, False)
  level = "USER$/" 
  dir_level = 0
while (0 == 0):  
  while (access_level == 2 or access_level == 3):
    one_temp = 1
    two_temp = 1
    input_admin = input(Fore.BLUE + level)
    input_admin = input_admin.lower()
    bash_found = False
    if (input_admin.lower() == "help"):
      bash_found = True
      print_custom("Available Commands:", Fore.CYAN, False)
      for i in range (len(available_commands)):
        print(available_commands[i])
    if ("cd" in input_admin and " ls" not in input_admin):
      temp_dir_level = dir_level
      bash_found = True
      for i in range(len(main_dir_names)):
        if (main_dir_names[i] == input_admin):
          level = "USER$/"
          dir_level = 0
          one_temp = 0
          two_temp = 0
      if (one_temp == 1 and dir_level == 0):
        for i in range(len(dir1)):
          if (dir1[i] in input_admin and dir1[i] not in level and dir_level == 0):
            level = level + dir1[i] + "/"
            current_dir = dir1[i]
            dir_level = 1
            one_temp = 0
        if (one_temp == 1 and temp_dir_level == 0):
          print_custom("Couldn't find this directory", Fore.RED, False)
      if (two_temp == 1 and dir_level == 1):
        for i in range(len(home)):
          if (home[i] in input_admin and home[i] not in level and dir_level == 1):
            level = level + home[i] + "/"
            current_dir = home[i]
            dir_level = 2
            two_temp = 0
        for i in range(len(sys)):
          if (sys[i] in input_admin and sys[i] not in level and dir_level == 1):
            if ("." not in input_admin):
              level = level + sys[i] + "/"
              current_dir = sys[i]
              dir_level = 2
              two_temp = 0
            else:
              two_temp = 0
              print_custom("Files are not directories.", Fore.RED, False)
        for i in range(len(boot)):
          if (boot[i] in input_admin and boot[i] not in level and dir_level == 1):
            if ("." not in input_admin):
              level = level + boot[i] + "/"
              current_dir = boot[i]
              dir_level = 2
              two_temp = 0
            else:
              two_temp = 0
              print_custom("Files are not directories.", Fore.RED, False)
        for i in range(len(nabeeh)):
          if (nabeeh[i] in input_admin and nabeeh[i] not in level and dir_level == 1):
            if ("." not in input_admin):
              level = level + nabeeh[i] + "/"
              current_dir = nabeeh[i]
              dir_level = 2
              two_temp = 0
            else:
              two_temp = 0
              print_custom("Files are not directories.", Fore.RED, False)
        for i in range(len(help)):
          if (help[i] in input_admin and help[i] not in level and dir_level == 1):
            if ("." not in input_admin):
              level = level + help[i] + "/"
              current_dir = help[i]
              dir_level = 2
              two_temp = 0
            else:
              two_temp = 0
              print_custom("Files are not directories.", Fore.RED, False)
        if (two_temp == 1 and temp_dir_level == 1):
            print_custom("Couldn't find this directory", Fore.RED, False)
    if ("ls" in input_admin and "cd" not in input_admin): 
      bash_found = True
      if dir_level == 0:
        for i in range(len(dir1) - 1):
          print_custom(dir1[i], Fore.YELLOW, False)
      if dir_level == 1 and current_dir == NonEmptyDirs[1]:
        for i in range(len(home) - 1):
          print_custom(home[i], Fore.YELLOW, False)
      if dir_level == 1 and current_dir == NonEmptyDirs[0]:
        for i in range(len(sys) - 1):
          print_custom(sys[i], Fore.YELLOW, False)
      if dir_level == 1 and current_dir == NonEmptyDirs[2]:
        for i in range(len(boot) - 1):
          print_custom(boot[i], Fore.YELLOW, False)
      if dir_level == 1 and current_dir == NonEmptyDirs[3]:
        for i in range(len(nabeeh) - 1):
          print_custom(nabeeh[i], Fore.YELLOW, False)
      if dir_level == 1 and current_dir == NonEmptyDirs[4]:
        for i in range(len(help) - 1):
          print_custom(help[i], Fore.YELLOW, False)
      
    elif ("ls" in input_admin and "cd" in input_admin and dir_level == 0): 
      bash_found = True
      print_custom("The LS command does not take composite arguments", Fore.YELLOW, False)
    if ("su" == input_admin.lower()):
      bash_found = True
      password_response = input("PASSWORD NEEDED: ")
      if (password_response == my_secret):
        if (access_level == 2):
          print(Fore.GREEN + "Access Level now 3")
          access_level = 3
        else:
          print(Fore.GREEN + "Access Level reduced to 2")
          access_level = 2
      else:
        print(Fore.RED + "Access Denied")
    if ("lock" in input_admin):
      bash_found = True
      access_level = 0
      locked = True
    if ("ui" == input_admin):
      bash_found = True
      for i in range(1):
        main = Tk(className = "OS")
        main.geometry("540x320")
        window = ttk.Frame(main, padding = 15)
        window.place()
        text1 = ttk.Label(main, text="Welcome to my OS!").place(x=0,y=0)
        date = find_time("date")
        time = find_time("time")
        text2 = ttk.Label(main, text=date).place(x=0,y=20)
        text3 = ttk.Label(main, text=time).place(x=0,y=40)
        destroy_button = ttk.Button(main, text="Quit",command=main.destroy).place(x=0,y=295)
        main.configure(bg="#AB0068")
        main.mainloop()
    if ("curses_ui" == input_admin):
      bash_found = True
      print_custom("not available yet...", Fore.CYAN, False)
    if ("apt" in input_admin):
      bash_found = True
      print_custom("APT currently holds no function....", Fore.CYAN, False)
    if ("install" in input_admin and "install"!=input_admin and "install "!=input_admin and "install  "!=input_admin):
      bash_found = True
      item_installed = input_admin[8:len(input_admin)+1]
      print("Starting to download dependencies and files...")
      for i in range(random.randint(5,25)):
        random0 = random.randint(1,5)
        if (random0 == 1):
          print("Searching for dependencies...")
        elif (random0 == 2):
          print("Checking for conflicts")
        elif (random0 == 3):
          print("." * random0 * random.randint(1,4))
        elif (random0 == 4):
          print("Determining File-System Config")
        elif (random0 == 5):
          print("Updating all processes...")
        time.sleep(random.randint(1,5)/10)
        random1 = random.randint(1,4)
        random2 = random.randint(1,len(word_list) - 1)
        if (random1 == 1):
          print("Installing dependency #" + str(random.randint(1,500)))
          print()
        elif (random1 == 2):
          print("Installing file #" + str(i))
          print()
        elif (random1 == 3):
          print("Installing the " + word_list[random2] + " dependency")
          print()
        elif (random1 == 4):
          print("Installing the " + word_list[random2] + " file")
          print()
        time.sleep(random.randint(1,5)/10)
        random1 = random.randint(1,3)
        if (random1 == 1):
          print(Fore.WHITE + "Updating system database....")
        elif (random1 == 2):
          print(Fore.WHITE + "Configuring your system..." + "." * random.randint(3,10))
        else:
          print(Fore.WHITE + "Checking for errors" + "." * random.randint(3,10))
      random2 = random.randint(1,10)
      if (random2 == 1):
        print(Fore.RED + "Error: " + item_installed + " couldn't be installed. Try updating or try another repository")
      else:
        print_custom(item_installed + " successfully installed!", Fore.GREEN, False)
        dir1.insert(0, item_installed)
        make_up_funny_filenames(random.randint(9,64))
    elif ("install" == input_admin or "install " == input_admin):
      bash_found = True
      print(Fore.RED + "You cannot install nothing!?")
    if (input_admin.lower() == "time"):
      bash_found = True
      date = find_time("date")
      time = find_time("time")
      print_custom(date, Fore.GREEN, False)
      print_custom(time, Fore.GREEN, True)
    if (input_admin.lower() == "print all words"):
      bash_found = True
      for i in range (len(word_list)):
        print_custom(word_list[i], Fore.CYAN, False)
    if ("search" in input_admin.lower()):
      bash_found = True
      if ("search" == input_admin.lower()):
        for i in range(len(search_repofiles)):
          print_custom(search_repofiles[i], Fore.MAGENTA, False)
      else: 
        amount = 0
        response = input_admin[7:len(input_admin)+1]
        response = response.lower()
        for i in range(len(search_repofiles)):
          if (response in search_repofiles[i]):
            print_custom(search_repofiles[i], Fore.MAGENTA, False)
            amount = amount + 1
        if (amount > 1):
          print_custom(str(amount)+" items found with your search: "+"["+response+"]", Fore.GREEN, False)
        elif (amount == 1):
          print_custom(str(amount)+" item found with your search: "+"["+response+"]", Fore.YELLOW, False)
        else:
          print_custom(str(amount)+" items found with your search: "+"["+response+"]", Fore.RED, False)
    if ("find word" in input_admin.lower()):
      bash_found = True
      if ("find word" == input_admin.lower()):
        print_custom("You must specify...", Fore.RED, False)
      else: 
        amount = 0
        response = input_admin[10:len(input_admin)+1]
        response = response.lower()
        for i in range(len(word_list)):
          if (response in word_list[i]):
            print_custom(word_list[i], Fore.MAGENTA, False)
            amount = amount + 1
        if (amount > 1):
          print_custom(str(amount)+" english words found with your search: "+"["+response+"]", Fore.GREEN, False)
        elif (amount == 1):
          print_custom(str(amount)+" english word found with your search: "+"["+response+"]", Fore.YELLOW, False)
        else:
          print_custom(str(amount)+" english words found with your search: "+"["+response+"]", Fore.RED, False)
    if (bash_found == False):
      if (input_admin == ""):
        print_custom("Bash cannot be empty", Fore.MAGENTA, False)
      elif (input_admin in word_list):
        print_custom("Bash: " + input_admin + ": command not found, but matches an english word,perhaps this function doesn't exist?", Fore.MAGENTA, False)
      else:
        print_custom("Bash: " + input_admin + ": command not found, and doesn't match an english word, perhaps there is a typo?", Fore.MAGENTA, False)
  
  
  while (access_level == 0 and locked == True):
    current_dir = ""
    password_ = input("PASSWORD: ")
    if (password_ == my_secret):
      print(Fore.GREEN + "You're back in!")
      access_level = 2
      locked = False
    else:
      print_custom("Access Denied", Fore.RED, True)