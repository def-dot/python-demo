import time
from weakref import finalize



class T:
    def __init__(self) -> None:
        finalize(self, self.__finalize)

    def __finalize(self) -> None:
        print("T finalized")



t = T()
print("t created")


del t

time.sleep(2)
