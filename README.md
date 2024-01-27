# packed-bed-void-fraction-
## Description

The method employed in this project is Monte Carlo-like, where n axial (or radial) planes are generated, each with x randomly generated points. The algorithm checks whether each point falls inside or outside the pallets.

### Usage

1. Use the OpenFOAM 'surfaceCheck' command on the stl file to obtain bed height and diameter.
2. Place the generated .obj files in the 'sandbox' folder.

### Output

The results are written to a file, where the first column contains axial (or radial) coordinates, and the second column contains the number of points that have fallen inside. This file is designed for easy graphical representation of the void fraction trend in the bed.

Feel free to explore and utilize the code for your projects!

