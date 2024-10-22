from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
import random

class AnalysisScreen(Screen):
    results = ListProperty([])

    def on_enter(self):
        self.generate_placeholder_results()

    def generate_placeholder_results(self):
        total_images = self.manager.get_screen('processing').total_images
        self.results = [
            {
                'filename': f'image_{i+1}.jpg',
                'fauna_detected': random.choice([True, False]),
                'confidence': random.uniform(0.5, 1.0)
            }
            for i in range(total_images)
        ]

    def show_results(self):
        # En una implementación real, aquí se mostrarían los resultados detallados
        pass