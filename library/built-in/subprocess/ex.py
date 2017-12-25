import subprocess as sbp

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::

# запускает калькулятор
# sbp.Popen('/usr/bin/gnome-calculator')

# запускает sublime и открывает в нём файл
sbp.Popen(['/usr/bin/subl', 'small_prog/print_table.py'])