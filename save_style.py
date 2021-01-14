'''
Este Script guardara estilos en formato .qml  en la ruta del proyecto 
'''
import os
proy = QgsProject.instance().fileName()
ruta = os.path.dirname(os.path.abspath(proy))
self=qgis.utils
layers = self.iface.mapCanvas().layers()

for layer in layers:
    layerType = layer.type()
    if layerType == QgsMapLayer.VectorLayer:
        name = layer.name()
        qml= ruta + '/'+str(name)+'.qml'
        if not os.path.isfile(qml):
            expand = 0
            while True:
                expand += 1
                new_qml = qml.split(".qml")[0] + str(expand) + ".qml"
                if os.path.isfile(new_qml):
                    continue
                else:
                    qml = new_qml
                    layer.saveNamedStyle(qml)
                    break
iface.messageBar().pushMessage("qgis", "Se guardo correctamente los estilos", level=Qgis.Info, duration=1)
