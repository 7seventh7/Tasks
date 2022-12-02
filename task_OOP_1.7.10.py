class AppStore:

    blocked = True
    all_apps = []

    """Объявите класс AppStore - интернет-магазин приложений для устройств
    под iOS. В этом классе должны быть реализованы следующие методы:
    """

    def add_application(self, app):
        """добавление нового приложения app в магазин
        """
        self.all_apps.append(app)

    def remove_application(self, app):
        """удаление приложения app из магазина
        """
        self.all_apps.remove(app)

    def block_application(self, app):
        """блокировка приложения app (устанавливает локальное
        свойство blocked объекта app в значение True)
        """
        if app in self.all_apps:
            self.blocked = True
        else:
            print("No such application")

    def total_apps(self):
        """возвращает общее число приложений в магазине
        """
        return len(self.all_apps)


class Application:

    def __init__(self, name):

        self.name = name
        self.blocked = False


# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)

# store = AppStore()
# app_youtube = Application("Youtube")
# app_vk = Application("VK")
# store.add_application(app_youtube)
# store.add_application(app_vk)

# print(store.all_apps)
#
#
#
# store.remove_application(app_youtube)
#
# print(store.app)

# with open('logs.txt', 'a') as log:
#     print(AppStore.__dict__, file = log)
#     print('\n', file = log)
#     print('--------------------------------------------------', file = log)
#     print('\n', file = log)




