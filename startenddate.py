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