from telegram import Bot
import time
from pprint import pprint

token = "6666621362:AAFxmI1lOaRi_0Dzd0doUHvTardmX5JePpY"

bot = Bot(token=token)

def echo():
    update_id = 0

    while True:
        time.sleep(0.5)

        # print(f'updates: {update_id}')
        updates = bot.get_updates()
        if updates[-1].update_id == update_id:
            continue
        else:
            last_update = updates[-1]
            
            message = last_update.message
            # pprint(message)
            print("-"*50)
            pprint(message)

            chat_id = message.chat.id
            text = message.text 
            photo = message.photo
            audio = message.audio
            document = message.document
            video = message.video
            location = message.location
            contact = message.contact
            dice = message.dice


            if text != []:
                bot.send_message(chat_id=chat_id, text=text)

            elif audio != []:
                file_id = audio[0].file_id
                duration = audio[0].duration
                bot.send_audio(chat_id=chat_id, audio=file_id, duration=duration)
            elif photo != []: 
                file_id = photo[0].file_id
                bot.send_photo(chat_id=chat_id, photo=file_id)
            elif contact != []:
                phone_number = message.contact.phone_number
                first_name = message.contact.first_name
                bot.send_contact(chat_id=chat_id, phone_number=phone_number, first_name=first_name)
            elif dice != []:
                emoji = message.dice.emoji
                value = message.dice.value
                bot.send_dice(chat_id=chat_id, emoji=emoji, value=value)
            elif animation != []:
                file_id = message.animation.file_id
                bot.send_animation(chat_id=chat_id, animation=file_id)
            elif location != []:
                latitude = message.location.latitude
                longitude = message.location.longitude
                bot.send_location(chat_id=chat_id, latitude=latitude, longitude=longitude)

            else:
                continue

            update_id = updates[-1].update_id

echo()