from shapely import geometry
import matplotlib.pyplot as plt
import geopandas as gpd


#%%
p_1 = geometry.Point(-118.4152, 33.9699)
p_2 = geometry.Point(-118.4152,33.9689)
p_3 = geometry.Point(-118.4144,33.9689)
p_4 = geometry.Point(-118.4142,33.96990)
p_5 = geometry.Point(-118.4152,33.9699)
pointList = [p_1, p_2, p_3, p_4, p_5]
poly = geometry.Polygon(pointList)

#%%
x,y = poly.exterior.xy
plt.plot(x,y)
plt.show()

#%%
centroid_polygon = poly.centroid
print(centroid_polygon)
bound_box = poly.bounds
print(bound_box)

#%%

(minx, miny, maxx, maxy) = bound_box
fig, ax = plt.subplots()
rect = plt.Rectangle((minx, miny), width = (maxx-minx), height = (maxy-miny), fill=False, edgecolor = 'pink',lw=5)
ax.add_patch(rect)

x,y = poly.exterior.xy
plt.plot(x,y)
plt.show()

#%%
fp = "Justice_Equity_Need_Index.geojson"
df = gpd.read_file(fp)
print(df.crs)

#%%
print(df.size)
#%%
print(df.shape)
#%%
columns = df.columns
print(columns)
#%%
df.head(10)
#%%
df_copy = df.copy
#%%
data_projected = df.to_crs("EPSG:3857")
#%%
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 8))
#%%
df.plot(ax=ax1, facecolor='gray')
#%%
crs_df = df.crs
#%%
ax1.set_title(crs_df)
#%%
data_projected.plot(ax=ax2, facecolor='blue')
#%%
ax2.set_title("EPSG:3857")
plt.tight_layout()
plt.show()

