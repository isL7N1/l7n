import telethon
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
from telethon.tl.functions.messages import GetPeerDialogsRequest

L7N = TelegramClient("pnhp",'29433225', "cbbfb104d4f4f43d3c78be56c1db2cf6") 
L7N.start()
L7N.send_message("me","مرحبا، الاوامر :\n`حجز + يوزر`")

@L7N.on(
events.NewMessage(
outgoing=True, pattern=r"حجز"))
async def StrPy(event):
        clicks = 1
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        username = str(msg[0])
        
        await event.reply(f"Done start - @{username}")
        try:
        	while True:
                    clicks += 1
                    await L7N(GetPeerDialogsRequest(peers=[username]))
        except telethon.errors.rpcerrorlist.UsernameNotOccupiedError:
                    try:
                        await L7N(functions.account.UpdateUsernameRequest(username=username))           
                    except Exception as error:
                    	if "wait" in str(error):
                    	  	await L7N.send_message(event.chat.id,f"Flood - {error.seconds} ️.")
                    	  	pass
                    	else:
                    		await L7N.send_message(event.chat_id, f'''
Err: {error}
User is Error : {username}''')
                    else:
                        await L7N.send_file(event.chat_id, "https://t.me/hhhhhviesw/2",caption=f'''
Good evening, chief ⚡
⌯ User ⤷ @{username}
⌯ Save ⤷ Account
⌯ Clicks ⤷ {clicks}
⌯ Program the bot : @g_4_q''')
                        await L7N.send_message(event.chat_id,"New Username 😁🗽:\nt.me/topython")
        except telethon.errors.rpcerrorlist.UsernameOccupiedError:
        	while True:
        		continue
        except telethon.errors.rpcerrorlist.ChannelPrivateError:
        	await L7N(functions.account.UpdateUsernameRequest(username=username))           
        	await L7N.send_file(event.chat_id, "https://t.me/hhhhhviesw/2",caption=f'''
Good evening, chief ⚡
⌯ User ⤷ @{username}
⌯ Save ⤷ Account
⌯ Clicks ⤷ {clicks}
⌯ Program the bot : @g_4_q''')
        	await L7N.send_message(event.chat_id,"New Username 😁🗽:\n@topython")
        
print("Run")
L7N.run_until_disconnected()