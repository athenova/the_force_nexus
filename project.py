from simple_blogger import Journalist
from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from simple_blogger.senders.TelegramSender import TelegramSender
from simple_blogger.senders.InstagramSender import InstagramSender
from simple_blogger.senders.VkSender import VkSender
from datetime import datetime

class Project(Journalist):
    def __init__(self, **kwargs):
        super().__init__(            
            first_post_date=datetime(2025, 1, 1),
            text_generator=OpenAITextGenerator(),
            topic_word_limit=100,
            reviewer=TelegramSender(),
            senders=[TelegramSender(channel_id=f"@the_force_nexus"), 
                     InstagramSender(channel_token_name='FORCE_NEXUS_THE_TOKEN'),
                     VkSender(group_id="229821912")],
            **kwargs)

    def _get_category_folder(self, task):
        return task['country']
                    
    def _task_converter(self, item):
        return { 
            "topic": item['name'],
            "location": item['location'],
            "country": item['country'],
            "topic_prompt": f"Расскажи интересный факт про {item['name']}, который находятся в {item['location']} {item['country']}, используй не более {self.topic_word_limit} слов, используй смайлики",
            "topic_image": f"Нарисуй {item['name']}, который находятся в {item['location']} {item['country']}",
        }
    
    def _system_prompt(self, task):
        return f"Ты - блогер-эзотерик с 1000000 миллионном подписчиков"