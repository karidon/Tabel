# -*- coding: utf-8 -*-

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-15'


class OpticalEquipment(object):
	"""Оптические приборы"""

	def __init__(self, count_duty_part=1, count_marching_unit=1):
		# Kолличество дежурных частей
		self.count_duty_part = int(abs(count_duty_part))
		# Kоличество строевых подразделений
		self.count_marching_unit = int(abs(count_marching_unit))

	def binoculars(self):
		'''
		Бинокль с увеличением 8 крат.
		:return: int
		'''
		return int((self.count_marching_unit * 3) + (self.count_duty_part * 1))

	def spotting(self):
		'''
		Зрительная труба.
		:return: int
		'''
		return int(self.count_marching_unit * 2)


if __name__ == '__main__':
	optic = OpticalEquipment()
	assert optic.binoculars() == 4
	assert optic.spotting() == 2
	optic2 = OpticalEquipment(2, 3)
	assert optic2.binoculars() == 11
	assert optic2.spotting() == 6
	print('Ok')
