# -*- coding: utf-8 -*-


def procent(arg, proc):
		'''
		Return matematic procent
		:param arg: int
		:param proc: int
		:return: int
		'''
		if arg == 0:
			return 'Неправильно ввели! Вы ввели {}'.format(arg)
		return int(((arg / 100) * proc) + 0.5)




if __name__ == '__main__':
	assert procent(120, 50) == 60
	assert procent(0, 50) == 'Неправильно ввели! Вы ввели 0'
	print('Ok')
