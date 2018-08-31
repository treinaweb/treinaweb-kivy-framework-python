from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Principal(Widget):
    pass

class Secundario(Widget):
    pass

class Teste(App):
    def build(self):
        return Secundario()

Teste().run()