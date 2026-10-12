from typing import overload, List


@overload
def convert(data: int) -> str:
    ...

@overload
def convert(data: List[int]) -> List[str]:
    ...


def convert(data):
    if isinstance(data, int):
        return str(data)
    elif isinstance(data, list):
        return [str(item) for item in data]
    else:
        raise TypeError("Unsupported type")
    

r = convert(10)
print(r.strip())

r = convert([1, 2, 3])
print([s.strip() for s in r])
