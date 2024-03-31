from pages.base_page import BasePage
from pages.locators import *


calc_url = 'https://calcus.ru/kalkulyator-rashoda-topliva'


class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    '''Рассчитать расход и стоимость (км, литры)'''
    def expense_and_cost(self):
        return self.find(expense_and_cost)

    def average_consumption(self):
        return self.find(average_consumption)

    def average_consumption_error(self):
        return self.find(average_consumption_error)

    def average_consumption_dropdown(self):
        return self.find(average_consumption_dropdown)

    def avg_cons_drop_l_100(self):
        return self.find(avg_cons_drop_l_100)

    def avg_cons_drop_km_l(self):
        return self.find(avg_cons_drop_km_l)

    '''Рассчитать средний расход на 100 км. (км, литры)'''
    def expense_per_100(self):
        return self.find(expense_per_100)

    def consumption(self):
        return self.find(consumption)

    def consumption_error(self):
        return self.find(consumption_error)

    '''Рассчитать расход и стоимость (мили, галлоны)'''
    def to_mil_gal_btn(self):
        return self.find(to_mil_gal_btn)

    def expense_and_cost_en(self):
        return self.find(expense_and_cost_en)

    def average_consumption_en(self):
        return self.find(average_consumption_en)

    def average_consumption_error_en(self):
        return self.find(average_consumption_error_en)

    def average_consumption_dropdown_en(self):
        return self.find(average_consumption_dropdown_en)

    def avg_cons_drop_mil_gal(self):
        return self.find(avg_cons_drop_mil_gal)

    def avg_cons_drop_gal_100(self):
        return self.find(avg_cons_drop_gal_100)

    def units(self):
        return self.find(units)

    '''Рассчитать средний расход на 100 км. (мили, галлоны)'''
    def expense_per_100_en(self):
        return self.find(expense_per_100_en)

    def consumption_en(self):
        return self.find(consumption_en)

    def consumption_error_en(self):
        return self.find(consumption_error_en)

    '''Общие методы'''
    def submit_btn(self):
        return self.find(submit_btn)

    def result_placeholder_sum(self):
        return self.find(result_placeholder_sum)

    def distance(self):
        return self.find(distance)

    def distance_error(self):
        return self.find(distance_error)

    def cost(self):
        return self.find(cost)
