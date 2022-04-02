class Presets(object):
    WELCOME = "<b>Merhaba.. {}</b>\n\n<i>Ben basit bir sesli botum. Sihri görmek için bana herhangi bir ses veya metin gönder." \
              " Benim hakkımda daha fazla bilgi için deneyin</i> /help .\n\n<b>Credits:</b><a href='https://github.com/01-Meyitzade-01'>" \
              "<b> meyitzade</b></a>"
    HELP = "<b><u>Summary:</u></b>\n<i>Bu bot, sesinizi çeşitli dillerde metne çevirebilir. Ayrıca " \
           "metinden konuşmaya da çeşitli dillerde destekler. Bu bot uzun sesi de çevirebilir " \
           "klipleri metne çevirir.\n\n<b><u>Kullanım:</u></b>\n🔰 Sesinizi metne çevirmek için dili seçmeniz yeterlidir " \
           "<a href='t.me/{}?start=start'>listesinden</a> bir şey söyleyin. Veya herhangi bir ses klibini doğrudan iletin " \
           "bota. Dillerden herhangi birini seçmediyseniz, bot varsayılan olarak Türkçe TR'yi atayacaktır. " \
           "çeviri için dil.\n\n🔰 Bot'a kısa mesaj gönderin. Çevirmek için gerekli dili seçin " \
           "it. You'll receive the voice clip for the corresponding text.</i>\n\n<b>®️Credits:</b><a " \
           "href='https://github.com/01-Meyitzade-01'><b> meyitzade</b></a> "
    PROCESSING = "<i>İşleniyor..</i>"
    CHANGE_LANG_TXT = "<i>Lütfen gerekli dili seçin.</i>"
    DOWNLOADING = "<i>sesini indiriyor..</i>"
    CONVERTING = "<i>sesinizi dönüştürme..</i>"
    CHUNK_ERROR = "<b>Sesiniz dönüştürülürken bazı bilinmeyen hatalar oluştu. neyse bitmiş halini göndereyim " \
                  "metinler. Rahatsızlıktan dolayı üzgünüz.</b> 🥵"
    ERROR_CONVERTING = "<i>Sesiniz dönüştürülürken hata oluştu..</i>"
    ERROR_FILE = "<b>Hata!</b>\n\n<i>Bu ses dönüştürülemez</i>"
    LONG_FILE = "🧐 <b><u>Hmm.. Uzun ses</u></b>\n\n<i>Dönüştürmeye çalışalım..</i>"
    CHUNK_TXT = "<i>Sesten metin oluşturma: {}</i>"
    FINISHED = "<i>ses tanıma bitti. !</i>"
    READ_TEXT = "<i>text.q'yi tanıma.. </i>"
    DECODED_TEXT = "<b><u>Decoded text:</u></b>\n<i>--Tap the text to copy--</i>\n\n<code>{}</code>\n\n" \
                   "<b>Credits:</b><a href='https://github.com/01-Meyitzade-01'><b> meyitzade</b></a>"
    DECODED_LONG_TEXT = "<b><u>Decoded text:</u></b>\n\n<code>{}</code>\n\n" \
                        "<b>Credits:</b><a href='https://github.com/01-Meyitzade-01'><b> Meyitzade</b></a>"
    ERROR_DECODE = "<b>Error!</b>\n\n<i>This audio cannot be able to decode</i>"
    LANGUAGE_SELECT_MSG = "Selected Language: {}"
    TEXT_TO_VOICE = "<b>Select the accent to convert:</b>"
    CONV_TO_VOICE = "<i>Converting your text to voice..</i>"
    GEN_VOICE = "<i>Generating the voice..</i>"
    VOICE_UPLOADED = "<i>Uploading the voice..Plz wait</i>"
    VOICE_CAPTION = "<b>Credits:</b><a href='https://github.com/01-Meyitzade-01'><b> Meyitzade</b></a>"
    A2T_REPORT = "<b><u>Intimation:</u></b>\n\n<i>Audio to Text conversion</i>\nby: {}"
    T2A_REPORT = "<b><u>Intimation:</u></b>\n\n<i>Text to Audio conversion</i>\nby: {}"
