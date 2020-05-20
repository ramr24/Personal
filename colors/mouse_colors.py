import os
import collections
from temp_funcs import read_file

path = "C:/Users/kumar/Documents/Github/analysis_projects/"
csv_path = os.path.join(path, "csv/")
path_shiny_mouse = os.path.join(csv_path, "shiny_mouse_ctx.csv")

fields_shiny = ["cell_name_label", 
                "cluster_label", "cluster_color",
                "seurat_cluster_label", "seurat_cluster_color",
                "topLeaf_label", "topLeaf_color"]
shiny_mouse = read_file(path_shiny_mouse, fields_shiny)

def mouse_dictionary(option, df=shiny_mouse):
    if option == "c":
        cluster_dict = dict(zip(df["cluster_label"], df["cluster_color"]))
        cluster_dict = collections.OrderedDict(sorted(cluster_dict.items()))
        
        list_keys = list(cluster_dict.keys())
        for key in list_keys:
            if key.startswith("n"):
                cluster_dict.pop(key)
        return cluster_dict
    
    elif option == "s":
        seurat_dict = dict(zip(df["seurat_cluster_label"], df["seurat_cluster_color"]))
        seurat_dict = collections.OrderedDict(sorted(seurat_dict.items()))
        return seurat_dict
    
    elif option == "t":
        topLeaf_dict = dict(zip(df["topLeaf_label"], df["topLeaf_color"]))
        topLeaf_dict = collections.OrderedDict(sorted(topLeaf_dict.items()))
        return topLeaf_dict
    
    else:
        print("Please enter c, s, or t")


"""
cluster = pd.DataFrame(list(cluster_dict.items()),columns = ["cluster_label","cluster_color"])
seurat = pd.DataFrame(list(seurat_dict.items()),columns = ["seurat_cluster_label","seurat_cluster_color"])
topLeaf = pd.DataFrame(list(topLeaf_dict.items()),columns = ["topLeaf_label", "topLeaf_color"])

writer = pd.ExcelWriter(excel_path + "shiny_mouse_colors_dict.xlsx")
cluster.to_excel(writer, "cluster_label", freeze_panes=(1,0), index=False)
seurat.to_excel(writer, "seurat_cluster_label", freeze_panes=(1,0), index=False)
topLeaf.to_excel(writer, "topLeaf_label", freeze_panes=(1,0), index=False)
writer.save()
"""