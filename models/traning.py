# -*- coding: utf-8 -*-


__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-15'


class TraningWeapons(object):
	"""Учебное оружие согласно положенности"""

	def __init__(self, count_marching_unit=1):
		self.count_marching_unit = int(abs(count_marching_unit))

	def traning_gun(self):
		'''
		Пистолет учебный.
		Пистолет-пулемет учебный.
		5,45 (7,62) мм автомат учебный.
		:return: int
		'''
		return int(self.count_marching_unit * 1)


if __name__ == '__main__':
	tran = TraningWeapons()
	assert tran.traning_gun() == 1

	print('Ok')
