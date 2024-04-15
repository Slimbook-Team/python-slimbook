import ctypes
import ctypes.util

_libslimbook = ctypes.CDLL("libslimbook.so.1")

MAX_PROCESSOR_VERSION = 48

class Processor(ctypes.Structure):
    _fields_ = [("cores", ctypes.c_ubyte),
                ("version", ctypes.c_char * MAX_PROCESSOR_VERSION)]

class MemoryDevice(ctypes.Structure):
    _fields_ = [("size", ctypes.c_ulong),
                ("speed", ctypes.c_uint),
                ("type", ctypes.c_ubyte)]

class Data(ctypes.Union):
    _fields_ = [("memory_device",MemoryDevice),
                ("processor",Processor)]

class Entry(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ubyte),
                 ("length", ctypes.c_ubyte),
                 ("handle",ctypes.c_ushort),
                 ("data",Data)]

def get():
    count = ctypes.c_uint()
    entries = ctypes.POINTER(Entry)()
    _libslimbook.slb_smbios_get.restype.argtypes = ctypes.POINTER(ctypes.POINTER(Entry)), ctypes.POINTER(ctypes.c_uint)
    _libslimbook.slb_smbios_get.restype = ctypes.c_int
    
    status = _libslimbook.slb_smbios_get(ctypes.byref(entries),ctypes.byref(count))
    
    tmp=[]
    
    if (status == 0):
        for n in range(count.value):
            entry = entries[n]
            tmp.append(entry)
    
        _libslimbook.slb_smbios_free.restype.argtypes = ctypes.POINTER(Entry)
        _libslimbook.slb_smbios_free.restype = ctypes.c_int
        _libslimbook.slb_smbios_free(entries)
    
    return tmp 

