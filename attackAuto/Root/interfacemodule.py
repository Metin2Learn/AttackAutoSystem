if uiTaskBar.TaskBar.IS_EXPANDED:  arat�l�r alt�na 


self.wndExpandedTaskBar.SetToggleButtonEvent(uiTaskBar.ExpandedTaskBar.BUTTON_OTOMATIK_AV, ui.__mem_func__(self.OtomatikAv))

eklenir


def ToggleInventoryWindow(self):  arat�l�r  

�st�ne eklenir

def OtomatikAv(self):
		import uiotomatikav
		self.otomatikav = uiotomatikav.otomatikav()
		self.otomatikav.Show()