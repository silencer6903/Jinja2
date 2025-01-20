from jinja2 import Template


def render_city_dropdown(cities):
    """
    Генерує HTML-код для випадкового списку з містами, використовуючи шаблон Jinja2.

    Якщо `id` міста більше за 30, місто додається до списку як елемент <option>.
    Інакше назва міста відображається як текст у списку.

    Parameters:
        cities (list): Список міст, де кожен елемент є словником
                       із ключами 'id' (int) та 'city' (str).

    Returns:
        str: Згенерований HTML-код для випадкового списку.

    Приклад використання:
        cities = [{'id': 54, 'city': 'Odessa'},
                  {'id': 8, 'city': 'Lviv'}]
        html = render_city_dropdown(cities)
        print(html)
    """
    link = '''<select name="cities">
    {% for c in cities -%}
    {% if c['id'] > 30 -%}
        <option value="{{c['id']}}">{{c['city']}}</option>
    {% else -%}
        {{c['city']}}
    {% endif -%}
    {% endfor -%}
    </select>'''

    tm = Template(link)
    return tm.render(cities=cities)


# Приклад використання:
cities = [
    {'id': 54, 'city': 'Odessa'},
    {'id': 8, 'city': 'Lviv'},
    {'id': 93, 'city': 'Ternopil'},
    {'id': 33, 'city': 'Dnipro'},
    {'id': 22, 'city': 'Lutsk'},
    {'id': 55, 'city': 'Rivne'}
]

html = render_city_dropdown(cities)
print(html)
