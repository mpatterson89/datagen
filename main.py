import kivy
kivy.require('1.0.7')
import sys
import socket
import subprocess
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
from taskscreen import TaskScreen
from startenddate import StartEndDate
from mainmenu import MainMenu	
from settingsscreen import SettingsScreen
from taskresultsscreen import TaskResultsScreen

class DataGenApp(App):
	#Window.fullscreen = True
	#icon = 'destiny.png'
	Config.set('graphics', 'width', '800')
	Config.set('graphics', 'height', '600')
	Config.write()
	
	def build(self):
		sm   		  = ScreenManager()
		menu 		  = MainMenu(name='menu')
		sed           = StartEndDate(name='sed')
		settingscreen = SettingsScreen(name="settingscreen")
		task 		  = TaskScreen(name='task')
		task_results  = TaskResultsScreen(name='task_results')

		sm.add_widget(menu)
		sm.add_widget(task)
		sm.add_widget(settingscreen)
		sm.add_widget(sed)
		sm.add_widget(task_results)
		return sm

if __name__ == '__main__':
    DataGenApp().run()