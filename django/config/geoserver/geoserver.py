# from django.http.request import UploadHandlerList
import zipfile
import os , requests
from django.conf import settings
# base_dir = settings.BASE_DIR
from pathlib import Path
# import rasterio
from tifffile import tifffile


# get rest url
# get wms url

class Geoserver():
    # init parameters
    def __init__(self , filename , type) :
        # self.start = start
        # self.end = end
        self.filename = filename
        self.type = type

    def get_path(filename,tif_type):
        cwd = os.getcwd()
        path = Path(cwd)
        django_zamin_path = path.parent.absolute()
        # zamin_path = django_zamin_path.parent.absolute()
        path = os.path.join(django_zamin_path , 'fastapi' , 'images' , tif_type , filename)

        return path

    # make zip file
    def make_zip(path , filename , tif_type):
        #read the file with path 
        # with tifffile.imread(path) as input :
            filename_without_format = filename.split('.')[0]
            zip_file = zipfile.ZipFile(os.path.join(settings.BASE_DIR , 'images' , tif_type , filename_without_format+'.zip'), mode='w')
            print(path)
            # print(input)
            # print(type(input))

            # print(zip_file  )
            # print(type(input))

        
        # zipfile.Z

        #compress using zipfile

        #save using zip file in BASE,DIR
        
        # zip the tif file into a zip



        ### ()Unit Test #Remove the first tiff file
        # zip_save_path = os.path.join(settings.BASE_DIR , 'images' , tif_type)
        # zfile = filename
        # output = zipfile.ZipFile(path, 'w')
        # print(output)
        # output.write(zfile,zfile ,zipfile.ZIP_DEFLATED )
        # output.close()
        # zip_path = os.path.join(zip_save_path,filename)
        # return zip_path

    # make layer in geoserver
    def make_layer(zip_path,filename):
        # make the layer from zip
        headers_zip = {'content-type': 'application/zip'}
        workspace = 'nurc'
        coveragestore = 'worldImageSample'
        with open(zip_path , 'rb') as zip_file:
            r_create_layer = requests.put("http://localhost:8080/geoserver/rest/workspaces/" + workspace  + "/coveragestores/" + coveragestore  + filename  ,
                auth=('admin', '20672067'),
                data=zip_file,
                headers=headers_zip)
        return {"status_code" : 200}









    # get file 


    # make layer


    # make store




# filename is Tehran.tif    



import os
from .catalog import Catalog
from .workspace import Workspace
from .util import shapefile_and_friends
from django.conf import settings


def get_rest_url():
    return 'http://{}:{}/geoserver/rest'.format(
        settings.GEOSERVER.get('HOST'),
        settings.GEOSERVER.get('PORT')
    )


def get_wms_url(workspace=None, internal=False):
    if workspace is None:
        workspace = settings.GEOSERVER.get('WORKSPACE')

    if internal:
        return 'http://geoserver:8080/geoserver/{}/wms'.format(
            workspace,
        )

    return 'http://{}:{}/geoserver/{}/wms'.format(
        settings.GEOSERVER.get('IP'),
        settings.GEOSERVER.get('PORT'),
        workspace,
    )


def get_catalog():
    return Catalog(
        get_rest_url(),
        settings.GEOSERVER.get('USERNAME'),
        settings.GEOSERVER.get('PASSWORD')
    )


def get_or_create_workspace(name=None, namespace=None):
    if name is None:
        name = settings.GEOSERVER.get('WORKSPACE')
    if namespace is None:
        namespace = settings.GEOSERVER.get('NAMESPACE')

    cat = get_catalog()
    workspace = cat.get_workspace(name)

    if workspace is None:
        return cat.create_workspace(name, namespace)
    
    return workspace


def delete_workspace(name):
    cat = get_catalog()
    workspace = cat.get_workspace(name)
    
    if workspace is not None:
        cat.delete(workspace)


def exist_store(name, workspace=None, type=None):
    cat = get_catalog()
    store = cat.get_store(name, workspace)

    if store is None:
        return False
    
    if type is None:
        return True

    if store.type.lower() == type.lower():
        return True
    
    return False


def delete_store(name, workspace=None):
    cat = get_catalog()
    store = cat.get_store(name, workspace)
    
    if store is not None:
        cat.delete(store)


def get_number_of_stores():
    cat = get_catalog()
    stores = cat.get_stores()
    return len(stores)


def get_number_of_layers():
    cat = get_catalog()
    layers = cat.get_layers()
    return len(layers)


def get_layer(name, workspace=None):
    cat = get_catalog()

    if workspace is None:
        return cat.get_layer(name)
    
    if isinstance(workspace, Workspace):
        workspace = workspace.name

    return cat.get_layer(f'{workspace}:{name}')


def exist_layer(name, workspace=None):
    cat = get_catalog()
    layer = get_layer(name, workspace)
    
    if layer is None:
        return False
    
    return True


def delete_layer(name, workspace=None):
    cat = get_catalog()
    layer = get_layer(name, workspace)
    
    if layer is not None:
        cat.delete(layer)


def create_layer_with_store(data_type, **kwargs):
    # print('now we are in create_layer_with_store')
    # raise 'now we are in create_layer_with_store as alert'
    # return('ali')
    store_name = kwargs.get('store_name')
    workspace = kwargs.get('workspace')
    layer_name = kwargs.get('layer_name')
    # print('storename is '  , store_name)
    # print('workspace is ' , workspace)
    # print('layername is' , layer_name)

    cat = get_catalog()

    workspace = get_or_create_workspace(name=workspace)

    if store_name is None:
        store_name = f'store_{get_number_of_stores() + 1}'

    if layer_name is None:
        layer_name = f'layer_{get_number_of_layers() + 1}'

    if exist_layer(layer_name, workspace):
        raise 'There is input layer_name!'

    if data_type.lower() in ['shapefile', 'shp', 'esri_shapefile', 'esri', '.shp']:
        data = __get_data_store_as_shapefile(**kwargs)
        cat.create_featurestore(store_name, data, workspace)

    elif data_type.lower() in ['postgis', 'postgre', 'postgres', 'postgresql']:
        
        if exist_store(store_name, workspace, 'PostGIS'):
            store = cat.get_store(store_name, workspace)
        else:
            store = __create_postgis_store(store_name, workspace, **kwargs)
        
        crs = kwargs.get('crs')
        if crs is None:
            crs = 'EPSG:4326'

        __create_layer_from_postgis_store(store, layer_name, crs, kwargs.get('table_name'))

    elif data_type.lower() in ['geotiff', 'tif', 'tiff', 'geotif']:
        # print('create_layer_with_store called in tif')
        if exist_store(store_name, workspace):
            print( 'There is input store_name!')

        url = kwargs.get('url')
        if url is None:
            raise 'Parameter "url" is not specified.' # set Extention

        __create_layer_with_geotiff_store(store_name, workspace, layer_name, url)
        # layer_name = store_name # !!!!!!!!!


    else:
        raise f'type of {data_type} is not supported.\nValid types: shapefile, postgis, geotif' # set Exception

    cat.reload()
    return get_layer(layer_name, workspace)


def __create_postgis_store(store, workspace, **kwargs):
    cat = get_catalog()

    store = cat.create_datastore(store, workspace)
    __update_store_as_postgis(store, **kwargs)
    
    cat.save(store)
    return store


def __create_layer_from_postgis_store(store, layer_name, crs, table_name=None):
    cat = get_catalog()

    ft = cat.publish_featuretype(
        name=layer_name,
        store=store,
        native_crs=crs,
        native_name=table_name
        # jdbc_virtual_table = 
    )
    cat.save(ft)


def __create_layer_with_geotiff_store(store_name, workspace, layer_name, url):
    cat = get_catalog()
    # print('this one',url)
    store = cat.create_coveragestore(
        store_name,
        workspace, 
        path=url,
        create_layer=True,
        layer_name=layer_name,
        source_name=store_name,
        upload_data=True,
        type='GeoTIFF',
        contet_type="image/tiff"
    )
    cat.save(store)


def __get_data_store_as_shapefile(**kwargs):
    url = kwargs.get('url')

    if url is None:
        raise 'Parameter "url" is not specified.\nSupported files: .shp, .zip' # set Extention

    file_name, file_extension = os.path.splitext(url)

    if file_extension == '.shp':
        data = shapefile_and_friends(file_name)
    elif file_extension == '.zip':
        data = url
    else:
        raise 'Input "url" is not supported.\nSupported files: .shp, .zip' # set Extention
    
    return data


def __update_store_as_postgis(store, **kwargs):
    kwargs['dbtype'] = 'postgis'
    
    if kwargs.get('host') is None:
        kwargs['host'] = settings.POSTGRESQL.get('HOST')

    if kwargs.get('port') is None:
        kwargs['port'] = settings.POSTGRESQL.get('PORT')
    
    if kwargs.get('database') is None:
        kwargs['database'] = settings.POSTGRESQL.get('NAME')
    
    if kwargs.get('user') is None:
        kwargs['user'] = settings.POSTGRESQL.get('USER')
    
    if kwargs.get('passwd') is None:
        kwargs['passwd'] = settings.POSTGRESQL.get('PASSWORD')
    
    if kwargs.get('schema') is None:
        kwargs['schema'] = settings.POSTGRESQL.get('SCHEMA')

    if kwargs.get('Expose primary keys') is None:
        kwargs['Expose primary keys'] = 'false'

    if kwargs.get('max connections') is None:
        kwargs['max connections'] = 10

    if kwargs.get('min connections') is None:
        kwargs['min connections'] = 1

    if kwargs.get('fetch size') is None:
        kwargs['fetch size'] = 1000

    if kwargs.get('Batch insert size') is None:
        kwargs['Batch insert size'] = 1

    if kwargs.get('Connection timeout') is None:
        kwargs['Connection timeout'] = 20

    if kwargs.get('validate connections') is None:
        kwargs['validate connections'] = 'true'

    if kwargs.get('Test while idle') is None:
        kwargs['Test while idle'] = 'true'

    if kwargs.get('Evictor run periodicity') is None:
        kwargs['Evictor run periodicity'] = 300

    if kwargs.get('Max connection idle time') is None:
        kwargs['Max connection idle time'] = 300

    if kwargs.get('Evictor tests per run') is None:
        kwargs['Evictor tests per run'] = 3

    if kwargs.get('Primary key metadata table') is None:
        kwargs['Primary key metadata table'] = ''

    if kwargs.get('Session startup SQL') is None:
        kwargs['Session startup SQL'] = ''

    if kwargs.get('Session close-up SQL') is None:
        kwargs['Session close-up SQL'] = ''

    if kwargs.get('Callback factory') is None:
        kwargs['Callback factory'] = ''

    if kwargs.get('Loose bbox') is None:
        kwargs['Loose bbox'] = 'true'

    if kwargs.get('Estimated extends') is None:
        kwargs['Estimated extends'] = 'true'
    
    if kwargs.get('SSL mode') is None:
        kwargs['SSL mode'] = 'DISABLE'

    if kwargs.get('preparedStatements') is None:
        kwargs['preparedStatements'] = 'false'

    if kwargs.get('Max open prepared statements') is None:
        kwargs['Max open prepared statements'] = 50

    if kwargs.get('encode functions') is None:
        kwargs['encode functions'] = 'true'

    if kwargs.get('Support on the fly geometry simplification') is None:
        kwargs['Support on the fly geometry simplification'] = 'true'

    if kwargs.get('Method used to simplify geometries') is None:
        kwargs['Method used to simplify geometries'] = 'FAST'

    if kwargs.get('create database') is None:
        kwargs['create database'] = 'false'

    if kwargs.get('create database params') is None:
        kwargs['create database params'] = ''

    store.connection_parameters.update(**kwargs)


def get_number_of_styles():
    cat = get_catalog()
    layers = cat.get_styles()
    return len(layers)


def get_layer_style(name, workspace=None):
    lyr = get_layer(name, workspace)

    if lyr is not None:
        return lyr._get_default_style()


def create_style(style, name, workspace=None):
    cat = get_catalog()
    if workspace is None:
        workspace = get_or_create_workspace()

    cat.create_style(name, style, True, workspace)
    return cat.get_style(name, workspace)


def set_layer_style(style_name, lyr=None, name=None, workspace=None):
    if lyr is None:
        lyr = get_layer(name, workspace)

    if exist_layer(lyr.name):
        cat = get_catalog()
        style = get_style(style_name, workspace)

        lyr._set_default_style(style)
        cat.save(lyr)


def get_style(name, workspace=None):
    cat = get_catalog()
    return cat.get_style(name, workspace)
