from pyrogram.emoji import *

class TEXT:
    DOWNLOAD_START = f"İndirme başlatılıyor ... {SLEEPING_FACE}"
    UPLOAD_START = f"Yükleme başlatılıyor... {SLEEPING_FACE}"
    UPLOAD_SUCESS = f"Beni kullandığın için teşekkürler :)"
    BANNED_USER_TEXT = f"Banlandın{FACE_WITH_TEARS_OF_JOY}."
    NOT_LOGGED_TEXT = f"This bot was only for private use {LOCKED_WITH_KEY}. If you want to use this bot you need to send me correct password in the format `/login bot_password`"
    SAVED_CUSTOM_THUMBNAIL = f"Resim kaydedildi.{NOTEBOOK_WITH_DECORATIVE_COVER}"
    DELETED_CUSTOM_THUMBNAIL = f"Resim başarıyla silindi. {CHECK_MARK_BUTTON}"
    NO_CUSTOM_THUMB_NAIL_FOUND = f"resim bulunamadı. {THUMBS_DOWN_LIGHT_SKIN_TONE}"
    THUMBNAIL_CAPTION = f"{BACKHAND_INDEX_POINTING_UP_LIGHT_SKIN_TONE} resim seçildi"


    ABOUT = """**Detaylarım :**

** Benim İsmim:** {bot_name}
    
** Dil:** [Python 3](https://www.python.org/)

** FrameWork:** [Pyrogram](https://github.com/pyrogram/pyrogram)

** Geliştirici:** {bot_owner}
"""

    HELP_USER = """**Adımları Takip Edin:**
   
☞︎︎︎ /mode komutunu kullanarak yükleme modunu değiştirin
☞︎︎︎ Bana bir fotoğraf gönder ve onu varsayılan pdf fotosu yapayım
☞︎︎︎ Şimdi bana bir dosya gönder ve yeniden adlandırayım.
☞︎︎︎ Sana pdf ismini sorduğumda yeni pdf ismini gir
"""

    START_TEXT = """Merhaba {user_mention},

Ben dosyaları fotoğraf ile beraber yeniden adlandırmak için tasarlandım.
Daha fazlası için yardım komutunu kullanın.

**Tasarlayan:** {bot_owner}
"""
