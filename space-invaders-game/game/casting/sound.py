class Sound:
    """create qualities of audio
    
    The responsibility of Sound is to get the filename, choose the audio level and
    repeat it until it needs to stop"""
    def __init__(self, filename, volume=1, repeat=False):
        """constructs a new sound using the specified filename, volume, and whether
        repeat is false or true

        Args:
            filename(): gets the name of the file
            volume(sound): sets volume of sound
            repeat(sound): sets if sound should repeat"""
        self._filename = filename
        self._volume = volume
        self._repeat = repeat
        
    def get_filename(self):
        """gets the audio filename"""
        return self._filename
        
    def get_volume(self):
        """get volume for Audio"""
        return self._volume
        
    def is_repeat(self):
        """repeats audio"""
        return self._repeat