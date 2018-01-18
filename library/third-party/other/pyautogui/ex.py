import pyautogui as pg
import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# устанавливаю паузу после каждого вызова функции 
# pg.PAUSE = 1

# активируем средство безопасного выхода из программы
pg.FAILSAFE = True


# for i in range(3):
	# pg.moveTo(100, 100, duration=0.25)
	# pg.moveTo(100, 200, duration=0.25)
	# pg.moveTo(200, 200, duration=0.25)
	# pg.moveTo(200, 100, duration=0.25)

# pg.moveRel(300, -50, duration=0.2)

# time.sleep(10)
# pg.click()

# distance = 200

# while distance > 0:
# 	pg.dragRel(distance, 0, duration=0.2)
# 	distance -= 10
# 	pg.dragRel(0, distance, duration=0.2)
# 	pg.dragRel(-distance, 0, duration=0.2)
# 	distance -=10
# 	pg.dragRel(0, -distance, duration=0.2)

pg.scroll(50)