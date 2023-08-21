from arbor import System

s = System("root")
s.mkfiles(["README.md", "LICENSE.md", ".ignore"])

s.mkdirs("files/docs")
s.mkdirs("files/music")

s.cd("files/docs")
s.mkfiles(["resume.txt", "recipe.wrd"])

s.cd("../../files/music")
s.mkfiles(["bing.mp3", "bang.mp3", "bop.wav"])
s.display()
