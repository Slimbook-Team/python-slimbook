import ctypes
import ctypes.util
from ctypes import c_char_p, c_int, c_uint, byref

_libslimbook = ctypes.CDLL("libslimbook.so.1")

def backlight_get(model):
    color = c_uint()
    _libslimbook.slb_kbd_backlight_get.restype = c_int
    status = _libslimbook.slb_kbd_backlight_get(model, byref(color))
    
    return color.value

def backlight_set(model,color):
    _libslimbook.slb_kbd_backlight_set(model,color)
    
def brightness_get(model):
    value = c_uint()
    _libslimbook.slb_kbd_brightness_get.restype = c_int
    status = _libslimbook.slb_kbd_brightness_get(model, byref(value))
    
    return value.value

def brightness_set(model,value):
    _libslimbook.slb_kbd_brightness_set(model,value)
    
def brightness_max(model):
    value = c_uint()
    _libslimbook.slb_kbd_brightness_max.restype = c_int
    status = _libslimbook.slb_kbd_brightness_max(model, byref(value))
    
    return value.value
