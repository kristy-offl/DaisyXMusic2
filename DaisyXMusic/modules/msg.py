# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello π [{}](tg://user?id={})!**\n\n**=>I'm a Advanced Bot For Playing Songs In Your Group's Voice Chat.**\n\n**=> I Can Play Songs In Your Channel Voice Chat's Also.**\n\n**πFor More Details Check /help For More Info.**"
      HELP_MSG = [
        ".",
f"""
**Hey π Welcome back to {PROJECT_NAME}

β© I can play music in your group's voice chat as well as channel voice chats

β© Assistant UserName >> @{ASSISTANT_NAME}\n\nClick Next For instructions**
""",

f"""
**How To Play Song's In Your Group Voice chat βοΈ

β© Make bot admin (Group and in channel if use cplay

β© Start a voice chat

β© Try /play [song name] for the first time by an admin

β© If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry**

**How To Play Song's In Your Channel Voice Chat !?

β© Make me admin of your channel 

β© Send /userbotjoinchannel in linked group

β© Now send commands in linked group**

** Available Commands**

**=>> Song Playing π§**

- /play: Play song using youtube music
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn

**=>> Playback β―**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

**Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.**
""",
        
f"""
**=>> Channel Music Play π **

β© For linked group admins only:

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

**channel is also can be used instead of c ( /cplay = /channelplay)**
""",

f"""
**=>> More tools π§βπ§**

- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

**=>> Commands for Sudo Users βοΈ**

 - /userbotleaveall - remove assistant from all chats
 - /gcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
Sudo Users can execute any command in any groups

"""
      ]
