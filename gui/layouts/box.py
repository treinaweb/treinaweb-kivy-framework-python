from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget


class TelaApp(BoxLayout):
    pass

class Box(App):
    def build(self):
        return TelaApp()

Box().run()