team1_num = 6
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 350.4

output1 = "В команде Мастера кода участников: %d !" % team1_num
print(output1)

output2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(output2)

output3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(output3)

output4 = "Волшебники данных решили задачи за {:.2f} с !".format(team2_time)
print(output4)

output5 = f"Команды решили {score_1} и {score_2} задач."
print(output5)

challenge_result = ''
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

output6 = f"Результат битвы: {challenge_result}"
print(output6)

output7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"
print(output7)