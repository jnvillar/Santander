from apscheduler.schedulers.blocking import BlockingScheduler

from santander.helpers import scrapper
from santander.services import database

scrapper_tool = scrapper.Scrapper()
sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='1-5', hour=4)
def scrapp():
    print('Scrapping')

    investments_founds_names = scrapper_tool.get_investment_founds()
    investments_founds_values = scrapper_tool.get_investment_founds_today_values()
    investments_founds_values = investments_founds_values[1::5]

    print('Saving data')

    database.insert_today_values(investments_founds_names, investments_founds_values)

    print('Data saved')


sched.start()
