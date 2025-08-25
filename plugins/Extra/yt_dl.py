# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from __future__ import unicode_literals

import os, requests, asyncio, math, time, wget
from pyrogram import filters, Client
from pyrogram.types import Message
from info import CHNL_LNK
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL


@Client.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    # Get query from message, joining all words after the command
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply_text("Please provide a song name.\nExample: `/song vaa vaathi song`")

    m = await message.reply_text(f"**🔎 Searching for your song...\n`{query}`**")
    
    try:
        # Search for the song on YouTube, get only the first result
        results = YoutubeSearch(query, max_results=1).to_dict()
        if not results:
            return await m.edit("❌ Song not found. Please check the spelling and try again.")

        # Extract info from the search result
        video_info = results[0]
        link = f"https://youtube.com{video_info['url_suffix']}"
        title = video_info["title"]
        duration = video_info["duration"]
        thumbnail_url = video_info["thumbnails"][0]
        video_id = video_info["id"]

        # Download the thumbnail
        thumb_name = f'thumb_{video_id}.jpg'
        thumb = requests.get(thumbnail_url, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)

    except Exception as e:
        await m.edit("❌ Search failed! Please try again later.\nExample: `/song vaa vaathi song`")
        print(f"Search Error: {e}")
        return
                
    await m.edit("**📥 Downloading your song...**")

    # yt-dlp options to download the best audio available
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'downloads/{video_id}.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
    }

    # Create a 'downloads' directory if it doesn't exist
    if not os.path.isdir("downloads"):
        os.makedirs("downloads")

    audio_file = None  # Initialize to handle potential errors
    try:
        # Download the audio using yt-dlp
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            audio_file = ydl.prepare_filename(info)

        # Prepare caption and other details for sending the audio
        cap = f"**BY›› [UPDATE]({CHNL_LNK})**"
        
        # Convert duration string (e.g., "3:45") to total seconds for Pyrogram
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60

        # Send the downloaded audio file to the user
        await message.reply_audio(
            audio=audio_file,
            caption=cap,
            title=title[:35],  # Telegram title limit is around 35 chars
            performer="VJ Botz",
            duration=dur,
            thumb=thumb_name
        )
        await m.delete()

    except Exception as e:
        await m.edit("**🚫 ERROR 🚫**\n\nSomething went wrong while downloading. Please try again.")
        print(f"Download/Upload Error: {e}")
        
    finally:
        # Clean up (delete) the downloaded audio file and thumbnail
        try:
            if audio_file and os.path.exists(audio_file):
                os.remove(audio_file)
            if os.path.exists(thumb_name):
                os.remove(thumb_name)
        except Exception as e:
            print(f"Cleanup Error: {e}")

def get_text(message: Message) -> [None,str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None


@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    urlissed = get_text(message)
    pablo = await client.send_message(message.chat.id, f"**𝙵𝙸𝙽𝙳𝙸𝙽𝙶 𝚈𝙾𝚄𝚁 𝚅𝙸𝙳𝙴𝙾** `{urlissed}`")
    if not urlissed:
        return await pablo.edit("Example: /video Your video link")     
    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        return await pablo.edit_text(f"**𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙵𝚊𝚒𝚕𝚎𝚍 𝙿𝚕𝚎𝚊𝚜𝚎 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗..♥️** \n**Error :** `{str(e)}`")       
    
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""**𝚃𝙸𝚃𝙻𝙴 :** [{thum}]({mo})\n**𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :** {message.from_user.mention}"""

    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,        
        reply_to_message_id=message.id 
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
