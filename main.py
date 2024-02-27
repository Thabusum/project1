from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
SoundLoader.load('dandalayya.mp3')
class MyApp(App):
    def build(self):
        self.sound = SoundLoader.load('dandalayya.mp3')
        return Builder.load_file('myapp.kv')

    def toggle_sound(self):
        if self.sound.state == 'stop':  # If the sound is not playing
            self.sound.play()  # Start playing the sound
            self.root.ids.play_button.text = 'On'  # Update the button text to "On"
        else:  # If the sound is playing
            self.sound.stop()  # Stop playing the sound
            self.root.ids.play_button.text = 'Off'  # Update the button text to "Off"


if __name__ == '__main__':
    MyApp().run()