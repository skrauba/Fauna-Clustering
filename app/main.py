from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

# Importar las clases de los screens
from logic.selection_screen import SelectionScreen
from logic.config_screen import ConfigScreen
from logic.processing_screen import ProcessingScreen
from logic.analysis_screen import AnalysisScreen
from logic.postprocessing_screen import PostprocessingScreen

class FaunaDetectionApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"

        # Cargar los archivos .kv
        Builder.load_file('screens/selection_screen.kv')
        Builder.load_file('screens/config_screen.kv')
        Builder.load_file('screens/processing_screen.kv')
        Builder.load_file('screens/analysis_screen.kv')
        Builder.load_file('screens/postprocessing_screen.kv')

        # Crear el administrador de pantallas
        sm = ScreenManager()
        sm.add_widget(SelectionScreen(name='selection'))
        sm.add_widget(ConfigScreen(name='config'))
        sm.add_widget(ProcessingScreen(name='processing'))
        sm.add_widget(AnalysisScreen(name='analysis'))
        sm.add_widget(PostprocessingScreen(name='postprocessing'))

        return sm

if __name__ == '__main__':
    FaunaDetectionApp().run()