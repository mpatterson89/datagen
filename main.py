import kivy
kivy.require('1.0.7')
import sys
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.layout import Layout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.lang import Builder
import socket
import subprocess
from kivy.uix.screenmanager import ScreenManager, Screen
from datepicker import DatePicker
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.garden.datetimepicker import DatetimePicker
from kivy.uix.switch import Switch
from kivy.core.window import Window
from kivy.config import Config


class TaskScreen(Screen):
	Builder.load_file('/home/mpatterson/Dev/kivy_stuff/DataGen/taskscreen.kv')

class SettingsScreen(Screen):
    pass

class MainMenu(Screen):
	pass

class StartEndDate(Screen):
	Builder.load_file('/home/mpatterson/Dev/kivy_stuff/DataGen/startenddate.kv')


class DataGenApp(App):
	#Window.fullscreen = True
	#icon = 'destiny.png'
	Config.set('graphics', 'width', '800')
	Config.set('graphics', 'height', '600')
	Config.write()
	def build(self):
		sm = ScreenManager()

		menu = MainMenu(name='menu')
		sed = StartEndDate(name='sed')
		datepicker = DatePicker()
		settingscreen = SettingsScreen(name="settingscreen")
		settingscreen.add_widget(datepicker)
		
		task = TaskScreen(name='task')
		sm.add_widget(menu)
		sm.add_widget(task)
		sm.add_widget(settingscreen)
		sm.add_widget(sed)
		return sm

if __name__ == '__main__':
    DataGenApp().run()