def delete_atoms(file_name, a, b, c):
    # Open the file
    with open(file_name, "r") as f:
        lines = f.readlines()

    # Get the number of atoms
    n_atoms = int(lines[3].strip().split()[0])

    # Initialize a list to store the indices of atoms to be deleted
    delete_list = []

    # Loop through the atoms to identify the ones to be deleted
    for i in range(n_atoms):
        # Get the current atom's position
        x, y, z = map(float, lines[9 + i].strip().split()[2:5])

        # Check if the position is inside the ellipsoid
        if (x / a)**2 + (y / b)**2 + (z / c)**2 > 1:
            delete_list.append(i + 1)

    # Create a new file to store the results
    with open("new_structure.data", "w") as f:
        # Copy the header lines from the original file
        for line in lines[:9]:
            f.write(line)

        # Loop through the atoms
        for i in range(n_atoms):
            # Check if the current atom is not in the delete list
            if i + 1 not in delete_list:
                f.write(lines[9 + i])

        # Update the number of atoms in the header
        n_atoms -= len(delete_list)
        f.seek(0)
        f.write(str(n_atoms) + "\n\n")

# Example usage
delete_atoms("structure.data", 1.0, 0.5, 0.5)
