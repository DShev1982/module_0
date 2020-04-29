import numpy as np

def game_core_v3(number):
    '''Двоичный поиск - в каждой итерации массив делится на две части
    , сравниваем срединное значение с искомым. Принимаем решение
    , что может находиться только в левой или только в правой части массива 
    (оказалось больше или меньше границы раздела). Отсекаем ту часть
    , в которой искомого значения быть не может'''
    count = 0
    range_start = 0
    range_finish = 100
    while True:
        count += 1
        range_middle = (range_start + range_finish)//2
        if number > range_middle:
            range_start = range_middle
        elif number < range_middle:
            range_finish = range_middle
        else:
            break
    return(count) # выход из цикла, если угадали
        
    
def score_game(game_core_v3):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(100, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)