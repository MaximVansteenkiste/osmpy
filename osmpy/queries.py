import pandas as pd

class QueryType:

    def postprocess(self, df):
        return df

# class POIs(osmpy.queries.QueryType):

#     query = """
#         [out:json];
#         node["shop"](poly:"{boundary}");
#         node["amenity"](poly:"{boundary}");
#         out body geom;
#     """

#     docstring = """
#     Location of Points of Interest within a boundary. 
#     Points of Interest being all shops and amenities.
#     """
    
#     def prep_pois(x):
    
#         if x.get('amenity'):
#             return f'amenity:{x["amenity"]}'
#         elif x.get('shop'):
#             return f'shop:{x["shop"]}'
#         else:
#             return None

#     def postprocess(self, df):
#         """Post process API result
#         """
#         df['poi'] = df['tags'].apply(prep_pois)
        
#         return df

class Amenities(QueryType):

    query = """
    [out:json];
    node["amenity"](poly:"{boundary}");
    out body geom;
    """

    docstring = """
    Location of amenities within a boundary
    """

    def postprocess(self, df):
        return df

class AmentiesCount(QueryType):

    query = """
    [out:json];
    node["amenity"](poly:"{boundary}");
    for (t["amenity"])
    {{
       make stat amenity=_.val,
           count=count(nodes);
       out;
    }}
    """

    docstring = """
    Number of amenities per type within a boundary
    """

    def postprocess(self, df):
        return df['tags'].apply(pd.Series).groupby('amenity').sum()

class RoadLength(QueryType):

    query = """
    [out:json];
    way["highway"](poly:"{boundary}");
    for (t["highway"])
    {{
       make stat highway=_.val,
           count=count(ways),length=sum(length());
       out;
    }}"""

    docstring = """
    Length of road by roadtype within a boundary
    """

    def postprocess(self, df):
        return df['tags'].apply(pd.Series).groupby('highway').sum()
