from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.clock import Clock
import random

class ProcessingScreen(Screen):
    progress = NumericProperty(0)
    total_images = NumericProperty(0)
    processed_images = NumericProperty(0)

    def on_enter(self):
        self.total_images = len(self.manager.get_screen('selection').valid_files)
        self.processed_images = 0
        self.progress = 0

    def start_processing(self):
        Clock.schedule_interval(self.process_image_placeholder, 0.5)

    def process_image_placeholder(self, dt):
        if self.processed_images < self.total_images:
            self.processed_images += 1
            self.progress = (self.processed_images / self.total_images) * 100
            return True
        else:
            self.manager.current = 'analysis'
            return False