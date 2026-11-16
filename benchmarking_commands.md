# Benchmarking Commands and Workflow

## Overview
This document contains the commands and code used to run and benchmark the four orthology inference tools evaluated in this project: SonicParanoid2, Proteinortho, OrthoFinder, and OrthoLoger.

The commands are organized by tool and task to make the benchmarking process reproducible. 

Before running the following commands make sure you are in the cloned benchmarking project directory:

```bash
cd benchmarking_project
```
## Resource Usage

The `/usr/bin/time --verbose` command was used to record resource
usage for each orthology inference tool. This provided information
such as elapsed time, maximum resident set size (memory usage),
and CPU utilization.

Resource usage was saved to a separate text file for each tool.

## Dataset Download

The main benchmarking dataset was downloaded using `wget`

```bash
# Make a new directory within the benchmarking_project directory for the datasets
mkdir -p datasets

# Retrieve the dataset using wget from the orthology benchmarking service webpage
# The 2020_04 dataset was chosen because it allows comparisons with the most methods
nohup wget -P datasets https://ftp.ebi.ac.uk/pub/databases/reference_proteomes/previous_releases/qfo_release-2020_04/QfO_release_2020_04.tar.gz &
```

Extract contents of QfO_release_2020_04.tar.gz:

```bash
# Make a new directory within the datasets directory to extract the contents of the gzipped file
mkdir -p datasets/QfO_release_2020_04

# Extract the contents of the file into the new directory
tar -xzf datasets/QfO_release_2020_04.tar.gz -C datasets/QfO_release_2020_04
```

combine all the protein fasta files for the main benchmarking input

```bash
# Make a new directory within the datasets directory to store just the protein fasta files for input
mkdir -p datasets/QfO_release_2020_04_combined_all

# Copy all the fasta files into the new directory
cp datasets/QfO_release_2020_04/*/*.fasta datasets/QfO_release_2020_04_combined_all

# Remove DNA and protein isoform fasta files to keep just the protein fasta files
rm -f datasets/QfO_release_2020_04_combined_all/*_DNA.fasta 
rm -f datasets/QfO_release_2020_04_combined_all/*_additional.fasta
```

## Orthofinder

```bash
# Activate the conda environment for OrthoFinder
conda activate of3_env

# Run OrthoFinder
nohup /usr/bin/time --verbose -o orthofinder_resource_usage.txt orthofinder -f datasets/QfO_release_2020_04_combined_all -o orthofinder_results &
```

## Proteinortho

```bash
# Activate the conda environment for Proteinortho
conda activate proteinortho_env

# Run Proteinortho
nohup /usr/bin/time --verbose -o proteinortho_resource_usage.txt perl proteinortho6.pl -project=proteinortho_main_benchmark datasets/QfO_release_2020_04_combined_all/*.fasta &
```

## SonicParanoid2

```bash
# Make a new directory within the datasets directory to have just fasta files for SonicParanoid2
# (it would not run if there were intermediate files left over in the input dataset directory from other tools
# so we had to create a clean directory to have just fasta files in it minus the intermediate files)
mkdir -p datasets/sonicparanoid_fasta_only
cp datasets/QfO_release_2020_04_combined_all/*.fasta datasets/sonicparanoid_fasta_only/

# Run SonicParanoid2
nohup /usr/bin/time --verbose -o sonicparanoid_resource_usage.txt pixi run -e sonicparanoid  sonicparanoid -i datasets/sonicparanoid_fasta_only -o sonicparanoid_results --project-id sonicparanoid_main_benchmark --graph-only &
```

## OrthoLoger

```bash
# Make a new directory within the benchmarking_project directory for the OrthoLoger results
mkdir -p orthologer_results

# Initialize the orthologer environment and generate the baseline configuration files
pixi run -e orthologer bash -c '
export PATH="$CONDA_PREFIX/bin:$PATH"
export ODBAPI_URL_VERSION="v12-2"
cd orthologer_results
orthologer -c create
'

# Copy the OrthoMapper configuration script and move into the results directory
cp orthologer_test_data/orthomapper_conf.sh orthologer_results/orthomapper_conf.sh
cd orthologer_results

# Import the Quest for Orthologs (QfO) benchmark dataset into orthologer
pixi run -e orthologer bash -c '
export PATH="$CONDA_PREFIX/bin:$PATH"
export ODBAPI_URL_VERSION="v12-2"
orthologer -c import -d ../datasets/QfO_release_2020_04_combined_all -p orthologer_main_benchmark
'

# Run OrthoLoger
nohup /usr/bin/time --verbose -o ../orthologer_resource_usage.txt pixi run -e orthologer bash -c '
export PATH="$CONDA_PREFIX/bin:$PATH"
export ODBAPI_URL_VERSION="v12-2"
orthologer -c run -p orthologer_main_benchmark
' &
```
