import ctypes
import ctypes.util
from ctypes import c_char_p, c_int, c_uint, byref

_libslimbook = ctypes.CDLL(ctypes.util.find_library('slimbook'))

def backlight_get(model):
    color = c_uint()
    _libslimbook.slb_config_load.restype = c_int
    status = _libslimbook.slb_kbd_backlight_get(model, byref(color))
    
    return color

def backlight_set(model,color):
    _libslimbook.slb_kbd_backlight_set.restype = c_int
    _libslimbook.slb_kbd_backlight_set(model,color)
