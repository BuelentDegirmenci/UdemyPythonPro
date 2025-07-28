input_file = "py311_packages.txt"
output_file = "requirements_cleaned.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if not line.startswith("#") and line.strip():
            parts = line.split()
            if len(parts) >= 2:
                pkg = parts[0]
                ver = parts[1]
                outfile.write(f"{pkg}=={ver}\n")

print(f"✓ Converted to pip format: {output_file}")
