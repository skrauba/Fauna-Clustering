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
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=False,
        )

    def select_folder(self):
        self.file_manager.show('/')

    def select_path(self, path):
        self.selected_folder = path
        self.exit_manager()
        toast(f"Carpeta seleccionada: {path}")
        self.list_valid_files()

    def exit_manager(self, *args):
        self.file_manager.close()

    def list_valid_files(self):
        valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        self.valid_files = [
            f for f in os.listdir(self.selected_folder)
            if f.lower().endswith(valid_extensions)
        ]
        toast(f"Se encontraron {len(self.valid_files)} imágenes válidas")