import requests

from .update import Update
from .message import Message
from .user import User
from .chat import Chat
from .photo_size import PhotoSize
from .audio import Audio
from .document import Document
from .video import Video
from .voice import Voice
from .contact import Contact
from .dice import Dice
from .location import Location
from .sticker import Sticker



class Bot:
    def __init__(self, token: str):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def get_updates(self):
        method = "getUpdates"
        resp = requests.get(self.api_url + method)

        if resp.status_code != 200:
            return []

        result_json = resp.json()["result"]
        updates = []
        for update in result_json:
            chat = None
            if 'chat' in update['message']:
                chat = Chat(
                    update["message"]["chat"]["id"],
                    update["message"]["chat"]["type"],
                    update["message"]["chat"]["first_name"],
                    update["message"]["chat"].get("last_name"),
                    update["message"]["chat"].get("username"),
                )

            user = None
            if 'from' in update['message']:
                user = User(
                    update["message"]["from"]["id"],
                    update["message"]["from"]["is_bot"],
                    update["message"]["from"]["first_name"],
                    update["message"]["from"].get("last_name"),
                    update["message"]["from"].get("username"),
                )

            photo = []
            if 'photo' in update['message']:
                photo = []
                for photo_size in update["message"]["photo"]:
                    photo.append(
                        PhotoSize(
                            photo_size["file_id"],
                            photo_size["file_unique_id"],
                            photo_size["width"],
                            photo_size["height"],
                            photo_size.get("file_size"),
                        )
                    )
            
            audio = None
            if 'audio' in update['message']:    
                audio = Audio(
                    update["message"]["audio"]["file_id"],
                    update["message"]["audio"]["file_unique_id"],
                    update["message"]["audio"].get("duration"),
                )

            document = None
            if 'document' in update['message']:
                document = Document(
                    update["message"]["document"]["file_id"],
                    update["message"]["document"]["file_unique_id"],
                    update["message"]["document"].get("file_name"),
                    update["message"]["document"].get("mime_type"),
                    update["message"]["document"].get("file_size"),
                )

            video = None
            if 'video' in update['message']:
                video = Video(
                    update["message"]["video"]["file_id"],
                    update["message"]["video"]["file_unique_id"],
                    update["message"]["video"]["width"],
                    update["message"]["video"]["height"],
                    update["message"]["video"].get("duration"),
                )

            voice = None
            if 'voice' in update['message']:
                voice = Voice(
                    update["message"]["voice"]["file_id"],
                    update["message"]["voice"]["file_unique_id"],
                    update["message"]["voice"].get("duration"),
                )

            contact = None
            if 'contact' in update['message']:
                contact = Contact(
                    update["message"]["contact"]["phone_number"],
                    update["message"]["contact"]["first_name"],
                    update["message"]["contact"].get("last_name"),
                    update["message"]["contact"].get("user_id"),
                )   

            dice = None
            if 'dice' in update['message']:
                dice = Dice(
                    update["message"]["dice"]["emoji"],
                )

            location = None
            if 'location' in update['message']:
                location = Location(
                    update["message"]["location"]["longitude"],
                    update["message"]["location"]["latitude"],
                )

            sticker = None  
            if 'sticker' in update['message']:
                sticker = Sticker(
                    update["message"]["sticker"]["file_id"],
                    update["message"]["sticker"]["file_unique_id"],
                    update["message"]["sticker"]["width"],
                    update["message"]["sticker"]["height"],
                    update["message"]["sticker"].get("is_animated"),
                    update["message"]["sticker"].get("emoji"),
                    update["message"]["sticker"].get("set_name"),
                    update["message"]["sticker"].get("mask_position"),
                    update["message"]["sticker"].get("file_size"),
                )

            message = Message(
                message_id=update["message"]["message_id"],
                date=update["message"]["date"],
                from_user=user,
                sender_chat=chat,
                chat=chat,
                forward_from=user,
                text=update["message"].get("text"),
                audio=audio,
                document=document,
                photo=photo,
                video=video,
                sticker=sticker,
                caption=update["message"].get("caption"),
                contact=contact,
                dice=dice,
                location=location,
            )

            update = Update(
                update["update_id"],
                message,
            )

            updates.append(update)

        return updates


    def send_message(self, chat_id: int, text: str):
        method = "sendMessage"
        params = {
            "chat_id": chat_id,
            "text": text,
        }
        resp = requests.post(self.api_url + method, params)

        return resp

    def send_photo(self, chat_id: int, photo: str):
        method = "sendPhoto"
        params = {
            "chat_id": chat_id,
            "photo": photo,
        }
        resp = requests.post(self.api_url + method, params)

        return resp

    def send_audio(self, chat_id: int, audio: str):
        method = "sendAudio"
        params = {
            "chat_id": chat_id,
            "audio": audio,
        }
        resp = requests.post(self.api_url + method, params)

        return resp

    def send_document(self, chat_id: int, document: str):
        method = "sendDocument"
        params = {
            "chat_id": chat_id,
            "document": document,
        }
        resp = requests.post(self.api_url + method, params)

        return resp

    def send_video(self, chat_id: int, video: str):
        method = "sendVideo"
        params = {
            "chat_id": chat_id,
            "video": video,
        }
        resp = requests.post(self.api_url + method, params)

        return resp

    def send_voice(self, chat_id: int, voice: str):
        method = "sendVoice"
        params = {
            "chat_id": chat_id,
            "voice": voice,
        }
        resp = requests.post(self.api_url + method, params)

        return resp

