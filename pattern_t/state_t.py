
def force_t():
    class Radio:
        def __init__(self):
            self.name = "My Radio"
            self.ams = ["1250", "1380", "1510"]
            self.fms = ["81.3", "89.1", "103.9"]
            self.state = 'am'
            self.am_index = 0
            self.fm_index = 0
            print(f"__init__ state {self.state} {self.value}")

        @property
        def value(self):
            if self.state == 'am':
                return self.ams[self.am_index]
            else:
                return self.fms[self.fm_index]

        def toggle(self):
            self.state = 'fm' if self.state == 'am' else 'am'
            print(f"toggle {self.state} {self.value}")

        def scan(self):
            if self.state == 'am':
                if self.am_index == len(self.ams) - 1:
                    self.am_index = 0
                else:
                    self.am_index += 1
                print(f"scan {self.state} {self.value}")
            else:
                if self.fm_index == len(self.fms) - 1:
                    self.fm_index = 0
                else:
                    self.fm_index += 1
                print(f"scan {self.state} {self.value}")

    r = Radio()
    r.toggle()
    r.scan()

    r.toggle()
    r.scan()

    r.toggle()
    r.scan()


def optimize_t():
    class State:
        def scan(self):
            if self.pos == len(self.stations) - 1:
                self.pos = 0
            else:
                self.pos += 1

        @property
        def val(self):
            return self.stations[self.pos]

    class AmState(State):
        def __init__(self, radio):
            self.radio = radio
            self.name = 'AM'
            self.stations = ["1250", "1380", "1510"]
            self.pos = 0

        def toggle(self):
            self.radio.state = self.radio.fmstate

    class FmState(State):
        def __init__(self, radio):
            self.radio = radio
            self.name = 'FM'
            self.stations = ["81.3", "89.1", "103.9"]
            self.pos = 0

        def toggle(self):
            self.radio.state = self.radio.amstate

    class Radio:
        def __init__(self):
            self.amstate = AmState(self)
            self.fmstate = FmState(self)
            self.state = self.amstate

        def toggle(self):
            self.state.toggle()

        def scan(self):
            self.state.scan()

    r = Radio()
    print(f"state {r.state.name} {r.state.val}")

    r.scan()
    print(f"state {r.state.name} {r.state.val}")

    r.toggle()
    print(f"state {r.state.name} {r.state.val}")

    r.toggle()
    print(f"state {r.state.name} {r.state.val}")


if __name__ == '__main__':
    # force_t()
    optimize_t()
