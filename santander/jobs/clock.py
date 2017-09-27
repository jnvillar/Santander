from apscheduler.schedulers.blocking import BlockingScheduler

from santander.helpers import scrapper
from santander.services import database
import time

scrapper_tool = scrapper.Scrapper()
sched = BlockingScheduler()


@sched.scheduled_job('interval', hours=1)
def scrapp():
    print('Scrapping')
    day = time.strftime("%a")
    
    if day is not 'Sun' and day is not 'Mon':
        investments_founds_names = scrapper_tool.get_investment_founds()
        investments_founds_values = scrapper_tool.get_investment_founds_today_values()
        investments_founds_values = investments_founds_values[1::5]

        print('Saving data')

        database.insert_today_values(investments_founds_names, investments_founds_values)

        print('Data saved')


sched.start()
