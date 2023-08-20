# Arber


Arber can create a dummy Tree view for the purposes of documentation.

Example:
```
from arber import System

s = System("root")
s.mkfiles(["README.md"])
s.mkdirs("music/")
s.cd("music")
s.mkfiles(["fizz.mp3", "bang.mp3", "pop.wav"])
s.cd("..")
s.mkdirs("files\docs")
s.cd("files")
s.mkfiles([".ignore"])
s.cd("docs")
s.mkfiles(["resume.txt", "recipe.wrd"])

s.display()
```
Produces:
```
root\
├─ files\
│  ├─ docs\
│  │  ├─ recipe.wrd
│  │  └─ resume.txt
│  └─ .ignore
├─ music\
│  ├─ bang.mp3
│  ├─ fizz.mp3
│  └─ pop.wav
└─ README.md
```

## Building/installing the Wheel:
To build the package requires setuptools and build.
>python3 -m build

Once built:
>pip install dist/arber-0.0.1-py3-none-any.whl --force-reinstall`