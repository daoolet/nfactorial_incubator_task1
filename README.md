<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#resume">Resume</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

[![screen.png](https://i.postimg.cc/KcfHNnqK/screen.png)](https://postimg.cc/jCWcqJrK)

nFactoiral Incubator 2024, Второй этап
Необходимо разработать веб-приложение, основанное на вселенной "Star Wars", позволяющее пользователям исследовать персонажей, планеты и космические корабли из франшизы.

Требования:
* Создание базового веб-макета
* Разработка страницы каталога планет, позволяющей пользователям исследовать различные планеты, представленные во вселенной "Звездных войн", с информацией об их климате, обитателях и примечательных достопримечательностях
* Реализация функции поиска позволяет пользователям искать персонажей, планеты и космические корабли по имени или ключевому слову
* Используйте API - [swapi]


### Built With

Так как я не знаю ни один JS framework. Решил сделать фронтэнд на Django Templates + Boostrap. К тому же есть небольшей бэк на Django для запросов к API.

* [![Django][djangoproject.com]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]


<!-- GETTING STARTED -->
## Getting Started

На уроках nFactorial Backend'23 я научился пользоваться [poetry] и с тех пор всегда использую его как альтернатива pip. Прошу обратить внимание  для запуска требуется установить [Python](https://www.python.org/).

### Prerequisites

Для начала необходимо установить poetry

* poetry
  ```sh
  pip install poetry
  ```

### Installation

1. Клонировать репо
   ```sh
   git clone https://github.com/daoolet/nfactorial_incubator_task1.git
   ```
2. Включить виртуальное окружение
   ```sh
   poetry shell
   ```
3. Установить зависимости
   ```sh
   poetry install
   ```
4. Запустить локально сервер
   ```py
   python manage.py runserver
   ```


<!-- RESUME -->
## Resume

Первое что я хотел бы отметить - это невозможность установить (via pip / poetry) библиотеку [swapi-python](https://github.com/phalt/swapi-python). Ругается именно на модуль ```ujson```. Я долго боролся с этой проблемой и решил не использовать готовую библиотеку. Для работы с API подключил библиотеку ```requests```, можно заметить, что для обработки запросов требуется время. Тем самым я не стал вытаскивать всю информацию json, а лишь часть. По причине отсуствия swapi-python не реализовал поиск. 

С точки зрения проектирования все GET-запросы обрабатываются в views.py, а результат выводится на шаблоны, к которым применены стили Boostrap. Для более красивого вывода информации использовал оригинальные цвета и шрифт Star Wars.

Одной из проблемой приложения является отправка запросов в реальном времени и не хранение результата в отдельном файле. Тем самым это занимает время, сайт "думает" при переходе на вкладки. Пологаю, эту проблему можно решить с готовой библиотекой swapi-python, где не требуется отправка запросов API.

<!-- CONTACT -->
## Contact

Daulet Khabidullin - [Linkedin] - dauletkhabidullin@gmail.com

Project Link: [GitHub repo](https://github.com/daoolet/nfactorial_incubator_task1.git)


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Оставлю полезные ссылки

* [Best README Template](https://github.com/othneildrew/Best-README-Template?tab=readme-ov-file#readme-top)
* [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
* []()



<!-- MARKDOWN LINKS & IMAGES -->
[swapi]: https://swapi.dev/
[poetry]: https://python-poetry.org/
[Linkedin]: https://www.linkedin.com/in/daoolet/


[djangoproject.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
