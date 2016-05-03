import time

class Timer:
    def __init__(self):
        self.start = time.time()

    def restart(self):
        self.start = time.time()

    def get_time_hhmmss(self):
        end = time.time()
        minutes, seconds = divmod(end - self.start, 60)
        hours, minutes = divmod(minutes, 60)
        time_str = "%02d:%02d:%02d" % (hours, minutes, seconds)
        return time_str

    def get_seconds(self):
        end = time.time()
        seconds = (end - self.start) / 60
        return seconds