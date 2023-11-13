import ctypes
import ctypes.util
from ctypes import c_char_p, c_int, c_uint, byref

_libslimbook = ctypes.CDLL(ctypes.util.find_library('slimbook'))
    
def fn_lock_get():
    value = c_uint()
    _libslimbook.slb_qc71_fn_lock_get.restype = c_uint
    status = _libslimbook.slb_qc71_fn_lock_get(byref(value))
    
    return value

def fn_lock_set(value):
    status = _libslimbook.slb_qc71_fn_lock_set(value)
    
def super_lock_get():
    value = c_uint()
    _libslimbook.slb_qc71_super_lock_get.restype = c_uint
    status = _libslimbook.slb_qc71_super_lock_get(byref(value))
    
    return value

def super_lock_set(value):
        status = _libslimbook.slb_qc71_super_lock_set(value)

def silent_mode_get():
    value = c_uint()
    _libslimbook.slb_qc71_silent_mode_get.restype = c_uint
    status = _libslimbook.slb_qc71_silent_mode_get(byref(value))
    
    return value

def silent_mode_set(value):
        status = _libslimbook.slb_qc71_silent_mode_set(value)
