from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class SelectionScreen(Screen):
    selected_folder = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_dropfile=self.on_folder_drop)  # Enlazar el evento de arrastrar carpeta

    def on_folder_drop(self, window, file_path):
        self.selected_folder = str(file_path.decode('utf-8'))
        print('La carpeta seleccionada es: ', self.selected_folder)

    def select_folder(self):
        # Lógica para abrir un selector de archivos o manejar la selección de carpeta
        print('Selección de carpeta activada.')
