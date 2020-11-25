

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'\n{self.x}, {self.y}, {self.z}\n'
        
        
class Line:

    def __init__(self, point1:Point, point2:Point):
        self.point1 = point1
        self.point2 = point2
        
    def get_direct_vector(self) -> Point:

        return Point(self.point2.x - self.point1.x, self.point2.y - self.point1.y, self.point2.z - self.point1.z)
        
        
class Sphere:

    def __init__(self, center:Point, radius:float):
        self.center = center
        self.radius = radius

def get_quadratic_equation_coefficients(line:Line, sphere:Sphere) -> list:
    
    dv = line.get_direct_vector()
    pt = line.point1

    c = sphere.center
    r = sphere.radius
    
    a = dv.x ** 2 + dv.y ** 2 + dv.z ** 2 
    b = 2 * ((pt.x - c.x) * dv.x + (pt.y - c.y) * dv.y + (pt.z - c.z) * dv.z)
    c = (pt.x - c.x) ** 2 + (pt.y - c.y) ** 2 + (pt.z - c.z) ** 2 - r ** 2
    
    return [a, b, c]

def find_collision_point(line:Line, t:float) -> Point:

        pt = line.point1
        dv = line.get_direct_vector()

        x = pt.x + t * dv.x
        y = pt.y + t * dv.y
        z = pt.z + t * dv.z

        return Point(x, y, z)

def solve_quadratic_equation(a, b, c) -> list:

    desc = b ** 2 - 4 * a * c
    
    if desc < 0:
        return []
    
    if desc == 0:
        x = -b / (2 * a)
        return [x] 
    
    x1 = (-b - desc ** 0.5) / (2 * a)
    x2 = (-b + desc ** 0.5) / (2 * a)
    
    return [x1, x2] 

def find_sphere_line_collision(line:Line, sphere:Sphere):

    a, b, c = get_quadratic_equation_coefficients(line, sphere)

    ans = solve_quadratic_equation(a, b, c)

    if len(ans) == 1:
        t = ans[0]

        point = find_collision_point(line, t)
        return f'{point.__str__()}'

    if len(ans) == 2:
        t1, t2 = ans
        
        point_one = find_collision_point(line, t1)
        point_two = find_collision_point(line, t2)
        
        return f'{point_one.__str__()}{point_two.__str__()}'

    return 'Коллизий не найдено'
    
def convert_source_to_dict(source_string:str) -> dict:
    """ Function conver str object like

        '{sphere: {center: [0, 0, 0], radius: 10.67}, line: {[1, 0.5, 15], [43, -14.6, 0.04]}}'

        to dict object like

        {'sphere': {'center': [0.0, 0.0, 0.0], 'radius': 10.67}, 'line': {'point1': [1.0, 0.5, 15.0], 'point2': [43.0, -14.6, 0.04]}}
    """
    source = source_string.split('}')
    for sep in ('{', ':', '[', ']', ',', ' '):
        source = ''.join(source).split(sep)
    
    objects = []
    for el, cnt in (('radius', 2), ('center', 4), ('line', 7)):
        i = source.index(el)
        objects.append([float(x) for x in source[i + 1 : i + cnt]])
        
    radius, center, line = objects
    point1, point2 = line[:3], line[3:]
    
    return {'sphere': {'center': center, 'radius': radius[0]}, 'line': {'point1': point1, 'point2': point2}}
   
def main():
    
    file_name = sys.argv[1]
    
    try:
        f = open(file_name, 'r')
        f.close()
    except:
        print("Не удалось открть файл")
    else:
        with open(file_name, 'r') as source_file:
            count = 0
            for line in source_file:
                count += 1
                line = line.strip().replace('\n','')
                if not line:
                    continue
                
                try:
                    source = convert_source_to_dict(line)
                except:
                    print(f'Строка {count}: некорректный формат данных')
                    print("""
Данные о сфере и линии должный иметь вид:

                    {sphere: {center: [0, 0, 0], radius: 10.67}, line: {[1, 0.5, 15], [43, -14.6, 0.04]}}
                        
Объекты и ключи могут находится в свободной последовательности. Соблюдайте расстановку пробельных символов внутри объектов.
""")

                else:
                    center_coordinates = source.get('sphere').get('center')
                    center = Point(*center_coordinates)
                    radius = source.get('sphere').get('radius')
                    sphere = Sphere(center, radius)
                    
                    point1_coordinates = source.get('line').get('point1')
                    point2_coordinates = source.get('line').get('point2')
                    point1 = Point(*point1_coordinates)
                    point2 = Point(*point2_coordinates)
                    line = Line(point1, point2)

                    print(find_sphere_line_collision(line, sphere))

            if count == 0:
                print("Файл пуст")

if __name__ == '__main__':

    import sys

    if len(sys.argv) != 2:
        print("""
Передайте имя файла с данными о сфере и линии в качестве аргумента командной строки, например: main.py main.txt.
        
Данные о сфере и линии должный иметь вид:

                    {sphere: {center: [0, 0, 0], radius: 10.67}, line: {[1, 0.5, 15], [43, -14.6, 0.04]}}
                        
Объекты и ключи могут находится в свободной последовательности. Соблюдайте расстановку пробельных символов внутри объектов.""")
    else:
        main()
    

    
