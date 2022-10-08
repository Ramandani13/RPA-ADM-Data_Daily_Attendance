import pyautogui as pag
from time import sleep
from datetime import datetime,timedelta

def input_tanggal():
	hariini = (datetime.now().strftime("%d-%m-%Y"))
	tgl = pag.prompt(title="Masukan Tanggal", default=hariini)
	return tgl


sleep(3)
edge = pag.locateCenterOnScreen("edge.png")
print(edge)
pag.moveTo(edge)
pag.click(clicks=2, interval=0.25)


sleep(2)
user = pag.locateCenterOnScreen("userid.png")
print(user)
pag.moveTo(user)
pag.moveTo(user.x , user.y + 30)
pag.click()
pag.write("vu08a12")

password = pag.locateCenterOnScreen("password.png")
print(password)
pag.moveTo(password)
pag.moveTo(password.x , password.y + 30)
pag.click()
pag.write("yamaha06*")

loginbutton = pag.locateCenterOnScreen("login.png")
print(loginbutton)
pag.moveTo(loginbutton)
pag.click()

sleep(2)
attendance = pag.locateCenterOnScreen("atendance.png")
print(attendance)
pag.moveTo(attendance)
pag.click()

attendance = pag.locateCenterOnScreen("atend_daily.png")
print(attendance)
pag.moveTo(attendance)
pag.click()


sleep(2)
if __name__ == "__main__":
	tglawal = input_tanggal()

sleep(1)
dated = pag.locateCenterOnScreen("date.png")
pag.moveTo(dated)
pag.moveTo(dated.x + 150, dated.y)
pag.click()
pag.press("backspace", presses=10)
pag.write(tglawal)

sleep(1)
dated = pag.locateCenterOnScreen("date.png")
pag.moveTo(dated)
pag.moveTo(dated.x + 330, dated.y)
pag.click()
pag.press("backspace", presses=10)
pag.write(tglawal)

sleep(1)
dated = pag.locateCenterOnScreen("date.png")
pag.moveTo(dated)
pag.moveTo(dated.x + 770, dated.y)
pag.click()

sleep(1)
alll = pag.locateCenterOnScreen("2222.png")
pag.moveTo(alll)
pag.moveTo(alll.x - 60, alll.y)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("confirm.png")
pag.moveTo(confir)
pag.click()


sleep(1)
dated = pag.locateCenterOnScreen("shift.png")
pag.moveTo(dated)
pag.moveTo(dated.x + 190 , dated.y )
pag.click()

dated = pag.locateCenterOnScreen("shift.png")
pag.moveTo(dated)
pag.moveTo(dated.x + 190 , dated.y + 50 )
pag.click()

dated = pag.locateCenterOnScreen("retrive.png")
pag.moveTo(dated)
pag.click()

# # ....................shift1.1
sleep(1)
dated = pag.locateCenterOnScreen("orgcd.png")
pag.moveTo(dated)
pag.moveTo(dated.x , dated.y + 40 )
pag.click()

dated = pag.locateCenterOnScreen("print.png")
pag.moveTo(dated)
pag.click()

sleep(2)
confir = pag.locateCenterOnScreen("cel.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("ok.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("a1.png")
pag.moveTo(confir)
pag.click()

# ......................shift1.2
sleep(1)
dated = pag.locateCenterOnScreen("orgcd.png")
pag.moveTo(dated)
pag.moveTo(dated.x , dated.y + 70 )
pag.click()

dated = pag.locateCenterOnScreen("print.png")
pag.moveTo(dated)
pag.click()

sleep(2)
confir = pag.locateCenterOnScreen("cel.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("ok.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("a1.png")
pag.moveTo(confir)
pag.click()

# ......................shift1.3
sleep(1)
dated = pag.locateCenterOnScreen("orgcd.png")
pag.moveTo(dated)
pag.moveTo(dated.x , dated.y + 100 )
pag.click()

dated = pag.locateCenterOnScreen("print.png")
pag.moveTo(dated)
pag.click()

sleep(2)
confir = pag.locateCenterOnScreen("cel.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("ok.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("a1.png")
pag.moveTo(confir)
pag.click()

# ......................shift1.4
sleep(1)
dated = pag.locateCenterOnScreen("orgcd.png")
pag.moveTo(dated)
pag.moveTo(dated.x , dated.y + 130 )
pag.click()

dated = pag.locateCenterOnScreen("print.png")
pag.moveTo(dated)
pag.click()

sleep(2)
confir = pag.locateCenterOnScreen("cel.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("ok.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("a1.png")
pag.moveTo(confir)
pag.click()

# ......................shift1.5
sleep(1)
dated = pag.locateCenterOnScreen("orgcd.png")
pag.moveTo(dated)
pag.moveTo(dated.x , dated.y + 160 )
pag.click()

dated = pag.locateCenterOnScreen("print.png")
pag.moveTo(dated)
pag.click()

sleep(2)
confir = pag.locateCenterOnScreen("cel.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("ok.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("a1.png")
pag.moveTo(confir)
pag.click()

# .......................clear
sleep(1)
dated = pag.locateCenterOnScreen("shift.png")
pag.moveTo(dated)
pag.moveTo(dated.x + 190 , dated.y )
pag.click()

dated = pag.locateCenterOnScreen("shift.png")
pag.moveTo(dated)
pag.moveTo(dated.x + 190 , dated.y + 80 )
pag.click()

dated = pag.locateCenterOnScreen("retrive.png")
pag.moveTo(dated)
pag.click()

# ....................shift2.1
sleep(1)
dated = pag.locateCenterOnScreen("orgcd.png")
pag.moveTo(dated)
pag.moveTo(dated.x , dated.y + 40 )
pag.click()

dated = pag.locateCenterOnScreen("print.png")
pag.moveTo(dated)
pag.click()

sleep(2)
confir = pag.locateCenterOnScreen("cel.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("ok.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("a1.png")
pag.moveTo(confir)
pag.click()

# ......................shift2.2
sleep(1)
dated = pag.locateCenterOnScreen("orgcd.png")
pag.moveTo(dated)
pag.moveTo(dated.x , dated.y + 70 )
pag.click()

dated = pag.locateCenterOnScreen("print.png")
pag.moveTo(dated)
pag.click()

sleep(2)
confir = pag.locateCenterOnScreen("cel.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("ok.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("a1.png")
pag.moveTo(confir)
pag.click()

# ......................shift2.3
sleep(1)
dated = pag.locateCenterOnScreen("orgcd.png")
pag.moveTo(dated)
pag.moveTo(dated.x , dated.y + 100 )
pag.click()

dated = pag.locateCenterOnScreen("print.png")
pag.moveTo(dated)
pag.click()

sleep(2)
confir = pag.locateCenterOnScreen("cel.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("ok.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("a1.png")
pag.moveTo(confir)
pag.click()

# ......................shift2.4
sleep(1)
dated = pag.locateCenterOnScreen("orgcd.png")
pag.moveTo(dated)
pag.moveTo(dated.x , dated.y + 130 )
pag.click()

dated = pag.locateCenterOnScreen("print.png")
pag.moveTo(dated)
pag.click()

sleep(2)
confir = pag.locateCenterOnScreen("cel.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("ok.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("a1.png")
pag.moveTo(confir)
pag.click()

sleep(1)
confir = pag.locateCenterOnScreen("exit.png")
pag.moveTo(confir)
pag.click()