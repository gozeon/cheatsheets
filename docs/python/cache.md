
## cachetools


```python title="cache.py"
from cachetools import cached, TLRUCache
from datetime import datetime, timedelta
from random import random

def my_ttu(_key, _value, now):
    # 随机每个key的过期时间
    return now + timedelta(hours=random())

@cached(cache=TLRUCache(maxsize=10, ttu=my_ttu, timer=datetime.now))
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```
