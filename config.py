import runpy

#sk = "training data/0.txt"
sk = "input.txt"
open(sk, "w").close()
runpy.run_path("main.py")

