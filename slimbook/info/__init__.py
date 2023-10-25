import ctypes
import ctypes.util
from ctypes import c_char_p

_libslimbook = ctypes.CDLL(ctypes.util.find_library('slimbook'))

SLB_MODEL_UNKNOWN =           0x0000

SLB_MODEL_EXECUTIVE =         0x0100
SLB_MODEL_EXECUTIVE_14_11TH = 0x0101
SLB_MODEL_EXECUTIVE_12TH =    0x0102

SLB_MODEL_PROX =              0x0200
SLB_MODEL_PROX_AMD =          0x0201
SLB_MODEL_PROX15_AMD =        0x0202
SLB_MODEL_PROX_AMD5 =         0x0203
SLB_MODEL_PROX15_AMD5 =       0x0204

SLB_MODEL_TITAN =             0x0400

SLB_MODEL_HERO =              0x0800
SLB_MODEL_HERO_RPL_RTX =      0x0801

SLB_MODEL_ESSENTIAL =         0x1000

SLB_PLATFORM_UNKNOWN =        0x0000
SLB_PLATFORM_QC71 =           0x0100
SLB_PLATFORM_CLEVO =          0x0200

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

def get_platform():
    return _libslimbook.slb_info_get_platform()

def is_module_loaded():
    return (_libslimbook.slb_info_is_module_loaded() != 0 )
