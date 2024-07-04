import math

# Noktalarýn Tanýmlanmasý
points = [(1, 2), (4, 6), (7, 3), (10, 8)]

# Öklid Mesafesi Ýçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafelerin Hesaplanmasý
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunmasý
min_distance = min(distances)
print("Minimum distance:", min_distance)
