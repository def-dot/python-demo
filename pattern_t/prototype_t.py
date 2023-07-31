class ProtoTypeT:
    def __init__(self, name='default', **kwargs):
        self.name = name
        self.__dict__.update(kwargs)

    def clone(self, **kwargs):
        new_obj = self.__class__(**self.__dict__)
        new_obj.__dict__.update(kwargs)
        return new_obj


class ProtoTypeDispatch:
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register_object(self, name, obj):
        self._objects[name] = name

    def unregister_object(self, name):
        del self._objects[name]


if __name__ == '__main__':
    o = ProtoTypeT()
    o_2 = o.clone(name='new_obj')
    print(id(o))
    print(id(o_2))
    print('o.__dict__------------')
    print(o.__dict__)
    print('o_2.__dict__------------')
    print(o_2.__dict__)

    dispath = ProtoTypeDispatch()
    dispath.register_object('default', o)
    dispath.register_object('obj1', o_2)
