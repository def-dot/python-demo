# sha256
import hashlib
import os.path


def hash256_t():
    # sha256=BNO-Wca_xBq_6PPMsYfF-50fag6h_8SP7tKKv1eA3Nk,752
    # sha256=04d3be59c6bfc41abfe8f3ccb187c5fb9d1f6a0ea1ffc48feed28abf5780dcd9
    with open("../suanfa/array_find_once_t.py", "rb") as f:
        content = f.read()
        hash_obj = hashlib.sha256()
        hash_obj.update(content)
        hash_val = hash_obj.hexdigest()
        return hash_val


def get_file_size():
    return os.path.getsize("../suanfa/array_find_once_t.py")


if __name__ == "__main__":
    r = hash256_t()
    print(f"hash 256 {r}")
    r = get_file_size()
    print(f"file size {r}")
