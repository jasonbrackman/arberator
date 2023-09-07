from fictus import FictusFileSystem, FictusDisplay
from fictus.renderer import emojiRenderer

ffs = FictusFileSystem("kitchen")
ffs.mkdir("/drawer/forks/old")
ffs.cd("/drawer/forks")
ffs.mkfile("salad.mov", "dinner.mp3")
ffs.cd("old")
ffs.mkfile("pitchfork.bak")
ffs.mkdir("/drawer/spoons")
ffs.cd("/drawer/spoons")
ffs.mkfile("ladle.psd")
ffs.cd("/")
FictusDisplay(ffs).pprint(renderer=emojiRenderer)
