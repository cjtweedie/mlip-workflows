import os
from pathlib import Path
from NEB.remap_poscar import main

# this script remaps atomic indices in POSCAR_f without needing to run a full NEB calc
# useful for getting correct end point structures to run a DFT refinement on converged NEB path
# for a different charge state, where the intermediate images are a good starting point,
# but start/end point geometries differ

# specify current working directory as repo_root,
# must contain initial/final POSCAR, config.yml files
# config.yml should specify names of initial/final POSCARs, ensure remap_f_i = true
dir = os.getcwd()
main(repo_root = Path(dir))