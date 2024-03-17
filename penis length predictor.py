# Система и имя нужно для очищения CMD от мусора
from os import system,name
# нужно для получения разрешения экрана
from win32api import GetSystemMetrics
# Надпись о загрузки появляется заранее
print("LOADING...")
# Средняя длина членов (вычислено из закрытой базы данных)
MEAN_LEN=15.76923076923077
# получаю из среднего арифметического разрешения пользователя поделённого на моё разрешение экрана коофицент размера для всех окон приложения
screencoof=((GetSystemMetrics(0)/2560)+(GetSystemMetrics(1)/1440))/2
# нужен для загрузки модели нейросети
from tensorflow.keras.models import load_model
# нужен для интерфейса
import customtkinter as ctk
# нужен для отображения членов в виде графиков
import matplotlib.pyplot as plt
# нужен для хранения данных
import numpy as np
# вывод название ОП (нужно для отладки)
print(name)
# создание окна
dataWin=ctk.CTk()
# установка разрешения (округлённый результат умножения разрешения 640x480 на коэффициент, операция нужна чтобы на всех мониторах соотношение всего экрана и окна были одинаковы)
dataWin.geometry(f'{round(640*screencoof)}x{round(480*screencoof)}')
# создание поля для ввода "рост"
hei=ctk.CTkEntry(master=dataWin,)
# создание поля для ввода "рост"
labhei=ctk.CTkLabel(master=dataWin,text='рост')
# установка на окно
labhei.pack()
hei.pack()

# создание поля для ввода "вес"
wei=ctk.CTkEntry(master=dataWin,)
# создание подсказки "вес"
labwei=ctk.CTkLabel(master=dataWin,text='вес')
# установка на окно
labwei.pack()
wei.pack()

# создание кнопки "возраст"
age=ctk.CTkEntry(master=dataWin,)
# создание подсказки "возраст"
labage=ctk.CTkLabel(master=dataWin,text='возраст')
# установка на окно
labage.pack()
age.pack()
# создание кнопки "Узнать длину члена"
button=ctk.CTkButton(master=dataWin,text='Узнать длину члена')
# функция get_result принимает рост вес и возраст
def get_result(height,weight,age):
    # занесение в массив полученных данных
    input_data = np.array([[float(height), float(weight), float(age)]])
    # ввод в нейросеть имеющихся данных
    prediction = model.predict(input_data)[0][0]
    # округление полученного от нейросети значения
    pepedton=round(prediction)
    # базовые настройки для графика
    fig, ax = plt.subplots()
    # если член короче нормы, то в начале ставится средняя длина, а полом её перекрывает предугаданная нейросетью длина
    if not prediction>MEAN_LEN:
        bar1 = ax.bar(1, MEAN_LEN, label=f'Средняя длина члена ({int(MEAN_LEN)} см)')
        bar2 = ax.bar(1, prediction, label=f'Длина твоего члена ({pepedton} см)')
    # в ином случае последовательность обратная
    else:
        bar1 = ax.bar(1, prediction, label=f'Длина твоего члена ({pepedton} см)')
        bar2 = ax.bar(1, MEAN_LEN, label=f'Средняя длина члена ({int(MEAN_LEN)} см)')

    # подсказки по двум осям графика
    ax.set_ylabel('Длина в СМ')
    ax.set_title('Сравнение')
    ax.set_xticks([1])
    ax.legend()

    # отображение графика
    plt.show()
    # очищение CMD
    system('cls' if name == 'nt' else 'clear')
# если по кнопки нажали левой клавишей мыши, то вызывается функция get_result с введёнными значениями трёх полей для ввода
button.bind('<Button-1>',lambda x:get_result(hei.get(),wei.get(),age.get()))
# отображение кнопки в окне
button.pack()

# загрузка модели
global model
model = load_model('penismodel.h5')

# очищение окна
system('cls' if name == 'nt' else 'clear')

# запуск цикла окна
dataWin.mainloop()