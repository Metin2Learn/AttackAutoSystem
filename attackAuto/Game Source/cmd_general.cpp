ACMD(do_guildskillup)  arat altýna ekle ;


ACMD(do_otomatikav_komut1)
{
	ch->AggregateMonster();
}

ACMD(do_otomatikav_komut2)
{
	if (ch->CountSpecifyItem(20171) == 0 && ch->CountSpecifyItem(20172) == 0)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "|cFF00FF00|H|h[Sistem] : Otomatik Av Calistirman ?cin Gerekli Nesne Yok");
		return;
	}
	ch->ChatPacket(CHAT_TYPE_COMMAND, "OtomatikAvWindow");
}