"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


# *******************************************  Вариант №1 *************************************************************
# O(n log n)
def get_top_profit_company(top, dct_company):
    list_company = list(dct_company.items())
    list_company.sort(key=lambda i: i[1], reverse=True)
    return list_company[:top]


company_annual_profit = {'company 1': 70000000, 'company 2': 20000000,
                         'company 3': 40000000, 'company 5': 100000000,
                         'company 6': 850000000, 'company 7': 100000}

top_list_company_profit = get_top_profit_company(3, company_annual_profit)
for i in top_list_company_profit:
    print(i[0], ':', i[1])

lst_company_profit = list(company_annual_profit.items())


# ******************************** Вариант №2 ************************************************************************
# О(n2)
def get_top_profit_company2(top, lst_company):
    for i in range(len(lst_company)):
        for j in range(len(lst_company) - 1):
            if lst_company[j + 1][1] > lst_company[j][1]:
                lst_company[j + 1], lst_company[j] = lst_company[j], lst_company[j + 1]
    return lst_company[:top]


for i in get_top_profit_company2(3, lst_company_profit):
    print(i[0], ':', i[1])


"""первым способом более эффективен так как О-нотация логарифмическая """
