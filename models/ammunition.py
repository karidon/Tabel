# -*- coding: utf-8 -*-

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-15'

from weapon import Weapon


class Ammunition(Weapon):
	"""Считает боеприпасы согласно положенности."""

	def pistol_catridges(self):
		'''
		Пистолетные патроны.
		:return: int
		'''
		return int((Weapon.guns(self) * 24) + (
			Weapon.pistol_gun(self) * 100))

	def automat_catridges(self):
		'''
		5,45 и 7,62 мм автоматные патроны.
		:return: int
		'''
		return int(
			(Weapon.automat(self) * 246) + (Weapon.hand_gun(self) * 750))

	def automat_catridges_tracer(self):
		'''
		5,45 и 7,62 мм автоматные патроны с трассирующе пулей.
		:return: int
		'''
		return int((Weapon.automat(self) * 54) + (Weapon.hand_gun(self) * 250))

	def sniper_catridges(self):
		'''
		7,62 мм винтовочные патроны снайперские.
		:return: int
		'''
		return int(Weapon.sniper_rifle(self) * 100)

	def special_carbine_catridges(self):
		'''
		18,5 мм патроны к специальным карабинам.
		:return: int
		'''
		return int(Weapon.special_carbine(self) * 16)

	def signal_catridges(self):
		'''
		Патроны сигнальные 18,5х60С.
		Патроны осветительные 18,5х60О.
		:return: int
		'''
		return int(Weapon.guns(self) * 4)

	def cartridge_lighting(self):
		'''
		26 мм патрон осветительный.
		26 мм патроны красного, зеленого, желтого огня каждого вида.
		:return: int
		'''
		return int(Weapon.signal_pistol(self) * 5)

	def rubber_bullet(self):
		'''
		Патрон с резиновой пулей.
		:return: int
		'''
		return int(
			(Weapon.special_carbine(self) * 250) + (Weapon.guns(self) * 48))

	def svetozvukovye(self):
		'''
		Патрон светозвуковой.
		:return: int
		'''
		return int(Weapon.guns(self) * 24)


if __name__ == '__main__':
	ammunit = Ammunition(120)
	assert ammunit.pistol_catridges() == 8880
	assert ammunit.automat_catridges() == 9618
	assert ammunit.automat_catridges_tracer() == 2282
	assert ammunit.sniper_catridges() == 100
	assert ammunit.special_carbine_catridges() == 32
	assert ammunit.signal_catridges() == 480
	assert ammunit.cartridge_lighting() == 10
	assert ammunit.rubber_bullet() == 6260
	assert ammunit.svetozvukovye() == 2880

	print('Ok')
