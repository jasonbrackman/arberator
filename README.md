## Fictus

Fictus allows a user to create and output a fictitious file system for sharing in a text driven environment.

```Text
🏡kitchen
└─ 📁drawer
   ├─ 📁forks
   │  ├─ 📁old
   │  │  └─ 📄pitchfork.bak
   │  ├─ 📄dinner.mp3
   │  └─ 📄salad.mov
   └─ 📁spoons
      └─ 📄ladle.psd
```
Fictus use cases include creating output for a wiki page, communicating a folder structure to a colleague over chat, or
mocking a file/folder structure layout before committing to actual creation on disk.  Since Fictus mimics a File System,
calling code can create complex loops to build up as little or as much as required to get an idea across.

### FictusFileSystem
Creating a Fictus File System starts with instantiating a FicutsFileSystem object and, optionally, providing
a name to use as the drive letter.  If one is not provided, a single slash ('/') will be used.

```Python
from fictus import FictusFileSystem

# Create a FictusFileSystem.
ffs = FictusFileSystem("c")
```

The object can then be built up using creation methods, such as `mdir` and `mkfile` and folder traversal can occur
using `cd`.


```Python
# create some directories
ffs.mkdir("/files/docs")
ffs.mkdir("/files/music/folk")

# Create some files in the current working directory (happens to be root).
ffs.mkfile("README.md", "LICENSE.md", ".ignore")

# Change directory to the `docs` and make more files. Start with `/` to traver from root.
ffs.cd("/files/docs")
ffs.mkfile("resume.txt", "recipe.wrd")

# Change directory to `music/folk`.  Note the relative cd from the `docs` folder. 
ffs.cd("../music/folk")
ffs.mkfile("bing.mp3", "bang.mp3", "bop.wav")
```

### FictusDisplay
A FictusDisplay can output the FFS.

```Python

from fictus import FictusDisplay

ffs.cd("/")  # ensure the cwd is the root of the file system

# Generate a ffs structure to be printed to stdout as text.
display = FictusDisplay(ffs)
display.pprint()
```

Produces:

```Text
c:\
├─ files\
│  ├─ docs\
│  │  ├─ recipe.wrd
│  │  └─ resume.txt
│  └─ music\
│     └─ folk\
│        ├─ bang.mp3
│        ├─ bing.mp3
│        └─ bop.wav
├─ .ignore
├─ LICENSE.md
└─ README.md
```

The display can also be generated in place:

```Python
FictusDisplay(ffs).pprint()
```

The tree displayed starts at current working directory. The same example
above with the current directory set to "c:/files/music" produces:

```Text
music\
└─ folk\
   ├─ bang.mp3
   ├─ bing.mp3
   └─ bop.wav
```

### Renderer
A FictusDisplay does allow the user to customize output for the DOC, ROOT, FOLDER, and 
FILE types.  The Renderer can be permanently reassigned by assinging to the `renderer`
property. Here is an example that takes advantage of the built-in `emojiRenderer`.  

```Python
from fictus.renderer import emojiRenderer
...
# FictusDisplay the ffs structure after a relative change of directory to files/music
ffs.cd("files/music")

# assign a new Renderer
display.renderer = emojiRenderer

# ouptut with the new Renderer applied
display.pprint()
```

This produces:

```Text
📁music
└─ 📁folk
   ├─ 📄bang.mp3
   ├─ 📄bing.mp3
   └─ 📄bop.wav
```

In the above example the renderer was updated so that each call to print will now use
the emojiRenderer. If the main renderer is not required to be updated and its meant to
just showcase one call in a different way the pprint() has an optional `renderer` argument.

```Python
from fictus.renderer import defaultRenderer
# current renderer is the emojiRenderer

# uses defaultRenderer just this one time
display.pprint(renderer=defaultRenderer)  

# use the emojiRenderer that was setup in the previous example set.
display.pprint() 
```

## Customization
Customization may be useful for creating HTML, Markdown, or other custom tags that are
not already provided.

For example:

```Python
from fictus.renderer import RenderTagEnum, RenderTag

# A customRenderer is created: adds special characters before a File or Folder.
customRenderer = Renderer()
customRenderer.register(RenderTagEnum.FILE, RenderTag("· ", ""))
customRenderer.register(RenderTagEnum.FOLDER, RenderTag("+ ", "\\"))

# Update display_model to the customRenderer
display.renderer = customRenderer
display.pprint()
```

Produces:

```Text
+ music\
└─ + folk\
   ├─ · bang.mp3
   ├─ · bing.mp3
   └─ · bop.wav
```


## Install Using Pip
>pip install fictus

## Building/installing the Wheel locally:
To build the package requires setuptools and build.
>python3 -m build

Once built:
>pip install dist/fictus-*.whl --force-reinstall
