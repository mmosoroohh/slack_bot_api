from app.utils.gappshelper import GappsHelper
import time
from datetime import datetime, date, timedelta
from config import get_env

class Actions:
    def __init__(self, slackhelper, user_info=None):
        self.gappshelper = GappsHelper()
        self.sheet = self.gappshelper.open_sheet()
        self.user_info = user_info
        self.slackhelper = slackhelper


    def my_tasks(self):
        email = self.user_info['user']['profile']['email']
        recipient = self.user_info['user']['id']
        task_cells = list(filter(lambda x: x['Email Address'] == email, self.sheet))
        for index, row in enumerate(task_cells):
            text_detail = (
                '*Task #{} for {}:* \n\n'
                '*Hey {},* Today is the check-in day for your writeupp titled\n'
                '`{}`.\n\n'
                'Whats the status of the article?\n'
                'PS: Please reply to this thread, the managers will review and reply to you ASAP').format(str(index + 1), row['Next Check-In'], row['Name'], row['Most Recent Learning Experienceyou\'d like to write about'])
            self.slackhelper.post_message(text_detail, recipient)
        return None

    def __convert_to_date(self, date_string):
        today = date.today()
        if date_string == 'today':
            return today
        elif date_string == 'yesterday':
            return today - timedelta(days=1)
        elif date_string == 'tomorrow':
            return today + timedelta(days=1)
        else:
            return today

    def show_tasks(self, date=None):
        if date in ['today', 'tomorrow', 'yesterday']:
            day_date_param = self.__convert_to_date(date)
            task_cells = list(filter(lambda x: datetime.strptime(self.__num_suffix(x['Next Check-In']), '%d %B %Y').date() == day_date_param, self.sheet))
            if task_cells:
                self.__perform_send_action(task_cells)
            else:
                return {'text': 'No task assigned to be checked in {}, try another date'.format(date)}
        else:
            date_param = date.replace('-', ' ')
            task_cells = list(filter(lambda x: x['Next Check-In'] == date_param, self.sheet))
            if task_cells:
                self.__perform_send_action(task_cells)
            else:
                return {'text': 'No task assigned to be checked in on this date, try another date'}

    def __perform_send_action(self, task_cells):
        recipient = self.user_info['user']['id']
        for index, row in enumerate(task_cells):
            text_detail = (
                '*Task #{} for {}:* \n\n'
                '*Hey {},* Today is the check-in day for your writeup titled\n'
                '`{}`.\n\n'
                'Whats the status of the article?\n'
                'PS: Please reply to this thread, the managers will review and reply to you ASAP').format(str(index + 1), row['Next Check-In'], row['Name'],
                row['Most Recent Learning Experience you\'d like to write about'])
            self.slackhelper.post_message(text_detail, recipient)
        return None

    def help(self):
        """
        Return the Available commands in the system and their usage format
        """
        return {
            'text': 'Available Commands: \n `/ranti my-task e.g /ranti my-task` \n To get task assigned to you.\n'
                    ' \n `/ranti show-task [date]{dth-month-year} e.g /ranti show-task 5th-june-2018` \n Show all tasks for a particular date \n'
                    '\n `/ranti show-task [today] e.g /ranti show-task today` \n Show all tasks for today \n'
                    '\n `/ranti show-task [tomorrow] e.g /ranti show-task tomorrow` \n Show all tasks for tomorrow \n'
                    '\n `/ranti help` \n This help information \n \n Ranti ver: 1.0'
        }

    def __num_suffix(self, check_in_date):
        """
        Strip the date suffix and return the date
        Before comparing the date
        """
        date_value = str(check_in_date).split(' ')
        day_value = date_value[0][:-2]
        date_value[0] = day_value
        return ' '.join(date_value)

    def get_centers(centers):
        return [{"name": "center", "text": i, "type": "button", "value": i} for i in centers]


    def start_channel(self):
        print('Worker is running...., waiting till 8.00am')
        while True:
            # current_time = datetime.now()
            # current_hour = current_time.hour
            # current_minute = current_time.minute
            #
            # if current_hour - 8 > 0:
            #     sleep_time = 24 - current_hour + 8 - (current_minute/60)
            # elif current_hour - 8 < 0:
            #     sleep_time = 8 - current_hour - (current_minute/60)
            # elif current_hour == 8:
            #     if current_minute == 0:
            #         sleep_time = 0
            #     else:
            #         sleep_time = 24 - current_hour + 8 - (current_minute/60)

            for index, row in enumerate(self.sheet):
                andela_centers = ["Andela Lagos", "Andela Kenya", "Andela Rwanda"]
                if :
                    text_detail = {
                        "text":'*Welcome to Activo \n\n*Hey {},* Choose your Center to continue...\n\n',
                        "attachments": [
                            {
                                "text": "Choose a center to book",
                                "fallback": "You are unable to choose a center",
                                "callback_id": "wopr_game",
                                "color": "#0080ff",
                                "attachment_type": "default",
                                "actions": get_centers(andela_centers)
                            }
                        ],
                        }
                        'Whats the status of the article?\n'
                        'PS: Please reply to this thread, the managers will review and reply to you ASAP').format(
                        str(index + 1), row['Next Check-In'], row['Name'],
                        row['Most Recent Learning Experience you\'d like to write about'])
                    self.slackhelper.post_message_to_channel(text_detail)
            print('Message sent or no tasks for today-waiting till 8.00a.m next day')
            time.sleep(sleep_time * 3600)
