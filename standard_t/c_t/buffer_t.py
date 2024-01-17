import ctypes

lib = ctypes.cdll.LoadLibrary("so_t.so")
buffer = ctypes.create_string_buffer(64)  # 创建一个64字节的缓冲区
buffer.value = b"hello world"
length = lib.get_string_len(buffer)
print("length", length)
