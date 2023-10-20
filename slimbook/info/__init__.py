import ctypes
import ctypes.util

_libslimbook = ctypes.CDLL(ctypes.util.find_library('slimbook'))

SLB_MODEL_UNKNOWN =           0x0000

SLB_MODEL_EXECUTIVE =         0x1000
SLB_MODEL_EXECUTIVE_14_11TH = 0x1001
SLB_MODEL_EXECUTIVE_12TH =    0x1002

SLB_MODEL_PROX =              0x2000
SLB_MODEL_PROX_AMD =          0x2001
SLB_MODEL_PROX15_AMD =        0x2002
SLB_MODEL_PROX_AMD5 =         0x2003
SLB_MODEL_PROX15_AMD5 =       0x2004

SLB_MODEL_TITAN =             0x4000

SLB_MODEL_HERO =              0x8000
SLB_MODEL_HERO_RPL_RTX =      0x8001

SLB_MODEL_ESSENTIAL =         0xA000

SLB_PLATFORM_UNKNOWN =        0x0000
SLB_PLATFORM_QC71 =           0x1000
SLB_PLATFORM_CLEVO =          0x2000


def get_model():
    return _libslimbook.slb_info_get_model()

def get_platform():
    return _libslimbook.slb_info_get_platform()
