from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty

class ProcessingScreen(Screen):
    progress = NumericProperty(0)

    def start_processing(self):
        # Implementar la lógica para iniciar el procesamiento de imágenes
        pass