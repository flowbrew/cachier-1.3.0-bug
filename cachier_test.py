import os
from cachier import cachier


def test():
    sf = './side_effect'
    if os.path.isfile(sf):
        os.remove(sf)

    @cachier(cache_dir='./cache')
    def foo(x):
        with open(sf, 'w') as f:
            f.write('data')
        return True

    foo('test')

    return os.path.isfile(sf)
