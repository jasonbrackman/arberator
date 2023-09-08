### Fictus

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

A code example:

```Python
from fictus import FictusFileSystem

# Create a FictusFileSystem.
ffs = FictusFileSystem("c")

# Create some files in the current working directory.
ffs.mkfile("README.md", "LICENSE.md", ".ignore")

# Create dir and files relative to the current working directory.
ffs.mkdir("./files/docs")
ffs.cd("./files/docs")
ffs.mkfile("resume.txt", "recipe.wrd")

# Create/Change dir to music. Start with a `/` to ensure traversal from _root.
ffs.mkdir("/files/music/folk")
ffs.cd("/files/music/folk")
ffs.mkfile("bing.mp3", "bang.mp3", "bop.wav")

# Generate a ffs structure to be printed to stdout as text.
ffs.cd("/")  # jump to _root; could have used "/" instead of "c:"
```

A FictusDisplay can output the FFS.

```Python
from fictus import FictusDisplay

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

A FictusDisplay does allow the user to customize output for the DOC, ROOT, FOLDER, and 
FILE types.  The Renderer can be changed from default for the code lifetime using the 
`set_renderer` function. Here is an example that takes advantage of the built-in 
`emojiRenderer`.  The existing Display is updated and a pprint is called again.

```Python
from fictus.renderer import emojiRenderer
...
# FictusDisplay the ffs structure after a relative change of directory to files/music
ffs.cd("files/music")
display.renderer = emojiRenderer
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
