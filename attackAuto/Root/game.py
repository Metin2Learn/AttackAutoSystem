"CloseRestartWindow"	: self.__RestartDialog_Close,  arat alt�na ekle

"OtomatikAvWindow"		: self.__otomatikavstart,


def __RestartDialog_Close(self):  arat alt�na ekle ;

	def __otomatikavstart(self):
		ahmetatalayInfo.Start = 1


self.guildScoreCounter = guildwarkillcounter.MessageQueue()   arat�l�r alt�ndaki self.itemDropQuestionDialog = None  alt�na eklenir.

self.otomatikavpelerin = 0


def OnUpdate(self):  arat�l�r ,  if self.enableXMasBoom:   den sonra eklenir ;


#Coded By Ahmet Atalay
		self.otomatikavpelerin += 1
		if self.otomatikavpelerin == 400:
			otopelerin = app.GetRandom(1,2)
			if 1 == ahmetatalayInfo.Pelerin:
				if otopelerin == 1:
					net.SendChatPacket("/otomatikav_komut1")
				elif otopelerin == 2:
					net.SendChatPacket("/otomatikav_komut1")
			self.otomatikavpelerin = 0
#Coded By Ahmet Atalay