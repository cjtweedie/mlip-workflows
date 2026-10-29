import os
from pathlib import Path
from NEB.remap_poscar import main

# specify current working directory as repo_root,
# must contain initial/final POSCAR, config.yml files
# config.yml should specify names of initial/final POSCARs, ensure remap_f_i = true
dir = os.getcwd()
main(repo_root = Path(dir))