import os

with open(os.path.join('..', 'pyproject.toml'), 'r') as f:
    version = [l for l in f.read().splitlines(keepends=False) if 'version' in l][0].split(' ')[-1].strip('\"')
    print(a)
