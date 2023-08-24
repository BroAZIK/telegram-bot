from .user import User
from .chat import Chat
from .audio import Audio
from .document import Document
from .photo_size import PhotoSize
from .video import Video
from .sticker import Sticker
from .contact import Contact
from .dice import Dice
from .location import Location
from .voice import Voice


class Message:
    def __init__(
        self, 
        message_id: int,
        date: int,
        from_user: User=None,
        sender_chat: Chat=None,
        chat: Chat=None,
        forward_from: User=None,
        text: str=None,
        audio: Audio=None,
        document: Document=None,
        photo: list[PhotoSize]=None,
        video: Video=None,
        sticker: Sticker=None,
        caption: str=None,
        contact: Contact=None,
        dice: Dice=None,
        location: Location=None,
        voice: Voice=None,
    ):
        self.message_id = message_id
        self.date = date
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.chat = chat
        self.forward_from = forward_from
        self.text = text
        self.audio = audio
        self.document = document
        self.photo = photo
        self.video = video
        self.sticker = sticker
        self.caption = caption
        self.contact = contact
        self.dice = dice
        self.location = location
        self.voice = voice

    def __str__(self):
        return f"Message {self.message_id} from {self.from_user} in {self.chat}"
