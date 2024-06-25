import math

# 1. Noktaların Tanımlanması: points adında, noktaları temsil eden bir liste oluşturduk.
points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma euclideanDistance fonksiyonu, iki nokta arasındaki Öklid mesafesini hesaplar.
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

#  3. Mesafelerin Hesaplanması distances adında bir liste oluşturarak, points listesindeki her nokta çifti arasındaki mesafeleri hesapladık ve bu listeye ekledik.
distances = []
for i in range(len(points)):
     for j in range(i + 1, len(points)):
         dist = euclideanDistance(points[i], points[j])
distances.append(dist)

# 4. Minimum Mesafenin Bulunması distances listesinden minimum mesafeyi bularak sonucu yazdırdık.
min_distance = min(distances)

# Sonuçların yazdırılması
print("Minimum mesafe:", min_distance)