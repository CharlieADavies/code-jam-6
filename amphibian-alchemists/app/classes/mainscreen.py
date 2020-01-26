from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.music = SoundLoader.load("misc/SneakySnooper.mp3")
        self.music.loop = True
        self.start_menu_music()

    def start_menu_music(self):
        self.music.play()

    def stop_menu_music(self):
        self.music.stop()
