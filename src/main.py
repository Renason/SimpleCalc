#!/bin/python

# + ----------------------- +
# |   SimpleCalc            |
# |   2. projekt IVS / 2017 |
# |   @ FIT VUT, BRNO       |
# |                         |
# |   Peter Marko           |
# |   Stanislav Mechl       |
# |   Andrej Nano           |
# + ----------------------- +   

## \mainpage SimpleCalc documentation
# 
# \section intro_sec Introduction
#
# This is the introduction about our project.
#
# \section authors_sec Authors
#  
# Andrej Nano
#
# Peter Marko
#
# Stanislav Mechl
# 

## @package main
#  Documentation for main.
#
#  More details. 

import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


# kivy configs
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 900)
Config.set('graphics', 'width', 600)
Config.set('graphics', 'borderless', 0)
Config.write()

class CalcGridLayout(GridLayout):
    def calculate(self,calculation):
        try:
            self.display.text = str(eval(calculation))
        except Exception:
            self.display.text = 'Error'

class CalculatorApp(App):
    def build(self):
        return CalcGridLayout()

if __name__ == "__main__":
    CalculatorApp().run()

