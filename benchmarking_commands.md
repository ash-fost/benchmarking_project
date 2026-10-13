# Benchmarking Commands and Workflow

## Overview
This document contains the commands and code used to run and benchmark the four orthology inference tools evaluated in this project: SonicParanoid2, Proteinortho, OrthoFinder, and OrthoLoger.

The commands are organized by tool and task to make the benchmarking process reproducible. 

## Dataset Download

The main benchmarking dataset was downloaded using `wget`

```bash
cd benchmarking_project
mkdir datasets
nohup wget -P datasets https://ftp.ebi.ac.uk/pub/databases/reference_proteomes/previous_releases/qfo_release-2020_04/QfO_release_2020_04.tar.gz &
```

Extract contents of QfO_release_2020_04.tar.gz

```bash
cd benchmarking_project/datasets
mkdir QfO_release_2020_04
cd QfO_release_2020_04
tar -xzf ~/benchmarking_project/datasets/QfO_release_2020_04.tar.gz -C .
```

combine all the files for the main benchmarking input

```bash
benchmarking_project/datasets
mkdir QfO_release_2020_04_combined_all
cp QfO_release_2020_04/*/*.fasta QfO_release_2020_04_combined_all
rm QfO_release_2020_04_combined_all/*_DNA.fasta # remove DNA fasta files to keep just the protein fasta files
```

extract species for the subdatasets

```bash
cd benchmarking_project/datasets
mkdir distant_species
mkdir close_species

# copy the close species into one folder
cp QfO_release_2020_04/Eukaryota/UP000005640_9606.fasta QfO_release_2020_04/Eukaryota/UP000002277_9598.fasta QfO_release_2020_04/Eukaryota/UP000000589_10090.fasta QfO_release_2020_04/Eukaryota/UP000002494_10116.fasta QfO_release_2020_04/Eukaryota/UP000002254_9615.fasta QfO_release_2020_04/Eukaryota/UP000009136_9913.fasta close_species/

# copy the distant species into one folder
cp QfO_release_2020_04/Eukaryota/UP000005640_9606.fasta QfO_release_2020_04/Eukaryota/UP000000437_7955.fasta QfO_release_2020_04/Eukaryota/UP000000803_7227.fasta QfO_release_2020_04/Eukaryota/UP000001940_6239.fasta QfO_release_2020_04/Eukaryota/UP000002311_559292.fasta QfO_release_2020_04/Eukaryota/UP000006548_3702.fasta distant_species/
```

## SonicParanoid2

## Proteinortho

```bash
# do not run this it is unfinished I am working on it
perl proteinortho6.pl -project=main_benchmark_results datasets/QfO_release_2020_04.tar.gz
```

## Orthofinder

## OrthoLoger
