arat�l�r.   -> class ExpandedTaskBar(ui.ScriptWindow):

alt k�sma eklenir   

BUTTON_OTOMATIK_AV = 3


arat�l�r : self.expandedTaskBarBoard = self.GetChild("ExpanedTaskBar_Board")

alt k�s�mda self.toggleButtonDict = {}  alt�na eklenir 


self.toggleButtonDict[ExpandedTaskBar.BUTTON_OTOMATIK_AV] = self.GetChild("AutoButton")
self.toggleButtonDict[ExpandedTaskBar.BUTTON_OTOMATIK_AV].SetParent(self)