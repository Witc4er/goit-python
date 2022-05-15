class Meta(type):

    def __new__(cls, name, parrent_class, attr):
        print('Method __new__ called with ', cls)
        print('name :', name)
        print('parrent class:  ', parrent_class)
        attr['class_number'] = Meta.children_number
        Meta.children_number += 1
        print('attr: ', attr)
        print('---------')
        return type.__new__(cls, name, parrent_class, attr)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data



if __name__ == '__main__':
    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    assert (a.class_number, b.class_number) == (0, 1)