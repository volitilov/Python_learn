import re

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::

my_text = """
	The ANSI/VT100 terminals and terminal emulators are 
	not just able to display black and white text; they 
	can display colors and formatted texts thanks to 
	escape sequences. Those sequences are composed of 
	the Escape character (often represented by 
	“^[” or “<Esc>”) followed by some other characters: 
	“<Esc>[FormatCodem”.vasy@mail.ru, djon-bondjon@gmail.com
"""

text_look_for = r'[\w\.-]+@\w+\.\w+'

allresults = re.findall(text_look_for, my_text)
print(len(allresults))