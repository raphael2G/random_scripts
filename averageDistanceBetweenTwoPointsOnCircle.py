# Let S be a spherical shell of radius 1, i.e., the set of points satisfying 
# x^2 + y^2 + z^2 = 1
# Find the average straight line distance between two points on S


import numpy as np

def random_point_on_sphere():
    # Generate random points on a unit sphere using spherical coordinates
    phi = np.random.uniform(0, 2 * np.pi)  # Azimuthal angle (longitude)
    cos_theta = np.random.uniform(-1, 1)   # Uniform in cosine of polar angle
    theta = np.arccos(cos_theta)           # Polar angle (latitude)
    
    # Convert spherical coordinates to Cartesian coordinates
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    
    return np.array([x, y, z])

def straight_line_distance(p1, p2):
    # Calculate the straight-line distance between two points on the unit sphere
    return np.linalg.norm(p1 - p2)

def mean_distance_on_sphere(num_pairs=100000):
    total_distance = 0.0
    
    for _ in range(num_pairs):
        # Generate two random points on the sphere
        p1 = random_point_on_sphere()
        p2 = random_point_on_sphere()
        
        # Calculate the straight-line distance between them
        distance = straight_line_distance(p1, p2)
        
        # Accumulate the total distance
        total_distance += distance
    
    # Compute the mean distance
    mean_distance = total_distance / num_pairs
    return mean_distance

# Example usage
mean_distance = mean_distance_on_sphere()
print(f"Mean straight-line distance between two random points on a unit sphere: {mean_distance}")
