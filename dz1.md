В синхронной модели:

A отправляет запрос B. 100
B отправляет запрос C. 200
B получает ответ от C. 300
B отправляет запрос D. 400
B получает ответ D. 500
B отправляет ответ A. 600
Итого, один вызов f_B займет: 600 мс. Соответственно, 1000 таких вызовов займут: 600 мс * 1000 раз = 600 000 мс.
Тут мы не учитывали, что единицы мс, так как они сильно меньше полученного результата

Асинхронная модель:

А отправляет 1000 запросов B до 1000 мс 
На 101мс В начинает получать эти запросы с разницей в милисикунду, и каждую мс делать запросы то в D то в C всего 2000 запросов и последняя отправка в 2101 мс
С начнет получать запросы каждые 2 мс на 201мс и тут же возвращать их в B. последняя отправка в 2201мс
D начнет получать запросы кждые 2мс на 202мс и тут же возвращать их в B. последняя отправка в 2202мс
на 301мс B начнет получать запросы от C и D и получит их все до 2302мс и с 2102 мс начнет отправлять их в А. последняя отправка в 4102мс
А получит последний ответ в 4202 мс