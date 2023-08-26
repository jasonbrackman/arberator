from fictus import System
from fictus.renderer import Renderer

s = System()
s.mkfile("README.md", "LICENSE.md", ".ignore")

s.mkdir("files/docs")
s.cd("/files/docs")
s.mkfile("resume.txt", "recipe.wrd")

s.mkdir("files/music")
s.cd("/files/music")
s.mkfile("bing.mp3", "bang.mp3", "bop.wav")

# Generate a tree structure to be printed to stdout as text.
s.cd("/")  # jump to root
s.display()

# change the cwd to files/docs and display the tree structure from there
s.cd("/files/docs")
s.display()

# Use the customRenderer
customRenderer = Renderer(
    "",
    "",  # Doc open/close
    "📄",
    "",  # File open/close
    "📁",
    "",  # Folder open/close
)

s.renderer = customRenderer
s.display()
