import os

if __name__ == '__main__':
    print("welcome to robospeaker 1.1 created by harry")
    while True:
        x= input('enter what you want to pronoune')
        if x=='q':
            os.system('say bye bye friend')
            break
        command=f"say {x}"
        os.system(command)