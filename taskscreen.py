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

	#GUI ELEMENT STATES
	state_status 		= []
	type_status  		= []
	priority_status	 	= []
	slider_status		= []
	users_list			= []
	date_status			= []
	random_state_switch = False
	DEBUG 				= False

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

		#Group 'Sliders'
		task_amount 		 = self.ids.task_amount.value
		duration_min		 = self.ids.sMin.value
		duration_max		 = self.ids.sMax.value
		self.slider_status 	 = [task_amount, duration_min, duration_max]

		#Group users
		users 				 = self.ids.users.text
		self.users_list 	 = users.split(',')

		#Group 'Random State'
		self.random_state_switch  = self.ids.random_state_switch.active
		
		#Group 'Dates'
		self.date_status = self.manager.get_screen('sed').soedate
		if self.date_status[0] == None:
			self.date_status[0] = "ERROR: Must select start date."
		if self.date_status[1] == None:
			self.date_status[1] = "ERROR: Must select end date."

		#debug: 
		if self.DEBUG == True:
			print self.state_status
			print self.type_status
			print self.priority_status
			print self.slider_status
			print self.users_list
			print self.random_state_switch
			print self.date_status

	def isStartDate(self):
		self.manager.get_screen('sed').set_switch(True)

	def isEndDate(self):
		self.manager.get_screen('sed').set_switch(False)

	def setResults(self):

		#Set 'States'
		state_results = "State: ["
		if self.random_state_switch == True:
			state_results = state_results + " Random states "
		elif self.state_status[0] == True:
			state_results = state_results + " Complete "
		elif self.state_status[1] == True:
			state_results = state_results + " Started "
		elif self.state_status[2] == True:
			state_results = state_results + " Paused "
		elif self.state_status[3] == True:
			state_results = state_results + " Waiting "
		elif self.state_status[4] == True:
			state_results = state_results + " Canceled "
		else:
			state_results = state_results + " ERROR: Need to select state "
		state_results = state_results + ']' 
		self.manager.get_screen('task_results').ids.state_status.text = state_results

		#Set 'Type'
		type_result = "Task Type: ["
		if self.type_status[0] == True:
			type_result = type_result + " EVS "
		elif self.type_status[1] == True:
			type_result = type_result + " Transport "
		elif self.type_status[2] == True:
			type_result = type_result + " Generic "
		else:
			type_result = type_result + " ERROR: Need to select type " 
		type_result = type_result + "]"
		self.manager.get_screen('task_results').ids.type_status.text  = type_result
		
		#Set 'Sliders(task_amount, min_duration, max_duration)'
		self.manager.get_screen('task_results').ids.task_amount.text  = "Task Amount: "      +str(self.slider_status[0]).split('.')[0]
		self.manager.get_screen('task_results').ids.min_duration.text = "Min Task Duration: "+str(self.slider_status[1]).split('.')[0]
		self.manager.get_screen('task_results').ids.max_duration.text = "Max Task Duration: "+str(self.slider_status[2]).split('.')[0]

		#Set 'Dates'
		self.manager.get_screen('task_results').ids.start_date.text   = "Start Date: " +self.date_status[0]
		self.manager.get_screen('task_results').ids.end_date.text     = "End Date: "   +self.date_status[1]
	
		#Set 'Priorities'
		hasPrioritySet = False
		priority_results = "Priorities: ["
		if self.priority_status[0] == True:
			priority_results = priority_results + " 0:Without Priority "
			hasPrioritySet = True
		if self.priority_status[1] == True:
			priority_results = priority_results + " 1: With Priority "
			hasPrioritySet = True
		if hasPrioritySet == False:
			priority_results = priority_results + "ERROR: Need to select at least 1 priority"
		priority_results = priority_results + "]"
		self.manager.get_screen('task_results').ids.priorities.text = priority_results

		#Set 'Users'
		users_list = "Users: "
		if len(self.users_list) > 0:
			users_list = users_list + self.users_list[0]
			for i in range(1,len(self.users_list)):
				users_list = users_list + " " + self.users_list[i]
		else:
			users_list = "ERROR: There must be at least 1 user" 
		self.manager.get_screen('task_results').ids.users.text = users_list


	def apply(self):
		if self.DEBUG == True:
			print "Apply Submitted"
		
		self.getStates()
		self.setResults()
		





