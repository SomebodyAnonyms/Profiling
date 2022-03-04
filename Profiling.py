import cProfile
import importlib
import os
import sys
from pstats import Stats

try: os.mkdir("Profiling")
except: pass

with cProfile.Profile() as Profile:
    importlib.import_module(sys.argv[1].replace(".py", ""))

with open("Profiling/Result.txt", "w") as File:
    stats = Stats(Profile, stream=File)
    stats.strip_dirs()
    stats.sort_stats("time")
    stats.dump_stats("Profiling/Result.prof")
    stats.print_stats()

os.system(f"snakeviz ./Profiling/Result.prof")