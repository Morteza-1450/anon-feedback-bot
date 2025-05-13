from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

# دریافت توکن و آی‌دی از متغیرهای محیطی
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=f"📩 پیام ناشناس:\n{msg}")
    await update.message.reply_text("✅ پیام شما ناشناس برای مدیر ارسال شد.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
app.run_polling()
