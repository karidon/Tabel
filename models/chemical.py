# -*- coding: utf-8 -*-


__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-16'

from preprocessing import procent


class MilitaryChemical(object):
	"""Военно-химическое имущество на строевое подразделение """

	def __init__(self, staff_member, civil_memeber=0, count_marching_unit=1):
		# Kолличество атестованных людей.
		self.staff_member = int(abs(staff_member))
		# Гражданские служащие.
		self.civil_memeber = int(abs(civil_memeber))
		# Количество строевых подразделений6
		self.count_marching_unit = count_marching_unit

	def calculates_masks(self):
		'''
		Общевойсковой фильтрирующий противогаз (гражданский противогаз).
		:return:
		'''
		return procent((self.staff_member + self.civil_memeber), 110)

	def calculates_additional_cartridge(self):
		'''
		Дополнительный патрон, аналогичный ДПГ-3
		:return: int
		'''
		return procent((self.staff_member + self.civil_memeber), 50)

	def calculates_respirator(self):
		'''
		Респиратор
		:return: int
		'''
		return procent((self.staff_member + self.civil_memeber), 10)

	def calculates_guffs(self):
		'''
		Утеплительные манжеты (НМУ)
		:return: int
		'''
		return self.calculates_masks() * 2

	def calculates_ozk(self):
		'''
		Общевойсковой защитный комплект (защитный плащ, аналогичный ОП-1 - 1 шт.
		чулки защитные - 1 пара, перчатки защитные - 1 пара)
		:return: int
		'''
		return int(self.staff_member + self.civil_memeber)

	def calculates_light_protective_suit(self, platoon):
		'''
		Легкий защитный костюм, аналогичный Л-1 (комплект)
		На взвод строевого подразделения
		:platoon int
		:return: int
		'''
		# Количество взводов
		self.platoon = int(abs(platoon))
		return int(self.platoon * 5)

	def calculates_metere_dose(self):
		'''
		Измеритель мощности дозы (комплект)
		:return: int
		'''
		return int(self.count_marching_unit * 1)

	def calculates_combined_arms(self):
		'''
		Общевойсковой комплект измерителей дозы, аналогичный ИД-1
		:return: int
		'''
		return int(((self.staff_member + self.civil_memeber) / 30) + 0.5)

	def calculates_vpxr(self, count_patrol):
		'''
		Прибор химической разведки войсковой, аналогичный ВПХР.
		:param count_patrol: int
		:return: int
		'''
		# Разведывательный дозор
		self.count_patrol = int(abs(count_patrol))
		return int((self.count_marching_unit * 1) + (self.count_patrol * 1))

	def calculates_tube(self):
		'''
		Комплект контрольных трубок (ККТ)
		:return: int
		'''
		return self.calculates_vpxr(self.count_patrol) * 5


	# TODO: Подумать как лучше сделать ИПП как функцию или self передовать




if __name__ == '__main__':
	military = MilitaryChemical(120, 10)
	assert military.calculates_masks() == 143
	assert military.calculates_additional_cartridge() == 65
	assert military.calculates_respirator() == 13
	assert military.calculates_guffs() == 286
	assert military.calculates_ozk() == 130
	assert military.calculates_light_protective_suit(4) == 20
	assert military.calculates_metere_dose() == 1
	assert military.calculates_combined_arms() == 4
	assert military.calculates_vpxr(1) == 2
	assert military.calculates_tube() == 10
	assert military.staff_member == 120 # индивидуальный противохимический пакет

	print('Ok')
