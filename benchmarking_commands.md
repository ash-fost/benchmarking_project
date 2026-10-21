# Benchmarking Commands and Workflow

## Overview
This document contains the commands and code used to run and benchmark the four orthology inference tools evaluated in this project: SonicParanoid2, Proteinortho, OrthoFinder, and OrthoLoger.

The commands are organized by tool and task to make the benchmarking process reproducible. 

## Dataset Download

The main benchmarking dataset was downloaded using `wget`

```bash
cd benchmarking_project
#change to the directory that contains the tools to be benchmarked
mkdir datasets
#make a new directory within the benchmarking_project directory for the datasets
nohup wget -P datasets https://ftp.ebi.ac.uk/pub/databases/reference_proteomes/previous_releases/qfo_release-2020_04/QfO_release_2020_04.tar.gz &
#retrieves the dataset using wget from the orthology benchmarking service webpage
#the 2020_04 dataset was chosen because it allows comparisons with the most tools
```

extract species for the subdatasets
```bash
cd datasets
#change directories to the newly created datasets directory
tar -xzf QfO_release_2020_04.tar.gz -C . Eukaryota/UP000005640_9606.fasta Eukaryota/UP000002277_9598.fasta Eukaryota/UP000000589_10090.fasta Eukaryota/UP000002494_10116.fasta Eukaryota/UP000002254_9615.fasta Eukaryota/UP000009136_9913.fasta Eukaryota/UP000000437_7955.fasta Eukaryota/UP000000803_7227.fasta Eukaryota/UP000001940_6239.fasta Eukaryota/UP000002311_559292.fasta Eukaryota/UP000006548_3702.fasta
#creates fasta files of species within the larger dataset for subdatasets

mkdir distant_species
#makes a new directory within the datasets directory for distant species
mkdir close_species
#makes a new directory within the datasets directory for close species

# copy the close species into one folder
cp Eukaryota/UP000005640_9606.fasta Eukaryota/UP000002277_9598.fasta Eukaryota/UP000000589_10090.fasta Eukaryota/UP000002494_10116.fasta Eukaryota/UP000002254_9615.fasta Eukaryota/UP000009136_9913.fasta close_species/

# copy the distant species into one folder
cp Eukaryota/UP000005640_9606.fasta Eukaryota/UP000000437_7955.fasta Eukaryota/UP000000803_7227.fasta Eukaryota/UP000001940_6239.fasta Eukaryota/UP000002311_559292.fasta Eukaryota/UP000006548_3702.fasta distant_species/
```

## SonicParanoid2

## Proteinortho

## Orthofinder

## OrthoLoger
