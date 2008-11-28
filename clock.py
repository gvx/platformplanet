#Substitute Clock For PyGame
#Copyright (C) 2005  Adam Bark apb_4@users.sourceforge.net
#Licence: GPL
from time import sleep, time
class ABClock:
    def __init__(self):
        self.t = time()
    def tick(self, rate=-1):
        self.rate = rate
        self._stop()
        retVal = int(round((time() - self.t) * 1000, 0))
        self.t = time()
        return retVal
    def _stop(self):
        try:
            sleep_time = 1.0/self.rate - (time() - self.t)
            if sleep_time > 0:
               sleep(sleep_time)
        except IOError:
            pass
