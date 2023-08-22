from arbor import System
from arbor.renderer import MarkdownRenderer, DefaultRenderer

s = System("root")
s.mkfiles(["README.md", "LICENSE.md", ".ignore"])

s.mkdirs("files/docs")
s.mkdirs("files/music")

s.cd("files/docs")
s.mkfiles(["resume.txt", "recipe.wrd"])

s.cd("../../files/music")
s.mkfiles(["bing.mp3", "bang.mp3", "bop.wav"])

# Generate a tree structure to be printed to stdout as text.
s.display()

# Override the renderer and print a tree structure using Markdown sugar.
s.renderer = MarkdownRenderer()
s.display()
