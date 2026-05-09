import bpy
import sys
arguments = sys.argv
filename = arguments[4]
fileType = filename.split('.')[-1].lower()
#clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
#import stl files, 
#Support for new (4.0.0) stl importer with check for older versions
if fileType == 'stl': 
    if bpy.app.version >= (4, 0, 0):
        bpy.ops.wm.stl_import(filepath=filename)
    else:
        bpy.ops.import_mesh.stl(filepath=filename)
elif fileType == 'obj':
    bpy.ops.import_scene.obj(filepath = filename)
elif fileType == 'dae':
    bpy.ops.wm.collada_import(filepath = filename)
else:
    for i in range(10):
        print('------------ invalid file type ------------')
