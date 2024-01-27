import vtk
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
import os
import shutil


#Functions
def generate_random_assiale(n):
    r = np.random.uniform(1, 300**2, 10000)**0.5
    theta = np.random.uniform(0, 2*np.pi, n)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return list(zip(x, y))

def generate_random_radiale(n, r):
    theta = np.random.uniform(0, 2*np.pi, n)
    z = np.random.uniform(0, 695, n)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return list(zip(x, y, z))

def barycenter(polydata):
  points = polydata.GetPoints()
  n_points = points.GetNumberOfPoints()
  barycenter = [0.0, 0.0, 0.0]

  for i in range(n_points):
     p = [0.0, 0.0, 0.0]
     points.GetPoint(i, p)
     barycenter[0] += p[0]
     barycenter[1] += p[1]
     barycenter[2] += p[2]

  return [x / n_points for x in barycenter]


# Directory path where you want to search for .obj files
directory_path = 'sandbox_pellet_150'
os.makedirs(directory_path+'/selected')
# List to hold all .obj file paths
obj_files = []

# Walking through the directory
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith('.obj'):
            reader = vtk.vtkOBJReader()
            reader.SetFileName(os.path.join(root, file))
            reader.Update()
            
            polydata = reader.GetOutput()
            baricentro = barycenter(polydata)
            if(baricentro[-1]>700):
               continue
            enclosedPoints = vtk.vtkSelectEnclosedPoints()
            enclosedPoints.SetInputData(polydata)
            enclosedPoints.SetSurfaceData(polydata)
            enclosedPoints.SetTolerance(0.0001)
            enclosedPoints.CheckSurfaceOn()
            enclosedPoints.Update()
            obj_files.append(enclosedPoints)
            shutil.copy2(directory_path+'/'+file, directory_path+'/selected')

if sys.argv[1] == "assiale":
    xy = generate_random_assiale(10000)
   # x, y = zip(*xy)
   # plt.scatter(x, y, s=1)
   # plt.show()
    np.savetxt('point.csv', xy)
    in_point = 0
    out_point = 0

    with open('output_assiale.txt', 'w') as file:
        for z in np.linspace(0, 695, 100):
            in_point = 0
            out_point = 0
            for i, _ in enumerate(xy):
                for en in obj_files:
                    isInside = en.IsInsideSurface(xy[i][0], xy[i][1], z)
                    if isInside:
                        in_point += 1
                        break

            file.write(f'{z} {in_point}\n')

elif sys.argv[1] == "radiale":
    in_point = 0
    out_point = 0
    with open('output_radiale.txt', 'w') as file:
        for r in np.linspace(0, 300, 100):
            in_point = 0
            out_point = 0
            xyz = generate_random_radiale(10000, r)
            for i, _ in enumerate(xyz):
                for en in obj_files:
                    isInside = en.IsInsideSurface(xyz[i][0], xyz[i][1], xyz[i][2])
                    if isInside:
                        in_point += 1
                        break
            file.write(f'{r} {in_point}\n')






