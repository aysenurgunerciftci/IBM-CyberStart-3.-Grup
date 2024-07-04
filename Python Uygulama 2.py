import math

# Noktalar�n Tan�mlanmas�
points = [(1, 2), (4, 6), (7, 3), (10, 8)]

# �klid Mesafesi ��in Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafelerin Hesaplanmas�
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunmas�
min_distance = min(distances)
print("Minimum distance:", min_distance)
