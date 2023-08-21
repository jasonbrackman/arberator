# Arbor


Arbor can create a dummy Tree view for the purposes of documentation.

Example:
```
from arbor import System

s = System("root")
s.mkfiles(["README.md", "LICENSE.md", ".ignore"])

s.mkdirs("files/docs")
s.mkdirs("files/music")

s.cd("files/docs")
s.mkfiles(["resume.txt", "recipe.wrd"])

s.cd("../../files/music")
s.mkfiles(["bing.mp3", "bang.mp3", "bop.wav"])

s.display()

```
Produces:
```
root\
├─ files\
│  ├─ docs\
│  │  ├─ recipe.wrd
│  │  └─ resume.txt
│  └─ music\
│     ├─ bang.mp3
│     ├─ bing.mp3
│     └─ bop.wav
├─ .ignore
├─ LICENSE.md
└─ README.md
```

## Building/installing the Wheel:
To build the package requires setuptools and build.
>python3 -m build

Once built:
>pip install dist/arbor-0.0.1-py3-none-any.whl --force-reinstall`