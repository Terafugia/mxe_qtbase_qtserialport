import sys
import gdb

# Update module path.
dir_ = '/home/user/mxe/usr/i686-w64-mingw32.static/share/glib-2.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from gobject_gdb import register
register (gdb.current_objfile ())
