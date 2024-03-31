from selenium.webdriver.common.by import By

'''Рассчитать расход и стоимость (км, литры)'''
expense_and_cost = (By.ID, 'type_1')

average_consumption = (By.NAME, 'average_consumption')
average_consumption_error = (By.ID, 'average_consumption-error')
average_consumption_dropdown = (By.CSS_SELECTOR, '.units-metric [name="consumption_unit"]')
avg_cons_drop_l_100 = (By.CSS_SELECTOR, '[value="lp100km"]')
avg_cons_drop_km_l = (By.CSS_SELECTOR, '[value="kmpl"]')


'''Рассчитать средний расход на 100 км. (км, литры)'''
expense_per_100 = (By.ID, 'type_2')

consumption = (By.NAME, 'consumption')
consumption_error = (By.ID, 'consumption-error')


'''Рассчитать расход и стоимость (мили, галлоны)'''
to_mil_gal_btn = (By.CSS_SELECTOR, '[data-value="english"]')

expense_and_cost_en = (By.ID, 'type_1')

average_consumption_en = (By.CSS_SELECTOR, '.units-english [name="average_consumption"]')
average_consumption_error_en = (By.ID, 'average_consumption-error')
average_consumption_dropdown_en = (By.CSS_SELECTOR, '.units-english [name="consumption_unit"]')
avg_cons_drop_mil_gal = (By.CSS_SELECTOR, '[value="mpg"]')
avg_cons_drop_gal_100 = (By.CSS_SELECTOR, '[value="gp100mi"]')

units = (By.CSS_SELECTOR, '.calc-input-desc .units-english')


'''Рассчитать средний расход на 100 км. (мили, галлоны)'''
expense_per_100_en = (By.ID, 'type_2')

consumption_en = (By.NAME, 'consumption')
consumption_error_en = (By.ID, 'consumption-error')


'''Общие локаторы'''
submit_btn = (By.CSS_SELECTOR, '.calc-submit')
result_placeholder_sum = (By.CSS_SELECTOR, '.result-placeholder-sum')
distance = (By.NAME, 'distance')
distance_error = (By.ID, 'distance-error')
cost = (By.NAME, 'cost')