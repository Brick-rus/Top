from pages.main_page import *
from pages.locators import *

'''Тесты для км, литров'''
# Клик по Submit без заполнения полей для "Рассчитать расход и стоимость" и "литров/100 км"
def test_1_expense_and_cost_l_100km_submit_click(browser):
    test_1 = MainPage(browser, calc_url)
    test_1.open()

    try:
        test_1.submit_btn().click()

        assert test_1.average_consumption_error().is_displayed(), f'Avg cons error'
        assert test_1.distance_error().is_displayed(), f'Dist error'

    finally:
        test_1.save_screenshot('test_1_expense_and_cost_l_100km_submit_click.png')


# Клик по Submit без заполнения полей для "Рассчитать расход и стоимость" и "километров/литр"
def test_2_expense_and_cost_km_l_submit_click(browser):
    test_2 = MainPage(browser, calc_url)
    test_2.open()

    try:
        test_2.average_consumption_dropdown().click()
        test_2.avg_cons_drop_km_l().click()
        test_2.submit_btn().click()

        assert test_2.average_consumption_error().is_displayed(), f'Avg cons error'
        assert test_2.distance_error().is_displayed(), f'Dist error'

    finally:
        test_2.save_screenshot('test_2_expense_and_cost_km_l_submit_click.png')


# Заполнение всех полей для "Рассчитать расход и стоимость" и "литров/100 км"
def test_3_expense_and_cost_all_fiels_l_100km(browser):
    test_3 = MainPage(browser, calc_url)
    test_3.open()

    try:
        test_3.average_consumption().send_keys("15")
        test_3.distance().send_keys("250")
        test_3.cost().send_keys("50")
        test_3.submit_btn().click()
        test_3.visibility_of_element_located(result_placeholder_sum)
        assert test_3.result_placeholder_sum().is_displayed(), f'Res sum error'
    finally:
        test_3.save_screenshot('test_3_expense_and_cost_all_fiels_l_100km.png')


# Заполнение всех полей для "Рассчитать расход и стоимость" и "километров/литр"
def test_4_expense_and_cost_all_fiels_km_l(browser):
    test_4 = MainPage(browser, calc_url)
    test_4.open()

    try:
        test_4.average_consumption_dropdown().click()
        test_4.avg_cons_drop_km_l().click()
        test_4.average_consumption().send_keys("20")
        test_4.distance().send_keys("250")
        test_4.cost().send_keys("50")
        test_4.submit_btn().click()
        test_4.visibility_of_element_located(result_placeholder_sum)
        assert test_4.result_placeholder_sum().is_displayed(), f'Res sum error'
    finally:
        test_4.save_screenshot('test_4_expense_and_cost_all_fiels_km_l.png')


# Клик по Submit без заполнения полей для "Рассчитать средний расход на 100 км."
def test_5_expense_per_100_submit_click(browser):
    test_5 = MainPage(browser, calc_url)
    test_5.open()

    try:
        test_5.script_click(test_5.expense_per_100())
        test_5.submit_btn().click()
        assert test_5.consumption_error().is_displayed(), f'Cons error'
        assert test_5.distance_error().is_displayed(), f'Dist error'
    finally:
        test_5.save_screenshot('test_5_expense_per_100_submit_click.png')


# Заполнение всех полей для "Рассчитать средний расход на 100 км."
def test_6_expense_per_100_all_fields(browser):
    test_6 = MainPage(browser, calc_url)
    test_6.open()

    try:
        test_6.script_click(test_6.expense_per_100())
        test_6.consumption().send_keys("50")
        test_6.distance().send_keys("250")
        test_6.cost().send_keys("50")
        test_6.submit_btn().click()
        test_6.visibility_of_element_located(result_placeholder_sum)
        assert test_6.result_placeholder_sum().is_displayed(), f'Res sum error'
    finally:
        test_6.save_screenshot('test_6_expense_per_100_all_fields.png')


'''Тесты для миль, галлонов'''
# Клик по Submit без заполнения полей для "Рассчитать расход и стоимость" и "миль / галлон"
def test_7_expense_and_cost_mil_gal_submit_click(browser):
    test_7 = MainPage(browser, calc_url)
    test_7.open()

    try:
        test_7.to_mil_gal_btn().click()
        test_7.submit_btn().click()

        assert test_7.average_consumption_error().is_displayed(), f'Avg cons error'
        assert test_7.distance_error().is_displayed(), f'Dist error'

    finally:
        test_7.save_screenshot('test_7_expense_and_cost_mil_gal_submit_click.png')


# Клик по Submit без заполнения полей для "Рассчитать расход и стоимость" и "галлонов / 100 миль"
def test_8_expense_and_cost_gal_100_submit_click(browser):
    test_8 = MainPage(browser, calc_url)
    test_8.open()

    try:
        test_8.to_mil_gal_btn().click()
        test_8.average_consumption_dropdown_en().click()
        test_8.avg_cons_drop_gal_100().click()
        test_8.submit_btn().click()

        assert test_8.average_consumption_error().is_displayed(), f'Avg cons error'
        assert test_8.distance_error().is_displayed(), f'Dist error'

    finally:
        test_8.save_screenshot('test_8_expense_and_cost_gal_100_submit_click.png')


# Заполнение всех полей для "Рассчитать расход и стоимость" и "миль / галлон"
def test_9_expense_and_cost_all_fiels_mil_gal(browser):
    test_9 = MainPage(browser, calc_url)
    test_9.open()

    try:
        test_9.to_mil_gal_btn().click()
        test_9.average_consumption_en().send_keys("15")
        test_9.distance().send_keys("250")
        test_9.cost().send_keys("50")
        test_9.submit_btn().click()
        test_9.visibility_of_element_located(result_placeholder_sum)
        assert test_9.result_placeholder_sum().is_displayed(), f'Res sum error'
    finally:
        test_9.save_screenshot('test_9_expense_and_cost_all_fiels_mil_gal.png')


# Заполнение всех полей для "Рассчитать расход и стоимость" и "галлонов / 100 миль"
def test_10_expense_and_cost_all_fiels_gal_100(browser):
    test_10 = MainPage(browser, calc_url)
    test_10.open()

    try:
        test_10.to_mil_gal_btn().click()
        test_10.average_consumption_dropdown_en().click()
        test_10.avg_cons_drop_gal_100().click()
        test_10.average_consumption_en().send_keys("20")
        test_10.distance().send_keys("250")
        test_10.cost().send_keys("50")
        test_10.submit_btn().click()
        test_10.visibility_of_element_located(result_placeholder_sum)
        assert test_10.result_placeholder_sum().is_displayed(), f'Res sum error'
    finally:
        test_10.save_screenshot('test_10_expense_and_cost_all_fiels_gal_100.png')


# Клик по Submit без заполнения полей для "Рассчитать средний расход на 100 км."
def test_11_expense_per_100_submit_click_en(browser):
    test_11 = MainPage(browser, calc_url)
    test_11.open()

    try:
        test_11.to_mil_gal_btn().click()
        test_11.script_click(test_11.expense_per_100_en())
        test_11.submit_btn().click()
        assert test_11.consumption_error_en().is_displayed(), f'Cons error'
        assert test_11.distance_error().is_displayed(), f'Dist error'
    finally:
        test_11.save_screenshot('test_11_expense_per_100_submit_click_en.png')


# Заполнение всех полей для "Рассчитать средний расход на 100 км."
def test_12_expense_per_100_all_fields_en(browser):
    test_12 = MainPage(browser, calc_url)
    test_12.open()

    try:
        test_12.to_mil_gal_btn().click()
        test_12.script_click(test_12.expense_per_100_en())
        test_12.consumption_en().send_keys("50")
        test_12.distance().send_keys("250")
        test_12.cost().send_keys("50")
        test_12.submit_btn().click()
        test_12.visibility_of_element_located(result_placeholder_sum)
        assert test_12.result_placeholder_sum().is_displayed(), f'Res sum error'
    finally:
        test_12.save_screenshot('test_12_expense_per_100_all_fields_en.png')
    