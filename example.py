from arber import System

s = System("root")
s.mkfiles(["README.md"])
s.mkdirs("music/")
s.cd("music")
s.mkfiles(["fizz.mp3", "bang.mp3", "pop.wav"])
s.cd("..")
s.mkdirs("files\docs")
s.cd("files")
s.mkfiles([".ignore"])
s.cd("docs")
s.mkfiles(["resume.txt", "recipe.wrd"])

s.display()
