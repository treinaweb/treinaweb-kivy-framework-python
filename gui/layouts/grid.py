from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class TelaApp(GridLayout):
    pass

class Grid(App):
    def build(self):
        return TelaApp()

Grid().run()