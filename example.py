from fictus import Display, FictusFileSystem, Renderer

# Create a FictusFileSystem. The default root name of '/' has been replaced with 'c:'
ffs = FictusFileSystem("c:")

# Create some files in the current working directory.
ffs.mkfile("README.md", "LICENSE.md", ".ignore")

# Create dir and files relative to the current working directory.
ffs.mkdir("./files/docs")
ffs.cd("./files/docs")
ffs.mkfile("resume.txt", "recipe.wrd")

# Create/Change dir to music. Start with a `/` to ensure traversal from root.
ffs.mkdir("/files/music")
ffs.cd("/files/music")
ffs.mkfile("bing.mp3", "bang.mp3", "bop.wav")

# Generate a ffs structure to be printed to stdout as text.
ffs.cd("c:")  # jump to root; could have used "/" instead of "c:"
ffs.display()

# Display the ffs structure after a relative change of directory to files/docs
ffs.cd("files/docs")
ffs.display()

# Create a customRenderer, apply it to a Display and update the ffs to use it.
customRenderer = Renderer(
    "",
    "",  # Doc open/close
    "📄",
    "",  # File open/close
    "📁",
    "",  # Folder open/close
)
# Update display to the customRenderer
display = Display(customRenderer)
ffs.set_display(display)
ffs.display()
