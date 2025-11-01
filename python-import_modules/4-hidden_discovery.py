#!/usr/bin/env python3
"""
4-hidden_discovery.py
Print all names from hidden_4.pyc that do not start with '__'
"""

if __name__ == "__main__":
    import marshal
    import types

    filename = "/tmp/hidden_4.pyc"

    # Read the compiled file
    with open(filename, "rb") as f:
        f.read(16)  # Skip the header (magic number + timestamp/hash)
        code = marshal.load(f)

    # Collect all names from the code object
    names = set()

    def collect_names(co):
        for name in co.co_names:
            if not name.startswith("__"):
                names.add(name)
        for const in co.co_consts:
            if isinstance(const, types.CodeType):
                collect_names(const)

    collect_names(code)

    # Print names one per line in alphabetical order
    for name in sorted(names):
        print(name)
