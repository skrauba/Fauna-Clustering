from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
import os

class SelectionScreen(Screen):
    selected_folder = StringProperty('')
    valid_files = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Inicialización del filemanager
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=False,
        )
        # Inicialización del drag and drop
        Window.bind(on_dropfile=self.on_folder_drop)

    def on_folder_drop(self, window, file_path):
        self.selected_folder = str(file_path.decode('utf-8'))
        if os.path.isdir(self.selected_folder):
            print('La carpeta seleccionada es: ', self.selected_folder)
            self.list_valid_files()
        else:
            toast(f"Debe seleccionar una carpeta válida...")

    def select_folder(self):
        self.file_manager.show('/')

    def select_path(self, path):
        self.selected_folder = path
        self.exit_manager()
        if os.path.isdir(self.selected_folder):
            toast(f"Carpeta seleccionada: {path}")
            self.list_valid_files()
        else:
            toast(f"Debe seleccionar una carpeta válida...")

    def exit_manager(self, *args):
        self.file_manager.close()

    def list_valid_files(self):
        valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        self.valid_files = [
            f for f in os.listdir(self.selected_folder)
            if f.lower().endswith(valid_extensions)
        ]
        toast(f"Se encontraron {len(self.valid_files)} imágenes válidas")
        # Lógica para abrir un selector de archivos o manejar la selección de carpeta
        print('Selección de carpeta activada.')
