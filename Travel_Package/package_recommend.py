def luggage_list(temp, weather_russki, dates):
    if temp!=None and weather_russki!=None:
        t=int(temp)
        items = [
            "Паспорт",
            "Билет",
            "Носки"
        ]

        if t < 10:
            items.append("Теплая зимняя куртка")
            if weather_russki == "Снег❄️":

                items.append("Шапка зимняя")
                items.append("Варежки")


        elif t < 20:
            items.append("Пальто")
            items.append("Свитер")

        elif t < 25:
            items.append("Ветровка")
            items.append("Кофта")

        if weather_russki == "Дождь🌧️":

            items.append("Зонтик")
            items.append("Дождевик")

        if weather_russki== "Солнечно☀️":

            items.append("Солнечные очки")
            items.append("Солнечный крем")



        if dates > 5:
            items.append("Запасная одежда")

        return " \n".join(items)
    else:
        return None