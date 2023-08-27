from fictus import FictusFileSystem
from fictus.renderer import Renderer

fs = FictusFileSystem("c:")

fs.mkfile("README.md", "LICENSE.md", ".ignore")

fs.mkdir("/files/docs")
fs.mkdir("/files/music")

fs.cd("/files/docs")  # traverse from root
fs.mkfile("resume.txt", "recipe.wrd")

fs.cd("../music")  # traverse relative from where we started
fs.mkfile("bing.mp3", "bang.mp3", "bop.wav")

# Generate a fs structure to be printed to stdout as text.
fs.cd("c:")  # jump to root
fs.display()

# change the cwd to files/docs and display the fs structure from there
fs.cd("/files/docs")
fs.display()

# Use the customRenderer
customRenderer = Renderer(
    "",
    "",  # Doc open/close
    "📄",
    "",  # File open/close
    "📁",
    "",  # Folder open/close
)

fs.renderer = customRenderer
fs.display()
