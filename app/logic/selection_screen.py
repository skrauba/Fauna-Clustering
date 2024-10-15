from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class SelectionScreen(Screen):
    selected_folder = StringProperty('')

    def select_folder(self):
        # Implementar la lógica para seleccionar una carpeta
        pass