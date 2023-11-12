import ctypes
import ctypes.util
from ctypes import c_char_p, c_int, c_uint

_libslimbook = ctypes.CDLL(ctypes.util.find_library('slimbook'))

def load(model):
    _libslimbook.slb_config_load.restype = c_int
    return _libslimbook.slb_config_load(model)

def store(model):
    _libslimbook.slb_config_store.restype = c_int
    return _libslimbook.slb_config_store(model)
