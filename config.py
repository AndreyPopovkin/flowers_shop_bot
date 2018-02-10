# -*- coding: utf-8 -*-

from catalog import Catalog

# TEST
token = '325287100:AAGlQ6zXH0lM28Kx5MPgEReMOyfCeP8REYc'
chanel = -1001145764283

# TEXT
main_menu = 'Основное меню'
main_menu_keyboard = [
    'Наш каталог',
    'Доставка',
    'О нас',
    'Контакты',
    'Скидки и бонусы',
]
back_button = 'Назад'

catalog = Catalog('Наш каталог', [
    Catalog('Букеты', [
        Catalog('Хризантемы', [Catalog('Букет 1'), Catalog('Букет 2')]),
        Catalog('Пионы', [Catalog('Букет 3'), Catalog('Букет 4')]),
    ]),
    Catalog('Розы', [
        Catalog('Красные', [Catalog('Букет 5')]),
        Catalog('Белые', [Catalog('Букет 6')]),
    ]),
    Catalog('Подарки', [
        Catalog('Красные', [Catalog('Букет 7')]),
        Catalog('Белые', [Catalog('Букет 8')]),
    ]),
])


# catalog = [
#     'Букеты',
#     'Розы',
#     'Подарки',
# ]
# bouquets = [
#     'Хризантемы',
#     'Пионы',
# ]
# roses = [
#     'Красные розы',
#     'Белые розы',
# ]
# presents = [
#     'Игрушки из цветов',
#     'Корзины с цветами',
# ]

deputates = 'Депутаты'
menu_return = 'Нажмите кнопку "Назад", чтобы вернуться в основное меню'
now_msg = 'Вы также можете узнать, что происходит именно сейчас'
now = 'Что сейчас происходит?'
FAQ = {
    'Как пройти в Государственную Думу?' : [
        'Георгиевский переулок, д.2, 10-й подъезд',
        55.758721,
        37.614795,
    ],
    'Как пройти в Малый Манеж?' : [
        'Георгиевский переулок, д.3/3',
        55.759630,
        37.615327,
    ]
}
contacts = '_INSTAGRAM_: [@molparlamrf](https://www.instagram.com/molparlamrf/)\n\n_TELEGRAM_: @zotovmedia\n\n'\
           '_VK_: https://vk.com/forumgd2017\n\n_Почта_: mp-rf@mail.ru'
cancel = 'Для отмены и возврата в меню отправьте /start'
cancelled = 'Отменено'
name = 'Ваше имя:'
contact = 'Ваши почта:'
offer = 'Ваше предложение:'
thanks = '_{}_, спасибо за ваш отзыв! В близжайшее время мы рассмотрим ваш вопрос и вышлем ответ по данным контактам:\n_{}_'
error = 'Что-то пошло не так...'

# PHOTOS

botograth_logo = 'AgADAgAD2qgxG8UeWUhPeTYTOwVRmcf7Mg4ABFf7JGovAAFinLeRAAIC'
botograth_caption = 'В случае обнаружения некорректной работы или предложений по совершенствованию Telegram бота, '\
                    'Вы можете обратиться с этим к разработчикам!'
our_contacts = 'Контакты для оперативной связи и предложений:\n\n_Почта_: '\
               'botograth@gmail.com\n\n_Telegram_: @botograth\_adm\n\n_VK_: https://vk.com/botograth'