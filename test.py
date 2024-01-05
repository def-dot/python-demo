d = {
            'normal': None,
            # 'disposed': ({"ip": "127.0.0.1"}, "sjj"),
            'deleted': None
        }

res = d.get('normal') or d.get('disposed') or d.get('deleted')
print(f"{res}")
if res:
    print(res[1])
    print(res[0])
