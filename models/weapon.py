# -*- coding: utf-8 -*-

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-15'

from preprocessing import procent


class Weapon(object):
	"""Считает оружие согласно положенности в стоевом подразделении"""

	def __init__(self, staff_member, count_duty_part=1, count_marching_unit=1):
		'''
		:param staff_member: int
		:return:
		'''
		# Kолличество атестованных людей
		self.staff_member = staff_member
		# Kолличество дежурных частей
		self.count_duty_part = count_duty_part
		# Kоличество строевых подразделений
		self.count_marching_unit = count_marching_unit

	def pistol(self):
		'''
		Пистолеты
		:return: int
		'''
		return int(self.staff_member)

	def bestally_pistol(self):
		'''
		Бесствольные пистолеты
		:return: int
		'''
		return int(self.staff_member)

	def pistol_gun(self):
		'''
		Пистолет-пулемет
		:return: int
		'''
		return procent(self.staff_member, 50)

	def signal_pistol(self):
		'''
		Cигнальный пистолет.
		:return: int
		'''
		return int((self.count_marching_unit * 1) + (self.count_duty_part * 1))

	def automat(self):
		'''
		5,45 мм или 7,62 мм автомат.
		:return: int
		'''
		return int(procent(self.staff_member, 25) + (self.count_duty_part * 3))

	def hand_gun(self):
		'''
		5,45 мм или 7,62 мм ручной пулемет
		:return: int
		'''
		return int(self.count_marching_unit * 2)

	def sniper_rifle(self):
		'''
		7,62 мм снайперская винтовка
		:return: int
		'''
		return int(self.count_duty_part * 1)

	def special_carbine(self):
		'''
		18,5 мм карабин специальный.
		:return: int
		'''
		return int(self.count_duty_part * 2)


if __name__ == '__main__':
	weapon = Weapon(120)
	assert weapon.pistol() == 120
	assert weapon.bestally_pistol() == 120
	assert weapon.pistol_gun() == 60
	weapon_odd = Weapon(121)
	assert weapon_odd.pistol_gun() == 61
	assert weapon_odd.signal_pistol() == 2
	assert weapon_odd.hand_gun()
	weapon_zero = Weapon(50, count_duty_part=0, count_marching_unit=0)
	assert weapon_zero.hand_gun() == 0

	print('Ok')
