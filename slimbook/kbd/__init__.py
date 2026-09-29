import ctypes
import ctypes.util
from ctypes import c_char_p, c_int, c_uint, byref

_libslimbook = ctypes.CDLL("libslimbook.so.1")

PROPERTY_EFFECT     = 0x01
PROPERTY_BRIGHTNESS = 0x02
PROPERTY_COLOR      = 0x03
PROPERTY_DIRECTION  = 0x04
PROPERTY_SPEED      = 0x05
PROPERTY_REACTIVE   = 0x06
PROPERTY_SAVE       = 0x09
PROPERTY_EOF        = 0xFF

EFFECT_NONE      = 0x00
EFFECT_BREATHING = 0x02
EFFECT_WAVE      = 0x03
EFFECT_RANDOM    = 0x04
EFFECT_RAINBOW   = 0x05
EFFECT_RIPPLE    = 0x06
EFFECT_MARQUEE   = 0x09
EFFECT_RAINDROP  = 0x0A
EFFECT_AURORA    = 0x0E
EFFECT_FIREWORKS = 0x11
EFFECT_SOLID     = 0x33

COLOR_NONE   = 0x00
COLOR_RED    = 0x01
COLOR_ORANGE = 0x02
COLOR_YELLOW = 0x03
COLOR_GREEN  = 0x04
COLOR_BLUE   = 0x05
COLOR_TEAL   = 0x06
COLOR_PURPLE = 0x07
COLOR_RANDOM = 0x08

BRIGHTNESS_CURRENT = 0x00
BRIGHTNESS_ZERO    = 0x01
BRIGHTNESS_FULL    = 0x02

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

def effect_set(model,effect,properties):
    _libslimbook.slb_kbd_effect_set.argtypes = [c_uint, c_uint, ctypes.POINTER(c_uint)]
    data =(c_uint * len(properties))(*properties)
    _libslimbook.slb_kbd_effect_set(model,effect,data)
