import os
import sys


def path_t():
    curr_dir = os.getcwd()
    print(f"curr_dir {curr_dir}")
    curr_dir_name = os.path.dirname(curr_dir)
    print(f"curr_dir_name {curr_dir_name}")
    curr_path = __file__
    print(f"curr_path {curr_path}")
    sys_path = sys.path
    print(f"sys_path {sys_path}")


if __name__ == "__main__":
    path_t()
