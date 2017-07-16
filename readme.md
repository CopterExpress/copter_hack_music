ROS-модуль для упрощения работы с музыкальным сервером хакатона Copter Hack 2017.
=================================================================================

ROS-Сервисы:
------------

`~get` (`copter_hack_music/GetMusic`)

Скачать музыку для анализа и воспроизведения. Файл сохраняется в папку `~/music`.

`~play` (`copter_hack_music/PlayMusic`)

Начать воспроизведение.

`~stop` (`std_srvs/Trigger`)

Остановить воспроизведение.

Пример использования из python
------------------------------

```python
import os
import time
import rospy
from std_srvs.srv import Trigger
from copter_hack_music.srv import GetMusic, PlayMusic

rospy.init_node('node_name')

# Создаем прокси к сервисам

get_music = rospy.ServiceProxy('/music/get_music', GetMusic)
play_music = rospy.ServiceProxy('/music/play', PlayMusic)
stop_music = rospy.ServiceProxy('/music/stop', Trigger)

# Получить музыку:

get_music()

# success: True
# filename: song1.wav
# message: ''

# Полученный файл для анализа сохранен в ~/music/song1.wav

# Вопроизвести музыку:

play_music(filename='song1.wav')

# Воспроизвести музыку с задержкой в 5 секунд:

play_music(filename='song1.wav', start=time.time() + 5)

# Остановить музыку

stop_music()
```

Установка
---------

Скачайте и соберите пакет с помощью Catkin:

```bash
cd catkin_ws/src
git clone
cd ..
catkin_make --pkg=copter_hack_music
```

Запуск
------

```bash
roslaunch copter_hack_music copter_hack_music.launch
```
