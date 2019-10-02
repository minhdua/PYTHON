# SaitamaCoder
import re


def validity(password):
	check = True
	if (len(password) < 8): check = False
	elif not re.search('[a-z]',password) : check = False
	elif not re.search('[A-Z]',password) : check = False
	elif not re.search('[0-9]',password) : check = False
	elif not re.search('[_,@,&]',password) : check = False
	elif re.search('\s',password) : check = False
	return check

def Main():
	password = input()
	if validity(password) : print ('Valid Password')
	else : print('Invalid Password')

if __name__ == '__main__':
	Main()
