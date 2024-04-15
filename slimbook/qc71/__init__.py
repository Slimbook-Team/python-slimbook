import ctypes
import ctypes.util
from ctypes import c_char_p, c_int, c_uint, byref

_libslimbook = ctypes.CDLL("libslimbook.so.1")
    
def fn_lock_get():
    value = c_uint()
    _libslimbook.slb_qc71_fn_lock_get.restype = c_uint
    status = _libslimbook.slb_qc71_fn_lock_get(byref(value))
    
    return value.value

def fn_lock_set(value):
    status = _libslimbook.slb_qc71_fn_lock_set(value)
    
def super_lock_get():
    value = c_uint()
    _libslimbook.slb_qc71_super_lock_get.restype = c_uint
    status = _libslimbook.slb_qc71_super_lock_get(byref(value))
    
    return value.value

def super_lock_set(value):
        status = _libslimbook.slb_qc71_super_lock_set(value)

def silent_mode_get():
    value = c_uint()
    _libslimbook.slb_qc71_silent_mode_get.restype = c_uint
    status = _libslimbook.slb_qc71_silent_mode_get(byref(value))
    
    return value.value

def silent_mode_set(value):
        status = _libslimbook.slb_qc71_silent_mode_set(value)

def turbo_mode_get():
    value = c_uint()
    _libslimbook.slb_qc71_turbo_mode_get.restype = c_uint
    status = _libslimbook.slb_qc71_turbo_mode_get(byref(value))
    
    return value.value

def turbo_mode_set(value):
        status = _libslimbook.slb_qc71_turbo_mode_set(value)
