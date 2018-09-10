from kivy.app import App
from kivy.properties import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton

from entidades import cliente
from repositorios import cliente_repositorio

class ExclusaoPopup(Popup):
    pass

class BotaoListagem(ToggleButton):
    def __init__(self, cliente_id, cliente_nome, cliente_idade, **kwargs):
        super(BotaoListagem, self).__init__(**kwargs)
        self.id_cliente = cliente_id
        self.nome_cliente = cliente_nome
        self.idade_cliente = cliente_idade
        self.text = self.nome_cliente + " " + self.idade_cliente
        self.group = 'clientes'

    def _do_release(self, *args):
        Principal().cliente_selecionado(self.id_cliente)

class Principal(BoxLayout):
    id_cliente = 0

    def __init__(self, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.listar_clientes()

    def cliente_selecionado(self, id):
        Principal.id_cliente = id
        #print(id)

    def remover_cliente(self):
        id = Principal.id_cliente
        popup = ExclusaoPopup()
        popup.funcao = partial(self.remover, id)
        popup.open()

    def remover(self, id):
        cliente_repositorio.ClienteRepositorio.remover_cliente(id)
        self.listar_clientes()

    def editar_cliente(self):
        id = Principal.id_cliente

        nome = self.ids.nome.text
        idade = self.ids.idade.text
        cli = cliente.Cliente(nome, idade)

        cliente_repositorio.ClienteRepositorio.editar_cliente(id, cli)
        self.listar_clientes()

    def cadastrar_cliente(self):
        nome = self.ids.nome.text
        idade = self.ids.idade.text

        cli = cliente.Cliente(nome, idade)
        cliente_repositorio.ClienteRepositorio.inserir_cliente(cli)
        self.ids.nome.text = ''
        self.ids.idade.text = ''
        self.listar_clientes()

    def listar_clientes(self):
        self.ids.clientes.clear_widgets()
        clientes = cliente_repositorio.ClienteRepositorio.listar_clientes()
        for i in clientes:
            id = str(i[0])
            nome = i[1]
            idade = str(i[2])
            self.ids.clientes.add_widget(BotaoListagem(id, nome, idade))


class Crud(App):
    def build(self):
        return Principal()

Crud().run()