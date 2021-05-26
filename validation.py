def validation(message):
    messages = message.split("\n")
    count = len(messages)
    if (count > 4):
        return ([False, "максимум 4 позиции"])
    price = []
    artical = []
    title = []
    for i in range(count):
        messages[i] = messages[i].split(',')
        if (len(messages[i]) != 3):
            return ([False, "неверный ввод данных\nНазвание товара, артикул, цена"])
        if (len(messages[i][0].strip()) > 13):
            return ([False, "слишком длинное название"])
        if (len(messages[i][2].strip()) > 6):
            return ([False, "слишком большая цена"])
        price.append(messages[i][2].strip())
        artical.append(messages[i][1].strip())
        title.append(messages[i][0].strip())
    return ([True, {'title': title, 'artical': artical, 'price': price, 'quantity': count}])