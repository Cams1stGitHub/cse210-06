from pydoc import ispackage
import pyray
import pathlib 

class AudioService:
    def __init__(self):
        self._sounds = {}
        
    def initialize(self):
        pyray.init_audio_device()
        
    def play_sound(self, sound):
        filepath = sound.get_filename()
        filepath = str(pathlib.Path(filepath))
        soundl = pyray.load_sound(filepath)
        self._sounds[filepath] = soundl
        pyray.set_sound_volume(self._sounds[filepath], sound.get_volume())
        pyray.play_sound(self._sounds[filepath])
        
    
        
    def release(self):
        pyray.close_audio_device()
        
    def is_sound_playing(self,sound):
        filepath = sound.get_filename()
        filepath = str(pathlib.Path(filepath))
        sound = self._sounds[filepath]
        isPlaying = pyray.is_sound_playing(self._sounds[filepath])
        return isPlaying