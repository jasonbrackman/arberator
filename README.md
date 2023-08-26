# Fictus

Fictus generates a fake file system (FFS) that can be sent to stdout to display in 
documentation or presentations.

Example:
```
from fictus import FictusFileSystem
from fictus.renderer import Renderer

# The FS will default to a root name of '/'; Below overrides default with `c:`
fs = FictusFileSystem("c:")

# create some files at root
fs.mkfile("README.md", "LICENSE.md", ".ignore")

# create directories relative to where we are in the FS.
fs.mkdir("files/docs")
fs.mkdir("files/music")

# change directory to docs and make some files.
fs.cd("/files/docs")
fs.mkfile("resume.txt", "recipe.wrd")

# Change directory to music; start with a `/` to ensure traversal from root.
fs.cd("/files/music")
fs.mkfile("bing.mp3", "bang.mp3", "bop.wav")

# Generate a tree structure to be printed to stdout as text.
fs.cd("c:")  # jump to root
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
above with the current directory set to "root/files/docs" produces:
```
c:\files\
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
