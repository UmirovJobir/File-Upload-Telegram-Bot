
from telegram.update import Update
from telegram.ext import CallbackContext, MessageHandler, Updater, CommandHandler, ConversationHandler, Filters
import settings

STATE_BEGIN = 1

def start(update:Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum! Fayllarni saqlobchi botga xush kelibsiz!\n"
                                "File yuboring")

    return STATE_BEGIN

def uploade_doc(update:Update, context:CallbackContext):
        update.message.reply_text("Assalomu alaykum!")

        print(update.message)
        # delete_message(qu=update, context=context)
        # update.message.reply_html(f"⏳ {orl.translate(key='kutib_turing_fayl_yuklanmoqda', k=kalit)}")
        #update.message.reply_html(f"{update.message}")

        #file_id
        # if update.message.photo:
        #     file_id = update.message.photo[-1].file_id
        #     newf = update.message.effective_attachment[-1].get_file()
        # elif update.message.document:
        #     file_id = update.message['document']['file_id']
        #     newf = update.message.effective_attachment.get_file()
        # try:
        #     p = context.bot.get_file(file_id)
        #     filename, file_extension = os.path.splitext(p.file_path)  # Faylni kengaytmasi va nomini aniqlash
        #     newf.download(f'resume/resume/{file_id}{file_extension}')
        #     context.chat_data.update({f'{update.message.chat_id}_file': f'{file_id}{file_extension}'})
        #     update.message.reply_html(f"{orl.translate(key='test_tekst', k = kalit)}",reply_markup=buttons(k=kalit).resend_resume_start_test())

#fileni id si va kengaytmasini bazaga saqlash kerak

        # except BaseException as e:
        #     update.message.reply_html(f"{orl.translate(key='faylni_tugri_yuboring', k=kalit)}")

updater = Updater(token=settings.TOKEN)
dispatcher = updater.dispatcher
updater.dispatcher.add_handler(CommandHandler('start', start))

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        STATE_BEGIN:[
            MessageHandler(Filters.all, uploade_doc)],
    },
    fallbacks=[]
)

updater.start_polling()
updater.idle()