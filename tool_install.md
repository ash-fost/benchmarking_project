# Sonicparanoid2
https://gitlab.com/salvo981/sonicparanoid2
https://bioconda.github.io/recipes/sonicparanoid/README.html

Sonicparanoid2 was installed using pixi

we did not use the mmsqs2 function of this tool as it was incompatible with the CPU on the server it required AVX2 and we only had AVX1. This was done using the --graph-only flag.

```bash
wget -qO- https://pixi.sh/install.sh | sh
source ~/.bashrc
cd ~/benchmarking_project
pixi init
pixi workspace channel add conda-forge
pixi workspace channel add bioconda
pixi add python=3.10
pixi add --pypi sonicparanoid
```
run test data

```bash
pixi run sonicparanoid-get-test-data -o sonicparanoid_test_data
cd sonicparanoid_test_data/sonicparanoid_test/
pixi run sonicparanoid -i ./test_input -o ./test_output --project-id my_first_run -t 4 --graph-only
```

problem we were having before (in case we want to try to fit it again)
https://gitlab.com/salvo981/sonicparanoid2/-/work_items/54

# Orthofinder
https://orthofinder.github.io/OrthoFinder/

Orthofinder was installed through a conda environment

```bash
conda create -n of3_env python=3.12
conda activate of3_env
conda install -c conda-forge -c bioconda orthofinder
conda install numpy=1.26.4
```

run test data

```bash
conda activate of3_env
orthofinder -f orthofinder_test_data/
```

# OrthoLoger
https://orthologer.ezlab.org/

https://bioconda.github.io/recipes/orthologer/README.html
 
 OrthoLoger was installed using pixi
 
```bash
pixi add python=3.12 "numpy<2" "scipy<1.13" "orthologer=3.9.1"
pixi add requests
```

run test data

change the paths below to match the location of your OrthoLoger installation and project directory

In the command below, replace:

- **`/home/epolonsky/benchmarking_project`** with the path to your own project directory
- **`.pixi/envs/default/ORTHOLOGER-3.9.1`** with the location of your OrthoLoger installation, if different

```bash
pixi run bash -c 'export PATH="$CONDA_PREFIX/bin:$PATH" /home/epolonsky/benchmarking_project/.pixi/envs/default/ORTHOLOGER-3.9.1/test/run_test.sh prot/main'
```

OrthoLoger writes the test output to the test installation directory:

**`/home/epolonsky/benchmarking_project/.pixi/envs/default/ORTHOLOGER-3.9.1/test/tests/prot/`**

The run log is stored in:

**`/home/epolonsky/benchmarking_project/.pixi/envs/default/ORTHOLOGER-3.9.1/test/tests/prot/RunLogs/`**

To copy the generated test data into the project directory:

```bash
cd ~/benchmarking_project
mkdir orthologer_test_data
cp -r /home/epolonsky/benchmarking_project/.pixi/envs/default/ORTHOLOGER-3.9.1/test/tests/prot/* orthologer_test_data/
```

# proteinortho
https://gitlab.com/paulklemm_PHD/proteinortho/-/tree/master?ref_type=heads

proteinortho was installed through a conda environment

```bash
conda create -n proteinortho_env -c conda-forge -c bioconda python=3.7 proteinortho
```

run test data

```bash
conda activate proteinortho_env
perl proteinortho6.pl -project= proteinortho_test_data/ proteinortho_test_data/C.faa proteinortho_test_data/E.faa proteinortho_test_data/L.faa proteinortho_test_data/M.faa
```


