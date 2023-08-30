import sys


def sys_t():
    print(dir(sys))
    dir_sys = ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__',
         '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache',
         '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git',
         '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook',
         'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info',
         'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks',
         'get_coroutine_origin_tracking_depth', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors',
         'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof',
         'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern',
         'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache',
         'platform', 'platlibdir', 'prefix', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setprofile',
         'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'unraisablehook',
         'version', 'version_info', 'warnoptions', 'winver']
    print(f"__name__ {sys.__name__}")
    # print(f"copyright {sys.copyright}")
    print(f"version {sys.version}")
    print(f"version_info {sys.version_info}")
    print(f"path {sys.path}")  # 模块搜索路径，包括解释器当前路径；解释器根目录；解释器DLLS目录；解释器Lib目录；虚拟环境根目录；虚拟环境Lib/site-packages目录（当使用虚拟环境时，不搜索解释器site-packages目录）。sys.path[0]为解释器当前执行路径。
    print(f"argv {sys.argv}")  # 获取解释器执行参数
    ls = range(sys.maxsize)  # sys.maxsize 只是限制了list和str的长度（len()），不是整数的最大值。python3中整数没有最大值（可以无限大，和存储方式有关）
    print(len(ls))
    ls = range(sys.maxsize + 1)
    # print(len(ls)) # error
    print(f"builtin_module_names {sys.builtin_module_names}")  # 初始化加载的内置模块(built-in)，windows时包含nt，linux时包含posix
    # print(f"modules {sys.modules}")  # 初始加载的module
    print(f"getdefaultencoding {sys.getdefaultencoding()}")  # utf-8
    print(f"getfilesystemencoding {sys.getfilesystemencoding()}")  # utf-8
    print(f"getfilesystemencodeerrors {sys.getfilesystemencodeerrors()}")  # surrogatepass
    print(f"getprofile {sys.getprofile()}")  # utf-8


if __name__ == "__main__":
    sys_t()
