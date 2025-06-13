import re

n = int(raw_input()) # type: ignore

for _ in range(n):
    pattern = raw_input() # type: ignore
    try:
        re.compile(pattern)
        print True    # type: ignore
    except re.error:
        print False # type: ignore
        