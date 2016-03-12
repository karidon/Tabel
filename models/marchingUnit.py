# -*- coding: utf-8 -*-


from abstract import Abstract


class MarchingUnit(Abstract):
	'''
	Marching Unit - строевое подразделение
	'''

	# TODO: Сколько дежурных частей
	# TODO: Сколько строевых подразделений


	def __init__(self, staff_member, count_platoon, civil_memeber=0,
	             count_marching_unit=1,
	             count_duty_part=1, count_patrol=1):
		'''

		:param staff_member: int
		:param marching_unit: int
		:param duty_part: int
		:return:
		'''
		Abstract.__init__(self, staff_member, civil_memeber)
		self.count_duty_part = count_duty_part  # количество дежурных частей
		self.count_marching_unit = count_marching_unit  # количество строевых подразделений
		self.count_platoon = count_platoon
		self.count_patrol = count_patrol  # разведовательный дозор

	def weapon(self):
		'''
		 Returns a dictionary of weapons in accordance with regulations
		:return: dict
		'''
		# pistol - пистолет.
		# bestally_pistol - бествольный пистолет
		pistol = bestally_pistol = self.staff_member

		# Пистолет-пулемет.
		pistol_gun = Abstract.procent(self, self.staff_member, 50)

		# Cигнальный пистолет.
		signal_pistol = (self.count_marching_unit * 1) + (
 			self.count_duty_part * 1)

		# 5,45 мм или 7,62 мм автомат.
		automat = Abstract.procent(self, self.staff_member, 25) + (
			self.count_duty_part * 3)

		# 5,45 мм или 7,62 мм ручной пулемет
		hand_gun = self.count_duty_part * 2

		# 7,62 мм снайперская винтовка
		sniper_rifle = self.count_duty_part * 1

		# 18,5 мм карабин специальный.
		special_carbine = self.count_duty_part * 2

		dic = {'pistol': pistol, 'bestally_pistol': bestally_pistol,
		       'pistol_gun': pistol_gun, 'signal_pistol': signal_pistol,
		       'automat': automat, 'hand_gun': hand_gun,
		       'sniper_rifle': sniper_rifle,
		       'special_carbine': special_carbine}

		return dic

	def ammunition(self):
		'''
		Считате боеприпасы согласно положенности
		:return:
		'''
		dict_weapon = MarchingUnit.weapon(self)

		# пистолетные патроны
		pistol_catridges = (dict_weapon['pistol'] * 24) + (
			dict_weapon['pistol_gun'] * 100)

		# 5,45 и 7,62 мм автоматные патроны
		automat_catridges = (dict_weapon['automat'] * 246) + (
			dict_weapon['hand_gun'] * 750)

		# 5,45 и 7,62 мм автоматные патроны с трассирующе пулей
		automat_catridges_tracer = (dict_weapon['automat'] * 54) + (
			dict_weapon['hand_gun'] * 250)

		# 7,62 мм винтовочные патроны снайперские
		sniper_catridges = dict_weapon['sniper_rifle'] * 100

		# 18,5 мм патроны к специальным карабинам
		special_carbine_catridges = dict_weapon['special_carbine'] * 16

		# signal_catridges - патроны сигнальные 18,5х60С
		# light_catridges - патроны осветительные 18,5х60О
		signal_catridges = light_catridges = dict_weapon['bestally_pistol'] * 4

		# cartridge_lighting - 26 мм патрон осветительный
		# color_catridges - 26 мм патроны красного, зеленого, желтого огня
		cartridge_lighting = color_catridges = (
			dict_weapon['signal_pistol'] * 5)

		# патрон с резиновой пулей
		rubber_bullet = (dict_weapon['special_carbine'] * 250) * (
			dict_weapon['bestally_pistol'] * 48)

		# патрон светозвуковой
		svetozvukovye = dict_weapon['bestally_pistol'] * 24

	# TODO 2: что то должно возвращать


	def traning_weapons(self):
		'''

		:param traning_pistol: int
		:param pistol_gun_traning: itn
		:param automat_traning: int
		:return:
		'''
		# traning_pistol - пистолет учебный
		# pistol_gun_traning - пистолет-пулемет учебный
		# automat_traning - 5,45 (7,62) мм автомат учебный
		traning_pistol = pistol_gun_traning = automat_traning = self.count_marching_unit * 1
		# TODO 3: что возвращать
		return traning_pistol, pistol_gun_traning, automat_traning

	def optical_equipment(self):
		'''
		Считает оптические приборы согласно положенности
		:return:
		'''
		# Бинокль с увеличением 8 крат
		binoculars = (self.count_duty_part * 3) + (self.count_duty_part * 1)

		# Зрительная труба
		spotting = self.count_marching_unit * 2

	# TODO: что то должана возвращать


	def military_chemical(self):
		# Общевойсковой фильтрирующий противогаз (гражданский противогаз)

		# TODO : надо подумать по поводу гражданиских
		mask = Abstract.procent(self, (self.staff_member + self.civil_memeber),
		                        110)

		# Дополнительный патрон аналогичный ДПГ-3
		additional_cartridge = Abstract.procent(self, (
			self.staff_member + self.civil_memeber), 50)

		# Респиратор
		respirator = Abstract.procent(self, (
			self.staff_member + self.civil_memeber), 10)

		# Утеплительные манжеты (НМУ)
		guffs = mask * 2

		# Общевойсковой защитный комлект
		ozk = self.staff_member + self.civil_memeber

		# Легкий защитный костюм Л-1
		light_protective_suit = self.count_platoon * 5

		# power_meter_1 - измеритель мощности дозы ИМД-21С
		# power_meter_2 - измеритель мощности дозы ИМД-2НМ
		power_meter_1 = power_meter_2 = self.count_marching_unit * 1

		# Общевойсковой комплект измерителей дозы, аналогичный ИД-1
		meter_dose = round((self.staff_member + self.civil_memeber) / 30)

		# Прибор химической разведки войсковой, аналогичный ВПХР
		device_chemical = (self.count_marching_unit * 1) + (
			self.count_patrol * 1)

		# Комплект контрольный трубок (ККТ-2)
		control_tube = round(device_chemical / 5)

		if control_tube == 0:
			control_tube = 1

		# Индивидуальный противохимический пакет (ИПП)
		individual_package = self.staff_member

		# sanitary - комплект санитарной обработки (КСО)
		# repair_box - ремонтный ящик средств защиты (РЯ-СЗ)
		sanitary = repair_box = self.count_marching_unit * 1




if __name__ == '__main__':
	battalion = MarchingUnit(140, 5)
	print(battalion.weapon())
	battalion.ammunition()
	print(battalion.traning_weapons())
	battalion.military_chemical()
