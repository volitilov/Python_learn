import pyautogui as pg
import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

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

# pg.scroll(50)

# im = pg.screenshot()

# time.sleep(10)
# pg.click(300, 200)
# pg.typewrite('Hello world', interval=0.25)

# ms = pg.alert(text='Hello python', button='OK')
ps = pg.password(text='password', title='enter password', 
	default='123', mask='*')
print(ps)