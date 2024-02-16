import ctypes
import ctypes.util
from ctypes import c_char_p, c_uint, c_ulonglong

_libslimbook = ctypes.CDLL(ctypes.util.find_library('slimbook'))

SLB_FAMILY_MASK =                 0xffffff00

SLB_MODEL_UNKNOWN =               0x0000

SLB_MODEL_EXECUTIVE =             0x0100
SLB_MODEL_EXECUTIVE_14_11TH =     0x0101
SLB_MODEL_EXECUTIVE_12TH =        0x0102

SLB_MODEL_PROX =                  0x0200
SLB_MODEL_PROX_AMD =              0x0201
SLB_MODEL_PROX15_AMD =            0x0202
SLB_MODEL_PROX_AMD5 =             0x0203
SLB_MODEL_PROX15_AMD5 =           0x0204

SLB_MODEL_TITAN =                 0x0400

SLB_MODEL_HERO =                  0x0800
SLB_MODEL_HERO_RPL_RTX =          0x0801
SLB_MODEL_HERO_S_TGL_RTX =        0x0802

SLB_MODEL_ESSENTIAL =             0x1000
SLB_MODEL_ESSENTIAL_SLIMBOOK =    0x1001
SLB_MODEL_ESSENTIAL_ESSENTIAL =   0x1002
SLB_MODEL_ESSENTIAL_15L =         0x1003
SLB_MODEL_ESSENTIAL_15_AMD_5000 = 0x1004
SLB_MODEL_ESSENTIAL_15_11 =       0x1005

SLB_MODEL_ELEMENTAL =             0x2000
SLB_MODEL_ELEMENTAL_15_I12 =      0x2001
SLB_MODEL_ELEMENTAL_14_I12 =      0x2002

SLB_MODEL_EXCALIBUR =             0x4000
SLB_MODEL_EXCALIBUR_14_AMD7 =     0x4001
SLB_MODEL_EXCALIBUR_16_AMD7 =     0x4002

SLB_PLATFORM_UNKNOWN =            0x0000
SLB_PLATFORM_QC71 =               0x0100
SLB_PLATFORM_CLEVO =              0x0200
SLB_PLATFORM_Z16 =                0x0400

SLB_SCAN_QC71_SUPER_LOCK =        0x68
SLB_SCAN_QC71_SILENT_MODE =       0x69
SLB_SCAN_QC71_TOUCHPAD_SWITCH =   0x76
SLB_SCAN_Z16_SILENT_MODE =        0xf2
SLB_SCAN_Z16_NORMAL_MODE =        0xf9
SLB_SCAN_Z16_PERFORMANCE_MODE =   0xe2

def product_name():
    _libslimbook.slb_info_product_name.restype = c_char_p
    return _libslimbook.slb_info_product_name().decode("utf-8")

def board_vendor():
    _libslimbook.slb_info_board_vendor.restype = c_char_p
    return _libslimbook.slb_info_board_vendor().decode("utf-8")

def product_serial():
    _libslimbook.slb_info_product_serial.restype = c_char_p
    return _libslimbook.slb_info_product_serial().decode("utf-8")

def bios_version():
    _libslimbook.slb_info_bios_version.restype = c_char_p
    return _libslimbook.slb_info_bios_version().decode("utf-8")

def ec_firmware_release():
    _libslimbook.slb_info_ec_firmware_release.restype = c_char_p
    return _libslimbook.slb_info_ec_firmware_release().decode("utf-8")

def get_model():
    return _libslimbook.slb_info_get_model()

def get_family():
    return _libslimbook.slb_info_get_family()

def get_platform():
    return _libslimbook.slb_info_get_platform()

def is_module_loaded():
    return (_libslimbook.slb_info_is_module_loaded() != 0 )

def keyboard_device():
    return _libslimbook.slb_info_keyboard_device()

def module_device():
    return _libslimbook.slb_info_module_device()

def touchpad_device():
    return _libslimbook.slb_info_touchpad_device()

def uptime():
    return _libslimbook.slb_info_uptime()

def kernel():
    _libslimbook.slb_info_kernel.restype = c_char_p
    return _libslimbook.slb_info_kernel().decode("utf-8")
    
def cmdline():
    _libslimbook.slb_info_cmdline.restype = c_char_p
    return _libslimbook.slb_info_cmdline().decode("utf-8")

def total_memory():
    _libslimbook.slb_info_total_memory.restype = c_ulonglong
    return _libslimbook.slb_info_total_memory()
    
def available_memory():
    _libslimbook.slb_info_available_memory.restype = c_ulonglong
    return _libslimbook.slb_info_available_memory()
