#******************************************************************************************************
# Created: polygon.by        
# Last Updated: 30.04.2020
# Version: 2.0.0
#
# Authors:
# Dzmitry Ivanou
# Dzmitry Dzrynou
#
# Much thanks to Yury Ruskevich, CGCode Telegram Channel and Alexander Plechkov for some good ideas an support.
#
#******************************************************************************************************
# MODIFY THIS AT YOUR OWN RISK

from PySide2 import QtWidgets, QtCore, QtGui
import os
import sys
import MaxPlus

#add Paths
TempCurrentDir = os.path.dirname(__file__)
CurrentDir = TempCurrentDir.replace ("\\", "/")

#path to config file
TempPtModPath = (CurrentDir + "\\pt_modules")
PtModPath = TempPtModPath.replace ("\\", "/")

if CurrentDir not in sys.path:
  sys.path.append( CurrentDir )

if PtModPath not in sys.path:
  sys.path.append( PtModPath )

for i in range(len(sys.path)):
  TempSysPath =  sys.path[i]
  CorrectSysPath =  TempSysPath.replace ("\\", "/")
  if CorrectSysPath not in sys.path:
    sys.path.append( CorrectSysPath )
  #print sys.path[i]

#['C:\\Program Files\\Autodesk\\3ds Max 2018\\python27.zip', 'C:\\Program Files\\Autodesk\\3ds Max 2018\\python\\DLLs', 'C:\\Program Files\\Autodesk\\3ds Max 2018\\python\\lib', 'C:\\Program Files\\Autodesk\\3ds Max 2018\\python\\lib\\plat-win', 'C:\\Program Files\\Autodesk\\3ds Max 2018\\python\\lib\\lib-tk', 'C:\\Program Files\\Autodesk\\3ds Max 2018', 'C:\\Program Files\\Autodesk\\3ds Max 2018\\python', 'C:\\Program Files\\Autodesk\\3ds Max 2018\\python\\lib\\site-packages', 'C:/Users/d_ivanov/AppData/Local/Autodesk/3dsMax/2018 - 64bit/ENU/scripts/polygontools', 'C:/Users/d_ivanov/AppData/Local/Autodesk/3dsMax/2018 - 64bit/ENU/scripts/polygontools/pt_modules']  

import pt_gui as gui
reload(gui)

def main():    

    #get main win
    mainWindow = MaxPlus.GetQMaxMainWindow()

    #get ptgui widget
    dockWidgets = [x for x in mainWindow.children() if x.__class__.__name__ == 'PTGUI']
    
    ptdlg = None
    
    #if widget in array dont run - else run
    if (len(dockWidgets) > 0):
      ptdlg = dockWidgets[0]
      print '\n', "PolygonTools is Already Running.", '\n'
    else:	
      ptdlg = gui.PTGUI(parent=mainWindow)      
      print '\n', "PolygonTools Started!", '\n'

    #window properties
    ptdlg.setFloating(True)
    ptdlg.show()

if __name__ == '__main__':
	main()    
