import os
from cachier import cachier


def cache_was_used():
    sf = './side_effect'
    if os.path.isfile(sf):
        os.remove(sf)

    @cachier(cache_dir='./cache')
    def foo(x):
        with open(sf, 'w') as f:
            f.write('data')
        return True

    foo('test')

    return not os.path.isfile(sf)
