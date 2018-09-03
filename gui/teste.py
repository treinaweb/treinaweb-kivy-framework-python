from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class Principal(BoxLayout):
    def teste(self):
        print("O método foi chamado")

class Secundario(Widget):
    pass

class Teste(App):
    def build(self):
        return Principal()

Teste().run()