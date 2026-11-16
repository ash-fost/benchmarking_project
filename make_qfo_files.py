from pathlib import Path


# Create the output folder
output = Path("QfO_2020_04_benchmarking_service_files")
output.mkdir(exist_ok=True)

# Convert the full FASTA IDs into their corresponding UniProt accession numbers
def get_accession(protein):
    parts = protein.split("|") # Split the protein ID using the "|" character

    # Check if the ID is in the UniProt format
    if len(parts) == 3 and parts[0] in ["sp", "tr"]:
        return parts[1]# If it is then return the UniProt accession number

    return protein # Keep the original ID if it is not in the UniProt format

# Save pairs into a new TSV file
def save_pairs(pairs, filename):

    # Open a new file inside the output folder
    with open(output / filename, "w") as f: 

        # Sort the pairs and write out each pair on a separate line
        for a, b in sorted(pairs):
            f.write(a + "\t" + b + "\n")

    # Print out the filename and number of pairs saved
    print(filename, ":", len(pairs), "pairs")



#### Proteinortho ####

# Store protein pairs as a set to not have any duplicates
pairs = set()

# Get the Proteinortho results file
file = Path("proteinortho_results/" "proteinortho_main_benchmark.proteinortho-graph")

# Open the file
with open(file) as f:

    # Read the file one line at a time
    for line in f:

        # Skip any header lines or empty lines
        if not line.startswith("#") and line.strip():

            # Split the line into columns
            fields = line.split()

            # Check that the line has the right amount of columns
            if len(fields) >= 6:

                # Extract the UniProt accession numbers
                a = get_accession(fields[0])
                b = get_accession(fields[1])

                # Only add if the protein pairs are not the same
                if a != b:
                    pairs.add(tuple(sorted((a, b))))


# Save the Proteinortho protein pairs as a TSV file
save_pairs(pairs, "proteinortho_QfO_2020_04.tsv")

#### OrthoFinder ####

# Store protein pairs as a set to not have any duplicates
pairs = set()

# Get the folder with the OrthoFinder orthologue files
folder = Path("orthofinder_results/Results_Oct18/Orthologues")

# Go through all TSV files inside the folder and its subfolders
for file in folder.rglob("*.tsv"):

    # Only use the files that are inside folders named "Orthologues_"
    if not file.parent.name.startswith("Orthologues_"):
        continue

    # Open the file
    with open(file) as f:

        # Skip the header
        next(f, None)  

        # Read the file one line at a time
        for line in f:

            # Split the line into columns
            fields = line.strip().split("\t")

            # Check that the line has the right amount of columns
            if len(fields) < 3:
                continue

            # Separate the proteins from each species
            proteins_a = fields[1].split(",")
            proteins_b = fields[2].split(",")

            # Compare every protein from species A with every protein from species B
            for a in proteins_a:
                for b in proteins_b:

                    # Extract the UniProt accession numbers
                    a = get_accession(a.strip())
                    b = get_accession(b.strip())

                    # Only add if the protein pairs are not the same
                    if a != b:
                        pairs.add(tuple(sorted((a, b))))


# Save the OrthoFinder protein pairs as a TSV file
save_pairs(pairs, "orthofinder_QfO_2020_04.tsv")



#### SonicParanoid2 ####

# Store protein pairs as a set to not have any duplicates
pairs = set()

# Store any files that has unexpected data
problems = []

# Get the folder with the SonicParanoid species-to-species results
folder = Path("sonicparanoid_results/runs/" "sonicparanoid_main_benchmark/" "species_to_species_orthologs")

# Go through all the FASTA files inside the folder and its subfolders
for file in folder.rglob("*.fasta"):

    # Skip anything that is not a file
    if not file.is_file():
        continue

    # Open the file
    with open(file) as f:

        # Read the file one line at a time
        for line in f:

            # Skip any header lines or empty lines
            if line.startswith("Size") or not line.strip():
                continue

            # Split the line into columns
            fields = line.strip().split("\t")

            # Check that the line has the right amount of columns
            if len(fields) != 4:
                problems.append(str(file)) # Keep track of any files with unexpected data
                continue

            # Separate the proteins from each species
            proteins_a = fields[2].split()
            proteins_b = fields[3].split()

            # Check that each protein ID has the right format
            if len(proteins_a) % 2 != 0 or len(proteins_b) % 2 != 0:
                problems.append(str(file)) # Keep track of any files with unexpected data
                continue

            # Extract every second element to get the protein IDs
            proteins_a = [get_accession(proteins_a[i]) for i in range(0, len(proteins_a), 2)]
            proteins_b = [get_accession(proteins_b[i]) for i in range(0, len(proteins_b), 2)]

            # Check that the total number of proteins matches the reported size
            if int(fields[0]) != len(proteins_a) + len(proteins_b):
                problems.append(str(file)) # Keep track of any files with unexpected data
                continue

            # Check that the number of possible pairs matches the reported number
            if int(fields[1]) != len(proteins_a) * len(proteins_b):
                problems.append(str(file)) # Keep track of any files with unexpected data
                continue

            # Compare every protein from species A with every protein from species B
            for a in proteins_a:

                for b in proteins_b:

                    # Only add if the protein pairs are not the same
                    if a != b:
                        pairs.add(tuple(sorted((a, b))))


# If there are any problems identified
if problems:

    # Print out any error messages
    print("SonicParanoid needs checking. No file created.")
    print("Problem files:", len(set(problems)))

# If there are no problems identified
else:

    # Save the SonicParanoid protein pairs as a TSV file
    save_pairs(pairs, "sonicparanoid_QfO_2020_04.tsv")



#### OrthoLoger ####

# Store protein pairs as a set to not have any duplicates
pairs = set()

# Store the relationship between internal IDs and UniProt accessions
id_to_accession = {}

# Get the folder that has the OrthoLoger mapping files
folder = Path("orthologer_results/Rawdata")

# Go through all the mapping files
for file in folder.glob("*.fs.maptxt"):

    # Open the file
    with open(file) as f:

        # Read the file one line at a time
        for line in f:

            # Split the line into columns
            fields = line.strip().split()

            # Check that the line has the right amount of columns
            if len(fields) >= 2:

                # Get the internal protein ID
                internal_id = fields[0]

                # Get the original protein ID
                protein = fields[1]

                # Extract the UniProt accession number
                accession = get_accession(protein)

                # Store the internal ID and its corresponding accession number
                id_to_accession[internal_id] = accession

# Print out the total number of proteins successfully mapped
print("Orthologer proteins mapped:", len(id_to_accession))

# Read the BRH files

# Get the folder with the OrthoLoger pairwise comparison results
folder = Path("orthologer_results/PWC")

# Set the initial protein ID count of ones that cannot be mapped
missing_ids = 0

# Go through all BRH files inside the folder and its subfolders
for file in folder.rglob("*.brh"):

    # Read the file one line at a time
    with open(file) as f:

        # Read the file one line at a time
        for line in f:

            # Skip any header lines or empty lines
            if line.startswith("#") or not line.strip():
                continue

            # Split the line into columns
            fields = line.split()

            # Check that the line has the right amount of columns
            if len(fields) < 2:
                continue

            # Convert the internal IDs into UniProt accession numbers
            a = id_to_accession.get(fields[0])
            b = id_to_accession.get(fields[1])

            # Check if either protein ID is missing from the mapping
            if a is None or b is None:

                # Add one to the missing ID count
                missing_ids += 1
                continue

            # Only add if the protein pairs are not the same
            if a != b:
                pairs.add(tuple(sorted((a, b))))

# Read the INPAR files

# Go through all INPAR files inside the folder and its subfolders
for file in folder.rglob("*.inpar"):

    # Read the file one line at a time
    with open(file) as f:

        # Read the file one line at a time
        for line in f:

            # Skip any header lines or empty lines
            if line.startswith("#") or not line.strip():
                continue

            # Split the line into columns
            fields = line.split()

            # Check that the line has the right amount of columns
            if len(fields) < 2:
                continue

            # The first two proteins are the seed pair
            seed_a = fields[0]
            seed_b = fields[1]

            # Get the species IDs from the seed protein IDs
            species_a = seed_a.split(":")[0]
            species_b = seed_b.split(":")[0]

            # Create a group for each seed protein
            group_a = {seed_a}
            group_b = {seed_b}

            # Read additional in-paralogs
            for field in fields[3:]:

                # Extract the internal protein ID
                internal_id = field.split(";")[0]

                # Add the protein to the group from the same species
                if internal_id.startswith(species_a + ":"):
                    group_a.add(internal_id)

                elif internal_id.startswith(species_b + ":"):
                    group_b.add(internal_id)

            # Create pairs between the two groups
            for protein_a in group_a:
                for protein_b in group_b:

                     # Convert the internal IDs into UniProt accession numbers
                    a = id_to_accession.get(protein_a)
                    b = id_to_accession.get(protein_b)

                     # Check if either protein ID is missing from the mapping
                    if a is None or b is None:

                        # Add one to the missing ID count
                        missing_ids += 1
                        continue

                    # Only add if the protein pairs are not the same
                    if a != b:
                        pairs.add(tuple(sorted((a, b))))

# Print out the total number of protein IDs that could not be mapped
print("Orthologer missing ID mappings:", missing_ids)

# If there are no missing protein IDs
if missing_ids == 0:

    # Save the OrthoLoger protein pairs into a new TSV file
    save_pairs(pairs, "orthologer_QfO_2020_04.tsv")

# If there are missing protein IDs identified
else:

    # Print out any error messages
    print("Orthologer file was NOT created.")
    print("Some protein IDs could not be mapped. Check the mapping files.")
