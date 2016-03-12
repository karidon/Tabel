# -*- coding: utf-8 -*-


class Abstract(object):
	'''
	Abstract class
	'''

	def __init__(self, staff_member, civil_memeber=0):
		'''
		staff_member - атестованные сотрудники
		civil_member - гражданские служащие
		duty_part - дежурная часть

		:param staff_member: int
		:param civil_memeber: int
		:return:
		'''
		self.staff_member = staff_member
		self.civil_memeber = civil_memeber

	def weapon(self):
		'''
		Believes the weapons according to the regulations
		:return:
		'''
		pass

	def ammunition(self):
		'''
		Considers ammunition according to the regulations
		:return:
		'''
		pass

	def traning_weapons(self):
		'''
		Believes training weapons according to the regulations
		:return:
		'''
		pass

	def optical_equipment(self):
		'''
		Believes optical devices according to regulations
		:return:
		'''
		pass

	def military_chemical(self):
		'''
		Considers the military-chemical property according to the regulations
		:return:
		'''
		pass

	def personal_protection(self):
		'''
		Considers means of individual protection according to the regulations
		:return:
		'''
		pass

	def procent(self, arg, proc):
		'''
		Return matematic procent
		:param arg: int
		:param proc: int
		:return: int
		'''
		return int(((arg / 100) * proc) + 0.5)
