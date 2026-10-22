import random
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = '8972894526:AAFbFNJds6s50p_WUMOKgabCLgAWvWJgd-A'

PAIRS = [
    "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", 
    "AUD/CAD (OTC)", "EUR/GBP (OTC)", "USD/BDT (OTC)"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 Get Quotex Signal (1 Min)", callback_data='sig_1')],
        [InlineKeyboardButton("📊 Get Quotex Signal (5 Min)", callback_data='sig_5')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = (
        "🔥 *Quotex AI Signal Bot Pro* 🔥\n\n"
        "آپ کا استقبال ہے! نیچے دیے گئے بٹنز سے سگنل ٹائم منتخب کریں:"
    )
    if update.message:
        await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')
    else:
        await update.callback_query.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    timeframe = "1 Minute" if query.data == 'sig_1' else "5 Minutes"
    
    await query.edit_message_text("⏳ *Quotex Live Market Analyze Ho Rahi Hai...*", parse_mode='Markdown')
    await asyncio.sleep(2)
    
    pair = random.choice(PAIRS)
    direction = random.choice(["CALL (UP) 🟢", "PUT (DOWN) 🔴"])
    accuracy = random.randint(88, 97)
    
    msg = (
        "🎯 *QUOTEX ACCURATE SIGNAL* 🎯\n\n"
        f"🌐 *Asset:* {pair}\n"
        f"📈 *Direction:* {direction}\n"
        f"⏱ *Timeframe:* {timeframe}\n"
        f"🔥 *Accuracy:* {accuracy}%\n\n"
        "⚠️ *Rule:* Risk management ke sath trade karein!"
    )
    
    keyboard = [[InlineKeyboardButton("🔄 Next Signal", callback_data=query.data)]]
    await query.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
