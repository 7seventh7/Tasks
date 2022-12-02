class Viber:

    list_of_massages = {}

    def __init__(self, msg):

        self.list_of_massages[msg] = False

    def add_message(self, msg):
        """добавление нового сообщения в список сообщений;
        """
        self.list_of_massages[msg] = False

    def remove_message(self, msg):
        """удаление сообщения из списка;
        """
        self.list_of_massages.pop(msg)

    def set_like(self, msg):
        """поставить/убрать лайк для сообщения msg
        (если лайка нет то он ставится, если уже есть, то убирается);
        """
        if msg in self.list_of_massages:
            if self.list_of_massages[msg] == False:
                self.list_of_massages[msg] = True
            else:
                self.list_of_massages[msg] = False

    def show_last_message(msg):
        """отображение последних сообщений;
        """
        pass

    @classmethod
    def total_messages(cls):
        """звращает общее число сообщений.
        """
        return len(cls.list_of_massages)



class Message:

    def __init__(self, text, fl_like = False):
        self.text = text
        self.fl_like = fl_like

    def get_message(self):
        return self.text

# m1 = Message('Привет, как дела?')
# m2 = Message('Как тебя зовут?')
# m3 = Message('Где ты работаешь?')
# v1 = Viber(m1)
# v2 = Viber(m2)
# v3 = Viber(m3)
# v3 = v2.set_like(m2)



# print(Viber.list_of_massages)
# print(Viber.total_messages())
#
# #print(Viber.__dict__)