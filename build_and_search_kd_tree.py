# Node definition for 2D K-d tree
class Node2D:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None

# Function to build 2D K-d tree
def build_kd_tree(points, depth=0):
    if not points:
        return None

    k = len(points[0])  # Dimension of the points, k=2 for 2D
    axis = depth % k

    sorted_points = sorted(points, key=lambda point: point[axis])

    mid = len(sorted_points) // 2
    node = Node2D(sorted_points[mid])
    node.left = build_kd_tree(sorted_points[:mid], depth + 1)
    node.right = build_kd_tree(sorted_points[mid + 1:], depth + 1)

    return node

# Data points for 2D K-d tree construction
#data_points = [(51, 75), (25, 40), (10, 30), (1, 10), (35, 90), (50, 50), (70, 70), (55, 1), (60, 80)]
#data_points = [(51, 75), (25, 40),(70, 70), (10, 30), (35, 90),(55, 1), (60,80), (1, 10),(50, 50)]
data_points =[
    (51, 75),   # Root node
    (25, 40),   # Left child of the root
    (70, 70),   # Right child of the root
    (10, 30),   # Left child of (25, 40)
    (35, 90),   # Right child of (10, 30)
    (60, 80),   # Right child of (70, 70)
    (1, 10),    # Left child of (35, 90)
    (55, 1),    # Left child of (60, 80)
]
# Build the 2D K-d tree
root_node = build_kd_tree(data_points)

# Now, the 'root_node' represents the root of the constructed 2D K-d tree.

# Function to print 2D K-d tree with ASCII art
def print_kd_tree_ascii(node, depth=0, prefix="Root: "):
    if node is None:
        return

    k = len(node.point)
    axis = depth % k

    # Print the current node
    print(" " * (depth * 4) + prefix + f"{node.point}")

    # Recursively print the left subtree
    print_kd_tree_ascii(node.left, depth + 1, "Left:  ")

    # Recursively print the right subtree
    print_kd_tree_ascii(node.right, depth + 1, "Right: ")


print_kd_tree_ascii(root_node)




# Function to calculate Euclidean distance between two K-dimensional points
def calculate_euclidean_distance_KD(point1, point2):
    return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5

# Recursive function to find K-dimensional points within the radius R
def find_points_within_radius_KD(node, query_point, R, depth=0):
    if node is None:
        return []

    distance = calculate_euclidean_distance_KD(node.point, query_point)
    result_list = []

    if distance <= R:
        result_list.append(node.point)

    k = len(query_point)
    dim = depth % k

    if node.point[dim] >= query_point[dim] - R:
        result_list.extend(find_points_within_radius_KD(node.left, query_point, R, depth + 1))

    if node.point[dim] <=  query_point[dim] + R:
        result_list.extend(find_points_within_radius_KD(node.right, query_point, R, depth + 1))

    return result_list

# Usage example for K-dimensional points:
query_point = (25,65) #q_x1, q_x2, q_x3, ..., q_xK)  # K-dimensional query point
R = 25  # Given radius R

result_list = find_points_within_radius_KD(root_node, query_point, R)
print(R)
print(result_list)
print([calculate_euclidean_distance_KD(node, query_point) for node in result_list])
R=30
result_list = find_points_within_radius_KD(root_node, query_point, R)
print(R)
print(result_list)
print([calculate_euclidean_distance_KD(node, query_point) for node in result_list])
R=40
result_list = find_points_within_radius_KD(root_node, query_point, R)
print(R)
print(result_list)
print([calculate_euclidean_distance_KD(node, query_point) for node in result_list])
R=50
result_list = find_points_within_radius_KD(root_node, query_point, R)
print(R)
print(result_list)
print([calculate_euclidean_distance_KD(node, query_point) for node in result_list])
