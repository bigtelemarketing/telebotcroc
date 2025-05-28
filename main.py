import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from datetime import datetime

BOT_TOKEN = '7996855061:AAFz6yh7CDhtRIRkhA0vSXjBJkcTIOBHXrE'
CHANNEL_USERNAME = '@consulenteperilrisparmio'

# Categorie promozionali
categorie = {
    "📱 Offerte SIM Mobile": [
        {
            "titolo": "TIM Power 50GB a 7,99€",
            "link": "https://www.bigtelemarketing.com/offerte/tim-power",
            "note": "Minuti, SMS illimitati e 50GB"
        },
        {
            "titolo": "Vodafone Special 100GB a 9,99€",
            "link": "https://www.bigtelemarketing.com/offerte/vodafone-special",
            "note": "Per clienti Iliad e virtuali"
        }
    ],
    "🏠 Internet Casa": [
        {
            "titolo": "Fastweb Fibra 2.5Gbps a 22,95€/mese",
            "link": "https://www.bigtelemarketing.com/offerte/fastweb-casa",
            "note": "Router incluso - attivazione gratuita"
        },
        {
            "titolo": "TIM Premium Fibra 24,90€",
            "link": "https://www.bigtelemarketing.com/offerte/tim-fibra",
            "note": "Velocità fino a 1Gbps"
        }
    ],
    "📦 Smartphone a Rate": [
        {
            "titolo": "iPhone 13 128GB con WindTre a 19,99€/mese",
            "link": "https://www.bigtelemarketing.com/rate/smartphone-windtre",
            "note": "Con offerta mobile attiva"
        }
    ],
    "⚡ Luce & Gas": [
        {
            "titolo": "Enel Energia Tutto Compreso a 85€/mese",
            "link": "https://www.bigtelemarketing.com/energia/enel",
            "note": "Luce + Gas flat - IVA inclusa"
        },
        {
            "titolo": "Iren Revolution Luce a 0,12€/kWh",
            "link": "https://www.bigtelemarketing.com/energia/iren",
            "note": "Offerta variabile con bonus"
        }
    ],
    "🛒 Offerte dallo Shop": [
        {
            "titolo": "Smart TV VOV 32'' HD Android",
            "link": "https://www.bigtelemarketing.com/shop/p/smart-tv-vov-32",
            "note": "Solo 109,99€ invece di 149,99€"
        },
        {
            "titolo": "Macchina Caffè Faber a Cialde",
            "link": "https://www.bigtelemarketing.com/shop/p/macchina-caffe-faber",
            "note": "In offerta a 109,99€"
        },
        {
            "titolo": "Xiaomi Redmi 14C 8+256GB",
            "link": "https://www.bigtelemarketing.com/shop/p/xiaomi-redmi-14c",
            "note": "Promo a 99,99€"
        }
    ]
}

async def invia_telegram():
    bot = Bot(BOT_TOKEN)
    for categoria, offerte in categorie.items():
        for offerta in offerte:
            testo = (
                f"*{categoria}*\n\n"
                f"🔹 {offerta['titolo']}\n"
                f"📌 {offerta['note']}\n"
                f"🔗 [Scopri di più]({offerta['link']})\n\n"
                f"🕒 Offerta aggiornata al {datetime.now().strftime('%d/%m/%Y %H:%M')}"
            )
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💬 WhatsApp", url="https://wa.me/393511937470")],
                [InlineKeyboardButton("🌐 Visita il sito", url="https://www.bigtelemarketing.com")]
            ])
            await bot.send_message(
                chat_id=CHANNEL_USERNAME,
                text=testo,
                reply_markup=keyboard,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )

if __name__ == "__main__":
    asyncio.run(invia_telegram())
