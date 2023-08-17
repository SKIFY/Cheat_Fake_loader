#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random, psutil, time, os
from art import tprint
from alive_progress import alive_bar



######################## CHANGE THIS ########################
game_name = 'valorant'
cheat_name = 'VALORANT HACK'
target_game_proccess_names = ['valorant']

files_count = random.randint(49,61)
######################## DON'T CHANGE THIS ########################


def set_logo(is_: bool = True):
	if is_: os.system('cls')

	tprint(f'{cheat_name}\n\n','stop')


set_logo()
with alive_bar(total=files_count, title='Downloading libraries', theme='smooth', force_tty=True) as bar:
	for i in range(files_count):
		if i < 14:
			bar.text = 'Downloading a packed archive'
		elif i < 23:
			bar.text = 'Unpacking archive'
		elif i < 34:
			bar.text = 'Changing script configuration'
		elif i < 50:
			bar.text = 'Downloading program interface'
		elif i < 62:
			bar.text = 'Compiling script'
		time.sleep(float(f'.{random.randint(1,9)}') if random.choice([True,False]) else float(f'.0{random.randint(4,9)}'))
		bar()

######################## ADD YOUR CODE ########################





######################## ADD YOUR CODE ########################

set_logo()
print(f'The cheat is ready for injection, run {game_name}')
gg=False
while True:
	for p in psutil.process_iter():
		for x in target_game_proccess_names:
			if x in str(p.name()).lower():
				gg=True
				break
	if gg: break
	time.sleep(5)

for x in range(6):
	for x in ['.','..','...']:
		print(f'Injecting cheat in {game_name}%s'%x, end='\r')
		time.sleep(.7)
		print(end=f"{' '*100}\r")

set_logo()
print('The cheat is successfully injected, to open the cheat menu, press F8 in the game')
while True:
	gg=True
	for p in psutil.process_iter():
		for x in target_game_proccess_names:
			if x in str(p.name()).lower():
				gg=False
				break
	if gg: break
	time.sleep(5)

for x in range(2):
	for x in ['.','..','...']:
		print("The game was closed, I'm removing the traces of the cheat%s"%x, end='\r')
		time.sleep(.4)
		print(end=f"{' '*100}\r")
input('All traces are removed, press ENTER to close')
