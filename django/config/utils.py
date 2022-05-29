from geoserver.geoserver import create_layer_with_store , get_or_create_workspace
from django.conf import settings
import os


class LayerAdd():
    def __init__(self , filename, filepath):
        # self.workspace = get_or_create_workspace()
        self.layer_name = filename.split('.')[0]
        self.store_name = self.layer_name
        self.path = settings.GEOSERVER.get('DATA_URL')
        self.url = os.path.join(self.path , filepath , filename)
        self.layer = None

    def tif_add(self):
        self.layer = create_layer_with_store(data_type='tif' , url=self.url , layer_name=self.layer_name , store_name=self.store_name )
        return self.layer

    def jp2_add(self):
        pass
    def shp_add(self):
        self.layer = create_layer_with_store(data_type='shp' , url=self.url , layer_name = self.layer_name , store_name=self.store_name )