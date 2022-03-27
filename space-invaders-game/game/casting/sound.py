class Sound:
    def __init__(self, filename, volume=1, repeat=False):
        self._filename = filename
        self._volume = volume
        self._repeat = repeat
        
    def get_filename(self):
        return self._filename
        
    def get_volume(self):
        return self._volume
        
    def is_repeat(self):
        return self._repeat