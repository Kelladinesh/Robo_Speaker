#works only in MAC OS

import os
if __name__  == '__main__':
    print('Welcome to RoboSpeaker 1.1, created by KD')
    while True:
        x = input('Enter what you want me to speak: ')
        if x == 'q':
            os.system("say'bye bye Guys'")
            break
        command = f'say{x}'
        os.system(command)