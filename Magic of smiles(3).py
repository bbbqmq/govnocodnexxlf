__version__ = (0, 0, 4)

#meta developer: @bbbqmq_govnocoder

from .. import loader
from asyncio import sleep


@loader.tds
class HeartsMod(loader.Module):
    strings = {"name": "Magic of smiles"}
    """Анимации из эмоджи"""

    @loader.owner
    async def heartscmd(self, message):
        for _ in range(10):
            for heart in ["❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "💝", "💖", "💗", "💓", "💞", "💕", "💟", "💘", "❣️", "❤️‍🔥"]:
                await message.edit(heart)
                await sleep(0.3)

    async def moonscmd(self, message):
        for _ in range(10):
            for moon in ["🌝", "🌚"]:
                await message.edit(moon)
                await sleep(0.3)

    async def moons2cmd(self, message):
        for _ in range(10):
            for moon2 in ["🌕", "🌖", "🌗", "🌘", "🌑", "🌒", "🌓", "🌔"]:
                await message.edit(moon2)
                await sleep(0.3)
                
    async def earthcmd(self, message):
        for _ in range(10):
            for earth in ["🌎", "🌍", "🌏",]:
                await message.edit(earth)
                await sleep(0.3)
                
    async def hikka2cmd(self, message):
        for _ in range(10):
            for hikka2 in ["🌕 Hikka 🌕", "🌖 Hikka 🌖", "🌗 Hikka 🌗", "🌘 Hikka 🌘", "🌑 Hikka 🌑", "🌒 Hikka 🌒", "🌓 Hikka 🌓", "🌔 Hikka 🌔",]:
                await message.edit(hikka2)
                await sleep(0.3)
                
    async def photocmd(self, message):
        for _ in range(1):
            for photo in ["📷", "📸", "📷", "🤡 <b>Узнал себя?</b>"]:
                await message.edit(photo)
                await sleep(1)

    async def clockscmd(self, message):
        for _ in range(12):
            for clock in ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]:
                await message.edit(clock)
                await sleep(0.3)

    async def policecmd(self, message):
        for _ in range(12):
            for police in [
                "🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵\n🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵\n🔴🔴🔴🔴⬜️⬜️⬜️🔵🔵🔵🔵",
                "🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴\n🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴\n🔵🔵🔵🔵⬜️⬜️⬜️🔴🔴🔴🔴",
            ]:
                await message.edit(police)
                await sleep(0.3)