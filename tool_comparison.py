from pathlib import Path


# Get the location of the directory containing the four TSV prediction files 
folder = Path("QfO_2020_04_benchmarking_service_files")

# Get the names and locations of the four TSV prediction files
files = {
    "OrthoFinder":    folder / "orthofinder_QfO_2020_04.sorted.tsv",
    "Proteinortho":   folder / "proteinortho_QfO_2020_04.sorted.tsv",
    "SonicParanoid2": folder / "sonicparanoid_QfO_2020_04.sorted.tsv",
    "OrthoLoger":     folder / "orthologer_QfO_2020_04.sorted.tsv",
}

# Store which tools predicted each protein pair
pair_tools = {}

# Store the number of predictions for each method
total = {}

# Read each method's prediction file
for method in files:

    total[method] = 0

    # Open the file
    with open(files[method]) as file:

        # Read the file one line at a time
        for line in file:

            # Create an empty list for the pair if it is new
            if line not in pair_tools:
                pair_tools[line] = []

            # Record that this tool predicted the pair
            pair_tools[line].append(method)

            # Count the prediction for this method
            total[method] += 1

# Count the pairs predicted by only one tool and by all four tools
unique = {method: 0 for method in files}
shared_all = 0

for tools in pair_tools.values():

    # Predicted by all four tools
    if len(tools) == 4:
        shared_all += 1

    # Predicted by only one tool
    if len(tools) == 1:
        unique[tools[0]] += 1

# Print the results for each tool
for method in files:
    print(method)
    print("Number of ortholog pair predictions:", f"{total[method]:,}")
    print("Ortholog pair predictions unique to each tool:", f"{unique[method]:,}", f"({100 * unique[method] / total[method]:.1f}%)")
    print("Ortholog pair predictions shared by all four tools:", f"{shared_all:,}")
