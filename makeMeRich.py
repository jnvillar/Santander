import scrapper
import database

url = 'http://www.santanderrio.com.ar/ConectorPortalStore/Rendimiento'
scrapper = scrapper.Scrapper(url)
investmentsFoundsNames = scrapper.get_investment_founds()
investmentsFoundsValues = scrapper.get_investment_founds_today_values()
database.insert_today_values(investmentsFoundsNames, investmentsFoundsValues)

