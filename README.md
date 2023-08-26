# Fictus

Fictus generates a fake Tree View to stdout for the purpose of documentation.

Example:
```
from fictus import System


s = System("root")
s.mkfile("README.md", "LICENSE.md", ".ignore")

s.mkdir("files/docs")
s.mkdir("files/music")

s.cd("files/docs")
s.mkfile("resume.txt", "recipe.wrd")

s.cd("../../files/music")
s.mkfile("bing.mp3", "bang.mp3", "bop.wav")

# jump to root
s.cd("/")

# Generate a tree structure to be printed to stdout as text.
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

The tree displayed starts at current working directory. The same example
above with the current directory set to "root/files/docs" produces:
```
root\files\
     ├─ docs\
     │  ├─ recipe.wrd
     │  └─ resume.txt
```
The way the Tree is displayed can be manipulated by overriding the Renderer.
The default renderer will display the Tree as simple text.  But you can override
the settings to display the Tree as HTML, Markdown, or any other format you want.

Example:
```
# Use the customRenderer
from fictus.renderer import Renderer

customRenderer = Renderer(
    "", "",  # Doc open/close
    "📄", "",  # File open/close
    "📁", "",  # Folder open/close
)

s.renderer = customRenderer
s.display()
```
Produces:
```
📁root\
├─ 📁files\
│  ├─ 📁docs\
│  │  ├─ 📄recipe.wrd
│  │  └─ 📄resume.txt
│  └─ 📁music\
│     ├─ 📄bang.mp3
│     ├─ 📄bing.mp3
│     └─ 📄bop.wav
├─ 📄.ignore
├─ 📄LICENSE.md
└─ 📄README.md
```

## Install Using Pip
>pip install fictus

## Building/installing the Wheel locally:
To build the package requires setuptools and build.
>python3 -m build

Once built:
>pip install dist/fictus-*.whl --force-reinstall
