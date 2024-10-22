from time import sleep


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age


class UrTube:
    users = []
    videos = []
    current_user = None

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def add(self, *args):  # Закидывает в список обьекты кортежами потому что передаем 2 обьекта в ur.add(v1, v2)
        ur.videos.append(args)

    def get_videos(self, keyword):  # ur.add(v1, v2)  = Внутри списка кортеж с двумя обьектами
        # ur.add(v3) = такая команда добавит еще один кортеж
        list_name = []
        keyword = keyword.upper()
        for i in ur.videos:
            if (len(i)) == 1:
                obj = (i[0].title.upper())
                if keyword in obj:
                    list_name.append(i[0].title)
            if (len(i)) != 1:
                for j in i:
                    obj = (j.title.upper())
                    if keyword in obj:
                        list_name.append(j.title)
        return list_name

    # def watch_video(self, film_name):

    def register(self, nickname, password, age):
        list_name = []
        for i in ur.users:
            list_name.append(i.nickname)
        if nickname in list_name:
            print(f'Пользователь {nickname} уже существует')
        else:
            ur.users.append(User(nickname, password, age))
            ur.current_user = nickname

    def log_out(self):
        ur.current_user = None

    def log_in(self, nickname, password):
        password = hash(str(password))
        for i in ur.users:
            if (nickname == i.nickname) and (password == i.password):
                ur.current_user = nickname

    def watch_video(self, keyword):
        for i in ur.videos:

            if (len(i)) == 1:
                age = 0
                for i in ur.users:
                    if ur.current_user == i.nickname:
                        age = i.age
                if keyword == i[0].title and ur.current_user == None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')

                elif keyword == i[0].title and ur.current_user != None and age >= 18:
                    print('sek sleep')
                    du = 0
                    while du < j.duration:
                        du += 1
                        print(du)
                        sleep(0.5)
                    if du == j.duration:
                        print('Конец видео')

            if (len(i)) != 1:

                for j in i:
                    age = 0
                    for i in ur.users:
                        if ur.current_user == i.nickname:
                            age = i.age
                    if keyword == j.title and ur.current_user == None:
                        print('Войдите в аккаунт, чтобы смотреть видео')
                    elif keyword == j.title and age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')

                    elif keyword == j.title and ur.current_user != None and age >= 18:
                        du = 0
                        while du<j.duration:
                            du +=1
                            print(du)
                            sleep(0.5)
                        if du==j.duration:
                            print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
