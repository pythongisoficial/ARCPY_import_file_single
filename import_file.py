import arcpy

mxd=arcpy.mapping.MapDocument("CURRENT")

df=arcpy.mapping.ListDataFrames(mxd,"*")[0]

caminho_arquivo=r"D:\____data\__GitRepositorios\repositorios_pythongis\arcpy\import_files_arcpy\dados/limite.shp"

map_vect_obj=arcpy.mapping.Layer(caminho_arquivo)

arcpy.mapping.AddLayer(df,map_vect_obj,"BOTTOM")
