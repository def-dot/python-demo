import zlib
import hashlib


# 示例文件路径
file_path = 'D:\code\python-demo\standard_t\libexample.so'


def calculate_crc32_for_file(file_path):
    # 打开文件并以二进制模式读取内容
    with open(file_path, 'rb') as file:
        # 初始化 CRC 寄存器
        crc32_value = 0
        # 逐块更新 CRC32
        for chunk in iter(lambda: file.read(8192), b''):
            crc32_value = zlib.crc32(chunk, crc32_value)
    return crc32_value & 0xFFFFFFFF  # 保证结果是一个无符号 32 位整数



def calculate_sha256_for_file(file_path):
    sha256_hash = hashlib.sha256()

    # 以二进制模式打开文件并逐块更新哈希值
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)

    # 获取最终的哈希值
    sha256_result = sha256_hash.hexdigest()
    return sha256_result


def calculate_md5_for_file(file_path):
    md5_hash = hashlib.md5()

    # 以二进制模式打开文件并逐块更新哈希值
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)

    # 获取最终的哈希值
    md5_result = md5_hash.hexdigest()
    return md5_result


crc32_result = calculate_crc32_for_file(file_path)
crc32_result = hex(crc32_result)

sha256_result = calculate_sha256_for_file(file_path)

md5_result = calculate_md5_for_file(file_path)

# 输出结果
print(f"文件路径: {file_path}")
print(f"CRC32 校验值: {crc32_result}")
print(f"SHA256 校验值: {sha256_result}")
print(f"MD5 校验值: {md5_result}")
