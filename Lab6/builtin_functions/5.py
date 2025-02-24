#program with builtin function that returns True if all elements of the tuple are true.
import os

def all_true(t):
    return all(t)

tuple1 = (True, True, True)
tuple2 = (False, True, True)
tuple3 = (False, False, True)
tuple4 = (False, False, False)
tuple5 = (True, True, False)
tuple6 = (True, False, False)

print(all_true(tuple1))
print(all_true(tuple2))
print(all_true(tuple3))
print(all_true(tuple4))
print(all_true(tuple5))
print(all_true(tuple6))