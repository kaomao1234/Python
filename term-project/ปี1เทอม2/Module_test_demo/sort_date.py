from typing import Tuple


timestamps = ['2020/8/16','2020/8/12','2020/8/13']
p = sorted(timestamps, key=lambda d: list(map(int, d.split('/'))),reverse=True)
print(p)