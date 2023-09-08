from fictus import FictusDisplay, FictusFileSystem, Renderer
from fictus.renderer import emojiRenderer, RenderTag, RenderTagEnum

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
ffs.cd("\\")  # jump to _root

display = FictusDisplay(ffs)
display.pprint(renderer=emojiRenderer)

# FictusDisplay the ffs structure after a relative change of directory to files/docs
ffs.cd("files/music")
display.pprint()

# Update the display to use emojiRenderer from its defaultRenderer and pprint again.
# Note how this is a one time emojiRenderer.  Calling pprint() again without the
# renderer optional value will result in the defaultRenderer being used.
display.pprint(renderer=emojiRenderer)

# Create a customRenderer, apply it to a FictusDisplay and update the ffs to use it.
customRenderer = Renderer()
customRenderer.register(RenderTagEnum.FILE, RenderTag("· ", ""))
customRenderer.register(RenderTagEnum.FOLDER, RenderTag("+ ", "\\"))

# Update display to the customRenderer permanently. Each call to pprint() will use the
# customRenderer unless the optional renderer is passed in like the emoji example above.
display.renderer = customRenderer
display.pprint()
