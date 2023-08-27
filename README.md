# Fictus

Fictus generates a fake file system (FFS) that can be sent to stdout to display in 
documentation or presentations.

Example:
```
from fictus import FictusFileSystem
from fictus.renderer import Renderer

# The FFS has a default root name of '/'; Below overrides the default with 'c:'.
fs = FictusFileSystem("c:")

# Create files at root, the cwd.
fs.mkfile("README.md", "LICENSE.md", ".ignore")

# Create dir and files; note paths are relative to current working directory
fs.mkdir("files/docs")  
fs.cd("files/docs")     
fs.mkfile("resume.txt", "recipe.wrd")

# Create/Change dir to music; start with a `/` to ensure traversal from root.
fs.mkdir("/files/music")
fs.cd("/files/music")
fs.mkfile("bing.mp3", "bang.mp3", "bop.wav")

# Generate a tree structure to be printed to stdout as text.
fs.cd("c:")  # jump to root; could have used "/" instead of "c:"
fs.display()
```
Produces:
```
c:\
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
above with the current directory set to "c:/files/docs" produces:
```
c:\files\
     ├─ docs\
     │  ├─ recipe.wrd
     │  └─ resume.txt
```
The way the Tree is displayed can be manipulated by overriding the Renderer.
The default renderer will display the FFS as simple text.  But you can override
the Renderer to use HTML, Markdown, or any other format you want.

Example:
```

from fictus.renderer import Renderer

# create a customRenderer
customRenderer = Renderer(
    "", "",  # Doc open/close
    "📄", "",  # File open/close
    "📁", "",  # Folder open/close
)

fs.renderer = customRenderer
fs.display()
```
Produces:
```
c:\files\
     ├─ 📁docs\
     │  ├─ 📄recipe.wrd
     │  └─ 📄resume.txt
```

## Install Using Pip
>pip install fictus

## Building/installing the Wheel locally:
To build the package requires setuptools and build.
>python3 -m build

Once built:
>pip install dist/fictus-*.whl --force-reinstall
