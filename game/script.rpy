# init python:
    # import urllib2
    # import json

    # class Connection:
        # url = "http://localhost:8080/show/"

        # def __init__(self, id_results):
            # self.response = urllib2.urlopen(Connection.url + str(id_results))
            # self.json_data = self.response.read()
            # self.py_data = json.loads(self.json_data)

        # def close_connection(self):
            # self.response.close()

    # class TestCharacter:
        # def __init__(self):
            # self.__id_results = None
            # self.__username = None
            # self.__results = None

        # @property
        # def char_id(self):
            # return self.__id_results
        
        # @id_results.setter
        # def id_results(self, id_results):
            # self.__id_results = id_results
        
        # @property
        # def username(self):
            # return self.username
        
        # @username.setter
        # def username(self, username):
            # self.username = username
        
        # @property
        # def results(self):
            # return self.results
        
        # @results.setter
        # def results(self, results):
            # self.results = results
            
        # ####
        # too much getter, setter #
        # let's skip the rest.)

# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define h = Character('Харуко', color="#00FF00")
define p = Character('Пай-тян', color="#FFFF00")
define c = Character('Си-тян', color="#0000FF")
define d = Character('Сатаняша', color="#8B0000")
define a = Character('Ангел', color="#F0E68C")
define q = Character(' ', color="#808080", kind=nvl)
define u = Character('Преподаватель', color="#808080")
define m = Character('Мия', color="#EE82EE")
define k = Character('Киберпанк', color="#00FF7F")
define y = Character('Технарь', color="#66CDAA")
define b = Character('БрОтки', color="#FF7F50")
define v = Character('Джун', color="#808000")
define g = Character('Голос', color="#000000")


#Покормил котейку
define fed = False

#Количество правельных ответов
define rep = 0
define repp = 0
define reph = 0

# Игра начинается здесь:
label start:
   # python:
        # test_sar = TestCharacter()
        # sar_getter = Connection(2)
        # test_sar.id = sar_getter.py_data['IdResults']
        # test_sar.username = sar_getter.py_data['Username']
        # test_sar.results = sar_getter.py_data['Results']

        # sar_getter.close_connection()
        
        # IdResults = test_sar.id
        # Username = test_sar.username
        # Results = test_sar.results
    
label start_plot:     
            
    scene street
    with fade
    
    #"[username]"
    
    "Вы идете в университет..."
    
    show neko_2
    
    "По дороге в универ, вы заметили маленького котёнка..."
    
    menu:
        "Сделайте выбор:"
        
        "Покормить котейку":
            $ fed = True
            hide neko_2
            show neko_1
            "Вы покормили котейку..."
        "Пройти мимо":
            hide neko_2
            show neko_3
            "Вы прошли мимо, оставив котейку голодным..."
    
    "Идете дальше в универ..."
    hide neko_1
    hide neko_3
    scene univer
    with fade
    
    "Остановившись у входа, вы посмотрели расписание..."
    
    q "Расписание"
    q "Пн:" 
    q "1)ЯиМП (практика)"
    q "2)Матанализ (практика)"
    q "3)Матанализ (практика)"
    q "4)Базы данных (практика)"
    
    nvl clear
    
    "Вы подумали..."
    
    menu:
        "Может прогулять занятия?"
        
        "Нет, все же лучше сходить":
            jump univer
        "Пройти гулять, забив на пары...":
            jump street
    
    return
#Тут начало ветки общего теста    
label univer:
    scene univercor
    with fade
    
    "Вы зашли в универ..."
    
    "Поднимаетесь на 7 этаж..."
    
    "Заходите в аудиторию..."
    
    scene class_day
    
    show ctyan_smile
    
    show pytyan_smile at left
    
    show haruko_smile at right
    
    "В аудитории уже собрался народ..."
    
    "Вы сели на последних партах..."
    
    "Спустя некоторое время, зашел препод..."
    
    hide ctyan_smile
    
    hide pytyan_smile
    
    hide haruko_smile
    
    show prepod_1
    
    u "Так ребята, готовим двойные листочки..."
    
    "Точно... Сегодня же контрольная... Подумали вы..."
    
    "Препод проходит по рядам и раздает контрольную..."
    
    "Очередь дошла до вас... Вам выдали листок с работой..."
    
    scene univertest
    hide prepod_1
    "Вы приступаете к работе..."
    
    jump question1
    return

label question1:
    menu:
        "Вопрос 1: Какой оператор в Python используется для логического И?"
        
        "a) &":
            jump question2
        "b) &&":
            jump question2
        "c) and":
            $ rep += 1
            jump question2
        "d) AND":
            jump question2
    return

label question2:
    menu:
        "Вопрос 2: Какая функция в C++ используется для вывода на экран?"
        
        "a) print()":
            jump question3
        "b) cout()":
            $ rep += 1
            jump question3
        "c) show()":
            jump question3
        "d) display()":
            jump question3
    return

label question3:
    menu:
        "Вопрос 3: Какой цикл используется в Python для перебора коллекций по порядку?"
        
        "a) while":
            jump question4
        "b) for":
            $ rep += 1
            jump question4
        "c) foreach":
            jump question4
        "d) do-while":
            jump question4
    return

label question4:
    menu:
        "Вопрос 4: Какой тип данных в C++ используется для хранения строк?"
        
        "a) char":
            jump question5
        "b) int":
            jump question5
        "c) string":
            $ rep += 1
            jump question5
        "d) float":
            jump question5
    return
    
label question5:
    menu:
        "Вопрос 5: Какая функция в Python используется для чтения ввода с клавиатуры?"
        
        "a) input()":
            $ rep += 1
            jump questionfin
        "b) read()":
            jump questionfin
        "c) get_input()":
            jump questionfin
        "d) scanf()":
            jump questionfin
    return
    
label questionfin:
    "Вы написали тест и сдали напроверку..."
    
    show prepod_1
    
    "Спустя некоторое время препод оглосил результаты..."
    
    hide prepod_1
    
    "У вас [rep] правильных ответов"
    
    if rep >= 3:
        "После успешно пройденного теста вы вышли на улицу..."
        jump linetestwin
    else:
        "После проваленного теста к вам подошел препод"
        scene univercor
        with fade
        show prepod_1
        u "Ты плохо написал тест, зайди на кафедру после занятий..."
        
        jump linetestlose
    return
    
label linetestwin:
    scene night_univer
    with fade
    
    "Уже вечер..."
    
    "Вас кто-то окликнул..."
    
    show miya_smile
    
    "Это была ваша одногрупница... Вроде её звали Мия..."
    
    m "Привет! Слушай ты же отлично написал тест..."
    hide miya_smile
    show miya_happy
    
    m "Можешь мне помочь с этой дисциплиной..."
    hide miya_happy
    show miya_smile
    
    m "А то скоро контрольная, а я не готова..."
    
    hide miya_smile
    
    "Хорошо... Вы отправились к ней домой..."
    scene home_miya
    "Придя к ней домой, вы попили чаю и сели решать тесты"
    scene room_miya
    
    jump question6
    return

label question6:
    menu:
        "Вопрос 1: Какое из этих условных выражений используется для проверки равенства двух значений в Python?"
        
        "a) ==":
            $ rep += 1
            jump question7
        "b) !=":
            jump question7
        "c) <=":
            jump question7          
        "d) >=":
            jump question7
    return

label question7:
    menu:
        "Вопрос 2: Какой из этих типов данных используется для хранения целых чисел в C++?"
        
        "a) char":
            jump question8
        "b) float":
            jump question8
        "c) double":
            jump question8
        "d) int":
            $ rep += 1
            jump question8
    return

label question8:
    menu:
        "Вопрос 3: Какие операторы используются для инкремента переменной в Python?"
        
        "a) ++":
            jump question9
        "b) —":
            jump question9
        "c) +=":
            $ rep += 1
            jump question9
        "d) *=":
            jump question9
    return
label question9:
    menu:
        "Вопрос 4: Какой из этих циклов используется для повторения кода определенное количество раз в C++?"
        
        "a) for":
            $ rep += 1
            jump question10
        "b) while":
            jump question10
        "c) do-while":
            jump question10
        "d) switch":
            jump question10
    return
label question10:
    menu:
        "Вопрос 5: Какой тип данных используется для хранения дробных чисел в Python?"
        
        "a) int":
            jump questionfin2
        "b) bool":
            jump questionfin2
        "c) float":
            $ rep += 1
            jump questionfin2
        "d) str":
            jump questionfin2
    return
label questionfin2:

    if rep >= 6:
        scene kafe
        with fade
        
        show miya_happytwo
        "Через 3 дня вы с Мией успешно сдали тест..."
        
        "Мия пригласила вас на ужин... Отпраздновать прошедшую контрольную..."
        
        "Ваш результат [rep] / 10"
    else:
        scene miya_lose
        with fade
        "Через 3 дня вы с Мией завилили тест..."
        
        "Мия с вами больше не общается..."
        
        "Ваш результат [rep] / 10"
    return
label linetestlose:
    scene kafedra
    with fade
    
    "После занятий вы зашли на кафедру"
    show prepod_2
    
    u "Ты плохо написал тест и должен его переписать."
    
    u "В течении 3-ёх дней будешь ходить ко мне и нарешивать тесты..."
    
    hide prepod_2
    scene black
    with fade
    
    "Спустя 3 дня..."
    
    scene univertest
    with fade
    show prepod_2
    
    u "Готовим двойные листочки, убираем телефоны со столов... На парте только листок и ручка..."
    
    "Вам выдали контрольную..."
    hide prepod_2
    jump questionlose6
    return
label questionlose6:
    menu:
        "Вопрос 1: Какое из этих условных выражений используется для проверки равенства двух значений в Python?"
        
        "a) ==":
            $ rep += 1
            jump questionlose7
        "b) !=":
            jump questionlose7
        "c) <=":
            jump questionlose7          
        "d) >=":
            jump questionlose7
    return

label questionlose7:
    menu:
        "Вопрос 2: Какой из этих типов данных используется для хранения целых чисел в C++?"
        
        "a) char":
            jump questionlose8
        "b) float":
            jump questionlose8
        "c) double":
            jump questionlose8
        "d) int":
            $ rep += 1
            jump questionlose8
    return

label questionlose8:
    menu:
        "Вопрос 3: Какие операторы используются для инкремента переменной в Python?"
        
        "a) ++":
            jump questionlose9
        "b) —":
            jump questionlose9
        "c) +=":
            $ rep += 1
            jump questionlose9
        "d) *=":
            jump questionlose9
    return
label questionlose9:
    menu:
        "Вопрос 4: Какой из этих циклов используется для повторения кода определенное количество раз в C++?"
        
        "a) for":
            $ rep += 1
            jump questionlose10
        "b) while":
            jump questionlose10
        "c) do-while":
            jump questionlose10
        "d) switch":
            jump questionlose10
    return
label questionlose10:
    menu:
        "Вопрос 5: Какой тип данных используется для хранения дробных чисел в Python?"
        
        "a) int":
            jump questionfinlose2
        "b) bool":
            jump questionfinlose2
        "c) float":
            $ rep += 1
            jump questionfinlose2
        "d) str":
            jump questionfinlose2
    return
label questionfinlose2:

    if rep >= 6:
        "Вы успешно написали контрольную..."
        
        "После уроков..."
        scene finalteach
        with fade
        "Препод позвал вас поесть рамена"
        
        "Ваш результат [rep] / 10"
    else:
        "Вы провалили контрольную..."
        show class_day
        with fade
        show bro_1 at left
        show bro_2
        show bro_42 at right
        "Вас окружают брОтки"
        
        b "Братан, забей на конрошу!"
        
        b "Погнали в караоке"
        hide bro_1
        hide bro_2
        hide bro_42
        
        scene karaoke
        with fade
        
        show bro_12 at left
        show bro_22
        show bro_4 at right
        
        "Ваш результат [rep] / 10"
    return
#Тут конец ветки общего теста
#Начало веткок по С++ и Питону
label street:
    scene street
    with fade
    "Вы пошли гулять..."
    
    scene streettwo
    
    "Решили зайти в пятерочку через дорогу..."
    
    "Переходя дорогу..."
    scene gruzovik
    with fade
    
    scene black
    with fade
    
    "ВАС СБИЛ ГРУЗОВИК..."
    
    if fed:
        jump paradise
    else:
        jump hell
    
    return
#Тута начало ветки рая   
label paradise:
    scene paradise
    with fade

    "Вы попали в рай!"
    
    show angel_smile
    
    "Перед вами стоит ангел..."
    
    show angel_happy
    
    a "Приветствую тебя в раю!"
    
    show angel_surprise
    
    a "Я ангел хранитель С++"
    
    a "Ты совершил хороший потупок покормив котёнка..."
    
    a "Я дам тебе возможность переродиться в другом мире... Но с одним условием..."
    
    a "Ты должен пройти тест... По программированию естественно..."
    
    a "Если ответишь хотя бы половину правильно, то ты переродишься..."
    
    "Ангел дает вам тест..."
    
    jump questioncplus1
    return
    
label questioncplus1:
    menu:
        "Вопрос 1: Что такое нулевой указатель в C++?"
    
        "a) Указатель, указывающий на первый элемент":
            jump questioncplus2
        "b) Указатель, указывающий на последний элемент":
            jump questioncplus2
        "c) Указатель, не указывающий ни на один объект":
            $ repp += 1
            jump questioncplus2
        "d) Указатель, равный нулю":
            jump questioncplus2
    return
label questioncplus2:
    menu:
        "Вопрос 2: Какой оператор используется для динамического выделения памяти в С++?"
    
        "a) new":
            $ repp += 1
            jump questioncplus3
        "b) malloc":
            jump questioncplus3
        "c) calloc":
            jump questioncplus3
        "d) free":
            jump questioncplus3
    return
label questioncplus3:
    menu:
        "Вопрос 3: Как объявить функцию в С++?"
    
        "a) function_name":
            jump questioncplus4
        "b) function name ()":
            jump questioncplus4
        "c) int function_name ()":
            jump questioncplus4
        "d) void function_name ()":
            $ repp += 1
            jump questioncplus4
    return
label questioncplus4:
    menu:
        "Вопрос 4: Какой оператор используется для ввода данных с клавиатуры в С++?"
    
        "a) cin":
            $ repp += 1
            jump questioncplus5
        "b) cout":
            jump questioncplus5
        "c) scanf":
            jump questioncplus5
        "d) printf":
            jump questioncplus5
    return
label questioncplus5:
    menu:
        "Вопрос 5: Что такое виртуальный деструктор в C++?"
    
        "a) Метод для создания нового объекта":
            jump questioncplusfin
        "b) Метод для уничтожения объекта":
            jump questioncplusfin
        "c) Метод, который может быть переопределен в наследниках":
            $ repp += 1
            jump questioncplusfin
        "d) Метод, который не может быть вызван напрямую":
            jump questioncplusfin
    return
label questioncplusfin:
    scene paradise
    show angel_smile
    "Вы закончили писать тест и отдали его ангелу на проверку..."
    
    "Спустя некоторое время..."
    
    show angel_surprise
    
    a "Я проверил тест..."
    
    if repp >= 3:
        show angel_happy
        
        a "Ты выполнил мои условия, я дам тебе переродиться в другом мире и начать жизнь с чистого листа..."
        
        scene black
        with fade
        
        jump isekai
    else:
        show angel_disgust
        
        a "Ты не выполнил мои условия, я не могу позволить тебе переродиться..."
        
        scene black
        with fade
        
        "Зазвенел будильник"
        
        scene bedroom_day
        
        "Вы проснулись... В своей кровати..."
        
        "Сон... Это был просто сон..."
        
        "На будильнике 7:00, пора вставать..."
        
        jump home
    return
label isekai:
    "Вы переродились в другом мире"
    scene cyberpunk
    show cyber
    k "Wake the fuck up, Samurai! We have a city to burn!"
    
    k "Но для начала... Сделаем тебе апгрейд..."
    hide cyber
    "Спустя некоторое время..."
    scene cybergar
    with fade
    show cyber at left
    show master_smile at right
    
    k "Проснулся?"
    
    y "Давай проверим как работает твой чип..."
    
    y "Пройди этот легкий тест..."
    
    jump cybertest1
    return
label cybertest1:
    menu:
        "Вопрос 1: Какой знак обозначает комментарии в C++?"
        
        "a) //":
            $ repp += 1
            jump cybertest2
        "b) /*":
            jump cybertest2
        "c) #":
            jump cybertest2
        "d) //":
            jump cybertest2
    return
label cybertest2:
    menu:
        "Вопрос 2: Что используется для объявления переменных в C++?"
        
        "a) var":
            jump cybertest3
        "b) const":
            jump cybertest3
        "c) int":
            $ repp += 1
            jump cybertest3
        "d) string":
            jump cybertest3
    return
label cybertest3:
    menu:
        "Вопрос 3: Какой оператор используется для выполнения условной операции?"
        
        "a) if-else":
            $ repp += 1
            jump cybertest4
        "b) for":
            jump cybertest4
        "c) while":
            jump cybertest4
        "d) switch":
            jump cybertest4
    return
label cybertest4:
    menu:
        "Вопрос 4: Какой оператор используется для работы с указателями в C++?"
        
        "a) &":
            jump cybertest5
        "b) *":
            $ repp += 1
            jump cybertest5
        "c) ::":
            jump cybertest5
        "d) ->":
            jump cybertest5
    return
label cybertest5:
    menu:
        "Вопрос 5: Как объявить функцию в C++?"
        
        "a) func myFunction()":
            jump cybertestfin
        "b) void myFunction()":
            $ repp += 1
            jump cybertestfin
        "c) int myFunction()":
            jump cybertestfin
        "d) myFunction()":
            jump cybertestfin
    return
label cybertestfin:
    if repp >= 6:
        hide master_smile
        show master_happy at right
        show cyber at left
        y "Отлично! Ты прошел тест..."
        
        k "Ты готов... Но запомни..."
        
        k "Словить пулю в этом городе гораздо легче, чем заболеть."
        scene cyberpunktwo
        with fade
        "Ваш результат [repp] / 10"
    else:
        hide master_smile
        show master_angry at right
        show cyber at left
        y "Возможно произошел сбой в системе..."
        
        y "Подожди пока я не восстановлю её..."
        
        "Ваш результат [repp] / 10"
    return
label home:
    scene bedroom_day
    "Вы задумались о будующем..."
    
    "Кем я буду в будущем?"
    scene black
    with fade
    "Прошло 10 лет..."
    scene badroomtwo
    with fade
    "Вы стали учителем информатики в школе"
    
    "Так на завтра надо составить тест..."
    
    jump cybertesth1
    return
label cybertesth1:
    menu:
        "Вопрос 1: Какой знак обозначает комментарии в C++?"
        
        "a) //":
            $ repp += 1
            jump cybertesth2
        "b) /*":
            jump cybertesth2
        "c) #":
            jump cybertesth2
        "d) //":
            jump cybertesth2
    return
label cybertesth2:
    menu:
        "Вопрос 2: Что используется для объявления переменных в C++?"
        
        "a) var":
            jump cybertesth3
        "b) const":
            jump cybertesth3
        "c) int":
            $ repp += 1
            jump cybertesth3
        "d) string":
            jump cybertesth3
    return
label cybertesth3:
    menu:
        "Вопрос 3: Какой оператор используется для выполнения условной операции?"
        
        "a) if-else":
            $ repp += 1
            jump cybertesth4
        "b) for":
            jump cybertesth4
        "c) while":
            jump cybertesth4
        "d) switch":
            jump cybertesth4
    return
label cybertesth4:
    menu:
        "Вопрос 4: Какой оператор используется для работы с указателями в C++?"
        
        "a) &":
            jump cybertesth5
        "b) *":
            $ repp += 1
            jump cybertesth5
        "c) ::":
            jump cybertesth5
        "d) ->":
            jump cybertesth5
    return
label cybertesth5:
    menu:
        "Вопрос 5: Как объявить функцию в C++?"
        
        "a) func myFunction()":
            jump cybertesthfin
        "b) void myFunction()":
            $ repp += 1
            jump cybertesthfin
        "c) int myFunction()":
            jump cybertesthfin
        "d) myFunction()":
            jump cybertesthfin
    return
label cybertesthfin:
    if repp >= 6:
        
        "Думаю такого теста им хватит..."
        
        "Вообщем... Мне 32 и я счастлив..."
        
        scene winfin
        with fade
        
        "Ваш результат [repp] / 10"
    else:
        
        "Надо бы переделать..."
        
        "На следующий день..."
        
        scene losefin
        with fade
        
        "Ваш результат [repp] / 10"
    return
#Тута начало ветки ада
label hell:
    scene hell
    with fade
    
    "Вы попали в ад!"
    
    show demon_smile
    
    "Перед вами стоит демон..."
    
    show demon_happy
    
    d "Ах-ха-ха-ха! Ещё один упал ко мне..."
    
    d "В АД! Ах-ха-ха-ха!"
    
    show demon_smile
    
    d "Нравятся мне такие равнодушные как ты... Хе-хе..."
    
    d "Ладно, дам тебе возможность вернуться обратно..."
    
    d "Но ты должен будешь выпонить мой ужасно сложный тест! Бу-га-га!"
    
    d "Если ответишь правильно на половину, то я отпущу тебя..."
    
    d "Если же ты завалишь тест, то будешь вечно у меня в аду гореть!"
    
    show demon_happy
    
    d "Ах-ха-ха-ха!"
    
    "Демон дает вам тест"
    
    jump questionpy1
    return

label questionpy1:
    menu:
        "Вопрос 1: Какой оператор используется для объединения двух списков в Python?"
        
        "a) ||":
            jump questionpy2
        "b) &&":
            jump questionpy2
        "c) //":
            jump questionpy2
        "d) +":
            $ reph += 1
            jump questionpy2
    return
    
label questionpy2:
    menu:
        "Вопрос 2: Какой метод нужно использовать, чтобы создать копию списка в Python?"
        
        "a) copy()":
            $ reph += 1
            jump questionpy3
        "b) insert()":
            jump questionpy3
        "c) remove()":
            jump questionpy3
        "d) pop()":
            jump questionpy3
    return
    
label questionpy3:
    menu:
        "Вопрос 3: Какой символ используется для создания комментария в Python?"
        
        "a) //":
            jump questionpy4
        "b) #":
            $ reph += 1
            jump questionpy4
        "c) *":
            jump questionpy4
        "d) !":
            jump questionpy4
    return
    
label questionpy4:
    menu:
        "Вопрос 4: Как вывести текст на экран в Python?"
        
        "a) print()":
            $ reph += 1
            jump questionpy5
        "b) input()":
            jump questionpy5
        "c) scan()":
            jump questionpy5
        "d) write()":
            jump questionpy5
    return
    
label questionpy5:
    menu:
        "Вопрос 5: Каким методом можно удалить последний элемент из списка в Python?"
        
        "a) remove()":
            jump questionpyfin
        "b) delete()":
            jump questionpyfin
        "c) pop()":
            $ reph += 1
            jump questionpyfin
        "d) discard()":
            jump questionpyfin
    return
    
label questionpyfin:
    scene hell
    show demon_sad
    "Вы закончили писать тест..."
    
    "Сатаняша взяла тест на проверку..."
    
    "Спустя некоторое время..."
    
    if reph >=3:
        show demon_happy
        d "Ах-ха-ха-ха! Тебе удалось успешно сдать мой ужасно сложный тест!"
        
        d "Так и быть... Я отпущу тебя..."
        
        d "Все же я демон... Слов на ветер не бросаю..."
        
        scene black
        with fade
        
        "Вы немного приоткрыли глаза..."

        scene sky
        with fade
        scene black
        with fade
        "Вы отрубились..."
        jump hospital
    else:
        show demon_happy
        d "Бу-га-га! Как я и думала... Ты завалил мой ужасно сложный тест!"
        
        d "Я отправлю тебя в на самое дно бездны!"
        
        scene black
        with fade
        
        "Вас отправили на днище бездны..."
        jump abyss
    return
label hospital:
    "Вас доставили в больничку..."
    
    scene med
    with fade
    
    "Вы проснулись..."
    
    show bro_3
    
    v "Братан, ты как..."
    
    v "Врач попросил тебе тест передать..."
    
    jump hosptest1
    return
label hosptest1:
    menu:
        "Вопрос 1: Какие типы данных есть в языке Python?"
        
        "a) int, float, double, boolean":
            jump hosptest2
        "b) int, float, bool, str":
            $ reph += 1
            jump hosptest2
        "c) double, float, char, bool":
            jump hosptest2
        "d) int, float, long, string":
            jump hosptest2
    return
label hosptest2:
    menu:
        "Вопрос 2: Что такое функция в Python?"
        
        "a) это переменная, которая хранит значение":
            jump hosptest3
        "b) это константа, которая всегда имеет одно и то же значение":
            jump hosptest3
        "c) это синтаксически оформленный блок кода, который можно вызывать и использовать многократно":
            $ reph += 1
            jump hosptest3
        "d) это условие, которое проверяет истинность или ложность утверждения":
            jump hosptest3
    return
label hosptest3:
    menu:
        "Вопрос 3: Какой метод вызывается для получения длины строки?"
        
        "a) lenght()":
            jump hosptest4
        "b) length()":
            jump hosptest4
        "c) len()":
            $ reph += 1
            jump hosptest4
        "d) size()":
            jump hosptest4
    return
label hosptest4:
    menu:
        "Вопрос 4: Что делает функция print()?"
        
        "a) выводит на экран результат вычислений":
            $ reph += 1
            jump hosptest5
        "b) записывает данные в файл":
            jump hosptest5
        "c) удаляет файл":
            jump hosptest5
        "d) выполняет чтение файлов":
            jump hosptest5
    return
label hosptest5:
    menu:
        "Вопрос 5: Каким образом можно перевести строку в целое число?"
        
        "a) str_var.to_int()":
            jump hosptestfin
        "b) int(str_var)":
            $ reph += 1
            jump hosptestfin
        "c) str_var.convert_to_int()":
            jump hosptestfin
        "d) to_int(str_var)":
            jump hosptestfin
    return
label hosptestfin:
    "Дверь открывается"
    
    hide bro_3
    show bro_1 at left
    show bro_2
    show bro_42 at right
    b "Братан!!! Ты как!!! Живой?"
    hide bro_1
    hide bro_2
    hide bro_42
    show bro_12 at left
    show bro_22
    show bro_4 at right
    
    b "Поправляйся!"
    
    "Ваш результат [reph] / 10"
    return
label abyss:
    scene black
    with fade
    
    g "Решай...Решай...*шепотом*"
    scene abyssb
    with fade
    g "Решай тесты на Python...*шепотом*"
    
    g "Решай...Решай...*шепотом*"
    jump abysstest1
    return
label abysstest1:
    menu:
        "Вопрос 1: Какие типы данных есть в языке Python?"
        
        "a) int, float, double, boolean":
            jump abysstest2
        "b) int, float, bool, str":
            $ reph += 1
            jump abysstest2
        "c) double, float, char, bool":
            jump abysstest2
        "d) int, float, long, string":
            jump abysstest2
    return
label abysstest2:
    menu:
        "Вопрос 2: Что такое функция в Python?"
        
        "a) это переменная, которая хранит значение":
            jump abysstest3
        "b) это константа, которая всегда имеет одно и то же значение":
            jump abysstest3
        "c) это синтаксически оформленный блок кода, который можно вызывать и использовать многократно":
            $ reph += 1
            jump abysstest3
        "d) это условие, которое проверяет истинность или ложность утверждения":
            jump abysstest3
    return
label abysstest3:
    menu:
        "Вопрос 3: Какой метод вызывается для получения длины строки?"
        
        "a) lenght()":
            jump abysstest4
        "b) length()":
            jump abysstest4
        "c) len()":
            $ reph += 1
            jump abysstest4
        "d) size()":
            jump abysstest4
    return
label abysstest4:
    menu:
        "Вопрос 4: Что делает функция print()?"
        
        "a) выводит на экран результат вычислений":
            $ reph += 1
            jump abysstest5
        "b) записывает данные в файл":
            jump abysstest5
        "c) удаляет файл":
            jump abysstest5
        "d) выполняет чтение файлов":
            jump abysstest5
    return
label abysstest5:
    menu:
        "Вопрос 5: Каким образом можно перевести строку в целое число?"
        
        "a) str_var.to_int()":
            jump abysstestfin
        "b) int(str_var)":
            $ reph += 1
            jump abysstestfin
        "c) str_var.convert_to_int()":
            jump abysstestfin
        "d) to_int(str_var)":
            jump abysstestfin
    return
label abysstestfin:
    "Вы бесконечно решаете тесты..."
    
    "Ваш результат [reph] / 10"
    return