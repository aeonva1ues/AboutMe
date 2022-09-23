import os
from django.views.generic import TemplateView
from django.conf import settings


class MyProfileView(TemplateView):
    template_name = "myProfile/main.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(MyProfileView, self).get_context_data(*args, **kwargs)
        context['my_photo'] = f'media/images/myphoto1.jpg'
        context['awards_list'] = [
            f'media/images/awards/{file_name}' for file_name in os.listdir(f'{settings.BASE_DIR}/media/images/awards')
        ]
        context['my_projects'] = [
            {
                'name': 'informaticssoft',
                'description': '''Несколько приложений (на данный момент - 2), созданных на Django для использования в школе. 
                Одно из них, PyTPretator, предоставляет пользователю редактор кода с некоторыми ограничениями (например, сложные для учеников библиотеки запрещены),
                справочники, а также задачи для практики (они пока не реализованы). PerformanceTech - файл-хранилище для фото и аудио, а также генератор веб-презентаций (галерей)
                для удобного показа на школьных мероприятиях.
                ''',
                'video': 'https://www.youtube.com/watch?v=LuhQFni2-m0',
                'github': 'https://github.com/aeonva1ues/InformaticsSoft'
            },
            {
                'name': 'ScreenManager',
                'description': '''
                Проект на Django, над которым я работал с своим наставником (знакомым программистом). Суть сайта: был написан агент, переносящий в базу данных информацию о фотографиях из сетевой папки 
                (снимки добавляются автоматически и имеют специальное название). На сайте визуализируются все устройства, с которых были сделаны снимки, а также с помощью фильтров и поиска можно находить их снимки. 
                ''',
                'video': 'https://www.youtube.com/watch?v=CyocPLV3UF8',
                'github': 'https://github.com/aeonva1ues/ScreenManager'
            },
            {   
                'name': 'InterviewBot',
                'description': '''
                В моем будущем проекте для Всероссийского конкурса присутствует опрос школьников, нацеленный на определение их заинтересованности
                в программировании. Для того, чтобы не проводить долгие и нудные беседы, с раздачей листочков, или не мучать себя и учеников гугл-формами с 5 вопросами, я сделал
                телеграм-бота. Так, за 2 дня, без моего участия, таблица "Results" в базе данных имела 37 записей. 
                ''',
                'video': 'https://www.youtube.com/watch?v=VEo17xP4tB4',
                'github': 'https://github.com/aeonva1ues/InterviewBot'
            },
            {
                'name': 'Licey2Bot',
                'description': '''
                Бот, автоматически переносящий новости с сайта лицея в телеграм-канал лицея (также созданный мной). Кроме того, имеет чат-бот функции, а также позволяет
                модераторам быстро создавать новости для канала в едином стиле (без необходимости выдачи админки в канале лицея). Реализована возможность пользователям задавать вопросы администрации лицея через бота.
                ''',
                'video': 'https://www.youtube.com/watch?v=extE4KcWSKM',
                'github': 'https://github.com/aeonva1ues/Licey2Bot'
            },
        ]
        return context
