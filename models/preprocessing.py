# -*- coding: utf-8 -*-


def procent(arg, proc):
	'''
	Return matematic procent
	:param arg: int
	:param proc: int
	:return: int
	'''
	# TODO : надо подумать если proc = 0
	arg = int(abs(arg))
	proc = int((abs(proc)))
	if arg == 0 or proc == 0:
		return 'Неправильно ввели! Вы ввели arg = {0} proc = {1}'.format(arg, proc)
	return int(((arg / 100) * proc) + 0.5)


if __name__ == '__main__':
	assert procent(120, 50) == 60
	assert procent(0, 50) == 'Неправильно ввели! Вы ввели arg = 0 proc = 50'
	assert procent(50, 0) == 'Неправильно ввели! Вы ввели arg = 50 proc = 0'
	assert procent(-120, 50) == 60


	print('Ok')
