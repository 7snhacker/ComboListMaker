import string
import random
import os
print("""   
                     _           
                    | |          
  ___ ___  _ __ ___ | |__   ___  
 / __/ _ \| '_ ` _ \| '_ \ / _ \ 
| (_| (_) | | | | | | |_) | (_) |
 \___\___/|_| |_| |_|_.__/ \___/ 
                                                                 
""")
print("Combo list Maker")
print("@7snhacker")
print("")
print("")
print("$ -1 One user combo ")
print("$ -2 list user combo ")
print("$ -3 random user combo ")
x = input("# ")
if x == '1':
    user1 = input(str("User : "))
    pass1 = open('password.txt','r')
    dn1 = open('combo.txt', 'a')
    done = 0
    li = 0
    m = 0
    while li == 0:
        pss = pass1.readline().split("\n")[0]
        done += 1
        print(done)
        dn1.write(f'{user1}:{pss}' + "\n")
        if pss == '':
            print("Done [*]")
            print("")
            print("")
            print('$ -0 back')
            print("")
            print("")
            r = input("# ")
            if r == '0':
                os.system("clear")
                os.system("python3 combomaker.py")
            dn1.close()
if x == '2':
    user2 = open('list.txt','r')
    pass2 = open('password.txt', 'r')
    dn2 = open('combo.txt', 'a')
    done = 0
    li = 0
    m = 0
    while li == 0:
        us2 = user2.readline().split("\n")[0]
        pss2 = pass2.readline().split("\n")[0]
        done += 1
        print(done)
        dn2.write(f'{us2}:{pss2}' + "\n")
        if pss2 == '':
            print("Done [*]")
            print("")
            print("")
            print('$ -0 back')
            print("")
            print("")
            ff = input("# ")
            if ff == '0':
                os.system("clear")
                os.system("python3 combomaker.py")
            dn1.close()
if x == '3':
    letters = string.ascii_lowercase
    user = int(input("letter count : "))
    passz = open('password.txt', 'r')
    dn3 = open('combo.txt', 'a')
    done = 0
    li = 0
    m = 0
    while li == 0:
        zzz = (''.join(random.choice(letters) for i in range(user)))
        pss = passz.readline().split("\n")[0]
        done += 1
        print(done)
        dn3.write(f'{zzz}:{pss}' + "\n")
        if pss == '':
            print("Done [*]")
            print("")
            print("")
            print('$ -0 back')
            print("")
            print("")
            hed = input("# ")
            if hed == '0':
                os.system("clear")
                os.system("python3 combomaker.py")
            dn3.close()















