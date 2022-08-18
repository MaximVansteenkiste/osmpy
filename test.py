import osmpy.core
from shapely import wkt

boundary = wkt.loads(
    'POLYGON((-46.63 -23.54,-46.6 -23.54,-46.62 -23.55,-46.63 -23.55,-46.63 -23.54))')
print(osmpy.core.get('RoadLength', boundary))
