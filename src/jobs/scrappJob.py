from src import celery
from src.helpers import scrapper
import src.services.database as database

scrapper_tool = scrapper.Scrapper()

@celery.task()
def scrap():
    investments_founds_names = scrapper_tool.get_investment_founds()
    investments_founds_values = scrapper_tool.get_investment_founds_today_values()
    investments_founds_values = investments_founds_values[1::5]
    database.insert_today_values(investments_founds_names, investments_founds_values)
    return
