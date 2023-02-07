def delete_atoms(file_name, shape, radius_x, radius_y):
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

        # Check if the position is inside the shape
        if shape == "circle":
            if x**2 + y**2 >= radius_x**2:
                delete_list.append(i + 1)
        elif shape == "ellipse":
            if x**2/radius_x**2 + y**2/radius_y**2 >= 1:
                delete_list.append(i + 1)

    # Create a new file to store the results
    with open("new_structure.data", "w") as f:
        # Copy the header lines from the original file
        for line in lines[:9]:
            f.write(line)

        # Loop through the atoms
        count = 0
        for i in range(n_atoms):
            # If the current atom is not in the delete list, write it to the new file
            if i + 1 not in delete_list:
                f.write(lines[9 + i])
                count += 1

    # Update the number of atoms in the new file
    with open("new_structure.data", "r") as f:
        lines = f.readlines()
    lines[3] = str(count) + " atoms\n"
    with open("new_structure.data", "w") as f:
        f.writelines(lines)

# Example usage
delete_atoms("structure.data", "ellipse", 2, 1)
