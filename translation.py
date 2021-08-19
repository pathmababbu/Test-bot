class Translation(object):
    START_TEXT = """Hi {},
I'm X-URL-Uploader!
මෙම බොට් භාවිතා කර Http/Https සෘජු link සම්බන්ද දෑ උඩුගත කරගැනීමේ හැකියාවක් ඇත 

/help වැඩි විස්තර සඳහා!"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """ඔබට උසස් ගණයේ වීඩියෝ බාගැනීමට අවශ්‍ය නම් පහත ආකෘතියෙන් ලබා දෙන්න:
URL |ගොනු නාමය | පරිශීලක නාමය  | මුරපදය"""
    DOWNLOAD_START = "ඔබේ ගීතය Download වෙමින් පවතී.."
    UPLOAD_START = "ඔබේ ගීතය Upload වෙමින් පවතී.."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nසමාවෙන්න , telegram තුල upload කල හැක්කෙ 2GB වලට වඩා කුඩා ගොනුවේ."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using @xurluploaderbot)"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds.\nUploaded in {} seconds.\n\n@xurluploaderbot"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    HELP_USER = """කොහොමද මාව භාවිතා කරන්නෙ? මෙම පියවර අනුගමනය කරන්න!
    
1. යවන්න url (උදාහරණය.domain/File.mp4 | New Filename.mp4).
2. යවන්න Image A Custom Thumbnail (විකල්ප).
3. බොත්තම තෝරන්න.
   SVideo - තිර පිටපත් සමඟ ගොනුව වීඩියෝවක් ලෙස දෙන්න
   DFile  - තිර පිටපත් සමඟ ගොනුව (වීඩියෝ) ගොනුව ලෙස දෙන්න
   Video  - තිර පිටපත් නොමැතිව ගොනුව වීඩියෝවක් ලෙස දෙන්න
   File   - තිරපිටපත් නොමැතිව ගොනුව දෙන්න

බොට් ප්‍රතිචාර නොදැක්වුවහොත් අමතන්න, @developer2006"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "පිලිතුරු /genthumbnail මාධ්‍ය ඇල්බමයකට,thumbnail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "මාධ්‍ය ඇල්බමයේ අඩංගු විය යුත්තේ ඡායාරූප දෙකක් පමණි. කරුණාකර මාධ්‍ය ඇල්බමය නැවත යවන්න, පසුව නැවත උත්සාහ කරන්න, නැතහොත් ඇල්බමයක ඡායාරූප දෙකක් පමණක් යවන්න."
    CANCEL_STR = "ක්‍රියාවලිය අවලංගු කරන ලදි.."
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    SLOW_URL_DECED = "ගොෂ් ඉතා මන්දගාමී යූආර්එල් එකක් බව පෙනේ. , මෙම ගොනුව බාගැනීමට මට හැකියාවක් නැත. මට වේගවත් යූආර්එල් එකක් ලබා දෙන්න, එවිට මට telegram වෙත උඩුගත කළ හැකිය, අනෙක් දෑ සඳහා මම වේගය අඩු නොකරමි."
