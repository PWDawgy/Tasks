"""Getting Started Example.

https://pypi.org/project/redis/

By default all responses are returned as bytes in Python3. The user is
responsible for decoding to Python3 strings.

Note: If all string responses from a client should be decoded, the user
can specify "decode_responses=True" to Redis__init__.
In this case, any Redis command that returns a string type will be
decoded with the encoding specified.
"""
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
print("r.set('foo', 'bar') {}", r.set('foo', 'bar'))
print("r.get(\'foo\') {}", r.get('foo'))
