# benchmarking_project

## Project Overview

This project aims to benchmark four orthology prediction tools to investigate their accuracy, computational performance, and the effect of evolutionary distance on ortholog prediction.

The four tools benchmarked are:

| Tool | Version | Execution Method | Source |
|------|---------|------------------|--------|
| SonicParanoid2 | 2.0.9 | Pixi environment (pixi) | https://gitlab.com/salvo981/sonicparanoid2 |
| Proteinortho   | 6.3.6  | Conda environment (proteinortho_env) | https://gitlab.com/paulklemm_PHD/proteinortho/-/tree/master?ref_type=heads   |
| OrthoFinder    | 2.5.5 | Conda environment (of3_env) | https://orthofinder.github.io/OrthoFinder/ |
| OrthoLoger     | 3.9.1 | Pixi environment (pixi) | https://orthologer.ezlab.org/ |


The tools will be evaluated using protein reference datasets from closely related and distantly related species. We will also investigate whether dataset size affects tool performance.

## Research Questions

Our project will address three main questions:

1. **Accuracy:** Which tool most accurately identifies orthologous genes?
2. **Efficiency:** Which tool has the shortest runtime and lowest memory usage?
3. **Evolutionary distance:** Does evolutionary distance between species affect the accuracy of orthology predictions?

## Background

Orthologs are genes in different species that evolved from a common ancestral gene. Orthologous genes often retain similar biological functions, making them useful for transferring functional annotations between species and studying evolutionary relationships.

Computational tools identify orthologs using different combinations of sequence similarity searches, reciprocal best-hit approaches, graph clustering, and phylogenetic analysis. Because these methods differ, they may produce different orthology predictions and computational requirements.

## Tool Installation

Installation instructions, software versions, dependencies, and example commands will be documented in `tool_install.md`.

## Data Selection

The data for this project is selected from the European Bioinformatics Institute (EBI) Quest for Orthologs (QfO) reference proteome collection. The collection of datasets can be found using the link below.

**QfO reference proteome releases:** `https://ftp.ebi.ac.uk/pub/databases/reference_proteomes/previous_releases/`

The dataset we are using: 

**QfO release 2020_04:** `https://ftp.ebi.ac.uk/pub/databases/reference_proteomes/previous_releases/qfo_release-2020_04/`

Reference proteomes provide protein sequences for different species and can be used as input for orthology inference tools.

## Dataset Categories

The types of datasets used in this project:

| Dataset | Species | Purpose |
|---------|---------|---------|
| Full | All 78 QfO species | Main benchmark |
| Close | list species used | Closely related species |
| Distant | list species used | More distantly related species |

Species were selected based on their evolutionary relationships and the availability of suitable proteomes and reference orthology data.

## Species

| Proteome_ID | Species | Common Name | NCBI Taxonomy ID | Subset |
|-------------|---------|-------------|---|---|
| `UP000005640` | *Homo sapiens* | Human | 9606 | Close and distant |
| `UP000002277` | *Pan troglodytes* | Chimpanzee | 9598 | Close |
| `UP000000589` | *Mus musculus* | House mouse | 10090 | Close |
| `UP000002494` | *Rattus norvegicus* | Brown rat | 10116 | Close |
| `UP000002254` | *Canis lupus familiaris* | Domestic dog | 9615 | Close |
| `UP000009136` | *Bos taurus* | Cattle | 9913 | Close |
| `UP000000437` | *Danio rerio* | Zebrafish | 7955 | Distant |
| `UP000000803` | *Drosophila melanogaster* | Fruit fly | 7227 | Distant |
| `UP000001940` | *Caenorhabditis elegans* | Roundworm | 6239 | Distant |
| `UP000002311` | *Saccharomyces cerevisiae* | Budding yeast | 559292 | Distant |
| `UP000006548` | *Arabidopsis thaliana* | Thale cress | 3702 | Distant |

**Dataset summary:** The dataset contains 11 eukaryotic species. The close subset includes six mammalian species, and the distant subset includes six species representing diverse eukaryotic lineages. Human is shared between both subsets.

## Comparing the Tools

The tools are compare using the following measures:

| Category | Measurement |
|----------|-------------|
| Accuracy | Precision, recall, and F1 score |
| Runtime | *`time`* |
| Memory | *`/usr/bin/time —verbose`* |
| Agreement | Overlap and differences between predicted ortholog relationships |
| Evolutionary distance | Changes in accuracy between closely related and distantly related species |
| Dataset size | Changes in runtime, memory, and accuracy across dataset sizes |
