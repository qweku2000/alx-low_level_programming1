import ctypes

# Load the shared library
dynamic_lib = ctypes.CDLL('./libdynamic.so')

# Define the prototypes for the C functions
dynamic_lib._putchar.restype = ctypes.c_int
dynamic_lib._putchar.argtypes = [ctypes.c_char]

dynamic_lib._islower.restype = ctypes.c_int
dynamic_lib._islower.argtypes = [ctypes.c_int]

dynamic_lib._isalpha.restype = ctypes.c_int
dynamic_lib._isalpha.argtypes = [ctypes.c_int]

dynamic_lib._abs.restype = ctypes.c_int
dynamic_lib._abs.argtypes = [ctypes.c_int]

dynamic_lib._isupper.restype = ctypes.c_int
dynamic_lib._isupper.argtypes = [ctypes.c_int]

dynamic_lib._isdigit.restype = ctypes.c_int
dynamic_lib._isdigit.argtypes = [ctypes.c_int]

dynamic_lib._strlen.restype = ctypes.c_int
dynamic_lib._strlen.argtypes = [ctypes.c_char_p]

dynamic_lib._puts.restype = None
dynamic_lib._puts.argtypes = [ctypes.c_char_p]

dynamic_lib._strcpy.restype = ctypes.c_char_p
dynamic_lib._strcpy.argtypes = [ctypes.c_char_p, ctypes.c_char_p]


dynamic_lib._strcmp.restype = ctypes.c_int
dynamic_lib._strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

dynamic_lib._memset.restype = ctypes.c_char_p
dynamic_lib._memset.argtypes = [ctypes.c_char_p, ctypes.c_char, ctypes.c_uint]

dynamic_lib._memcpy.restype = ctypes.c_char_p
dynamic_lib._memcpy.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]

dynamic_lib._strchr.restype = ctypes.c_char_p
dynamic_lib._strchr.argtypes = [ctypes.c_char_p, ctypes.c_char]

dynamic_lib._strspn.restype = ctypes.c_uint
dynamic_lib._strspn.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

dynamic_lib._strpbrk.restype = ctypes.c_char_p
dynamic_lib._strpbrk.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

dynamic_lib._strstr.restype = ctypes.c_char_p
dynamic_lib._strstr.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

def putchar(c):
    return dynamic_lib._putchar(c)

def islower(c):
    return dynamic_lib._islower(c)

def isalpha(c):
    return dynamic_lib._isalpha(c)

def abs(n):
    return dynamic_lib._abs(n)

def isupper(c):
    return dynamic_lib._isupper(c)

def isdigit(c):
    return dynamic_lib._isdigit(c)

def strlen(s):
    return dynamic_lib._strlen(s.encode('utf-8'))

def puts(s):
    dynamic_lib._puts(s.encode('utf-8'))

def strcpy(dest, src):
    return dynamic_lib._strcpy(dest.encode('utf-8'), src.encode('utf-8'))

# ... and so on for other functions
def strcat(dest, src):
    return dynamic_lib._strcat(dest.encode('utf-8'), src.encode('utf-8'))

def strncat(dest, src, n):
    return dynamic_lib._strncat(dest.encode('utf-8'), src.encode('utf-8'), n)

def strncpy(dest, src, n):
    return dynamic_lib._strncpy(dest.encode('utf-8'), src.encode('utf-8'), n)

def strcmp(s1, s2):
    return dynamic_lib._strcmp(s1.encode('utf-8'), s2.encode('utf-8'))

def memset(s, b, n):
    return dynamic_lib._memset(s.encode('utf-8'), b, n)

def memcpy(dest, src, n):
    return dynamic_lib._memcpy(dest.encode('utf-8'), src.encode('utf-8'), n)

def strchr(s, c):
    return dynamic_lib._strchr(s.encode('utf-8'), c.encode('utf-8'))

def strspn(s, accept):
    return dynamic_lib._strspn(s.encode('utf-8'), accept.encode('utf-8'))

def strpbrk(s, accept):
    return dynamic_lib._strpbrk(s.encode('utf-8'), accept.encode('utf-8'))

def strstr(haystack, needle):
    return dynamic_lib._strstr(haystack.encode('utf-8'), needle.encode('utf-8'))
