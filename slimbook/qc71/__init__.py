import ctypes
import ctypes.util
from ctypes import c_char_p, c_int, c_uint, byref

_libslimbook = ctypes.CDLL("libslimbook.so.1")
    
def manual_control_get():
    value = c_uint()
    _libslimbook.slb_qc71_manual_control_get.restype = c_uint
    status = _libslimbook.slb_qc71_manual_control_get(byref(value))
    
    return value.value

def manual_control_set(value):
    status = _libslimbook.slb_qc71_manual_control_set(value)

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

def profile_get():
    value = c_uint()
    _libslimbook.slb_qc71_profile_get.restype = c_uint
    status = _libslimbook.slb_qc71_profile_get(byref(value))

    return value.value

def profile_set(value):
    status = _libslimbook.slb_qc71_profile_set(value)

def custom_tdp_get():
    pl1 = c_uint()
    pl2 = c_uint()
    pl4 = c_uint()
    
    _libslimbook.slb_qc71_custom_tdp_get.restype = c_uint
    status = _libslimbook.slb_qc71_custom_tdp_get(byref(pl1),byref(pl2),byref(pl4))

    return (pl1.value, pl2.value, pl4.value)

def custom_tdp_set(pl1,pl2,pl4):
    status = _libslimbook.slb_qc71_custom_tdp_set(pl1,pl2,pl4)
