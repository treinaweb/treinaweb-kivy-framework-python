from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

from entidades import cliente
from repositorios import cliente_repositorio



class Principal(BoxLayout):


    def cadastrar_cliente(self):
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        cli = cliente.Cliente(nome, idade)
        cliente_repositorio.ClienteRepositorio.inserir_cliente(cli)
        self.ids.nome.text = ''
        self.ids.idade.text = ''
        self.listar_clientes()



class Crud(App):
    def build(self):
        return Principal()

Crud().run()