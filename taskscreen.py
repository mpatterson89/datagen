import kivy
kivy.require('1.0.7')
import sys
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.layout import Layout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.slider import Slider
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.properties import ObjectProperty


class TaskScreen(Screen):
	Builder.load_file('/home/mpatterson/Dev/kivy_stuff/DataGen/taskscreen.kv')

	state_status 	= []
	type_status  	= []
	priority_status = []
	DEBUG 			= False

	def getStates(self):

		#Group 'type'
		type_evs         	 = self.ids.cb_evs.active
		type_transport   	 = self.ids.cb_transport.active
		type_generic     	 = self.ids.cb_generic.active
		self.type_status 	 = [type_evs, type_transport, type_generic]

		#Group 'state'
		state_complete 		 = self.ids.state_complete.active
		state_started  		 = self.ids.state_started.active
		state_paused   		 = self.ids.state_paused.active
		state_waiting  		 = self.ids.state_waiting.active
		state_canceled 		 = self.ids.state_canceled.active
		self.state_status    = [state_complete, state_started, state_paused, state_waiting, state_canceled]

		#Group 'priority'
		priority_0     		 = self.ids.pr0.active
		priority_1	   		 = self.ids.pr1.active
		self.priority_status = [priority_0, priority_1]

		
		#debug: 
		if self.DEBUG == True:
			print self.state_status
			print self.type_status
			print self.priority_status

	def getType(self):
		pass


	def apply(self):
		print "Apply Submitted"
		self.getStates()
		self.getType()






