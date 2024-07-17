import os
import sys
sys.path.append('C:\\Users\\jorge\\Desktop\\Inicio\\UTH\\2024\\2-2024\\AVANZADA_II\\II_P\\ControladorReconocimientoFacial\\.venv\\Clases')

from Clases.Login import Login
from Clases.claseFigura import claseFiguras

figuras = claseFiguras()
login = Login()

booleana = False

booleana = login.facial()

if booleana == True or booleana == None:
    figuras.area()
else:
    figuras.volumen()
