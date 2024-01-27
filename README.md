# packed-bed-void-fraction-
The method is Monte Carlo-like, where n axial (or radial) planes are generated, each with x randomly generated points, and it is checked whether each point falls inside or outside the pallets.
Using the OpenFOAM 'surfaceCheck' command on the stl file to obtain bed height and diameter, as well as the .obj files to be placed in the 'sandbox' folder.
The output is written to a file, where the first column contains axial (or radial) coordinates, and the second column contains the number of points that have fallen inside. This file can be easily used to graphically represent the void fraction trend in the bed.
 
