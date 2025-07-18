#!/usr/bin/env python3
import marshal
import types
if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)  # Skip pyc header
        code = marshal.load(f)
    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)
    names = [name for name in dir(module) if not name.startswith("__")]
    for name in sorted(names):
        print(name)
