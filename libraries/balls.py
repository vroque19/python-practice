from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

# print('About to go BALLS!')

sleep(2)

phrase = "Ed Balls"
#phrase = "would than thing up can small most this right as part give however general early and possible part life own would lead way for end leave old might play one about before come around off present great same again order look after too leave and for work look because follow face small over nation need one find"


keyboard.type(phrase)
print('done')

