import kivy
kivy.require('1.0.7')
import sys
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.datetimepicker import DatetimePicker

class StartEndDate(Screen):
	Builder.load_file('/home/mpatterson/Dev/kivy_stuff/DataGen/startenddate.kv')

	date_switch = True
	soedate     = [None, None]
	DEBUG		= False

	def set_switch(self, isStartDate):
		self.date_switch = isStartDate

	def apply(self):
		if self.date_switch == True:
			self.soedate[0] = str(self.ids.datepicker.get_datetime())
		else:
			self.soedate[1] = str(self.ids.datepicker.get_datetime())
		
		if self.DEBUG == True:
			print self.soedate[0]
			print self.soedate[1]