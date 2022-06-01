from tkinter import *  #tkinter để thao tác với GUI, giúp tạo ra một window khi chạy Python
from datetime import datetime  #tính thời khắc hiện tại

import time  #thay đổi thời gian sau mỗi 0.1s
import math   # vẽ đường tròn làm mặt đồng hồ

WINwidth = 300  #độ lớn của đồng hồ
WINcolor = 'green'  #Màu sắc của đồng hồ

WINheight = WINwidth  #Chiều rộng của Window
S_length = WINwidth / 2 * 0.75  #Chiều dài kim giây
M_length = S_length * 0.95  #Chiều dài kim phút
H_length = S_length * 0.8  #Chiều dài kim giờ
H_LINEwidth = 8  #Độ phì của kim giờ
M_LINEwidth = H_LINEwidth / 2  #Độ phì của kim phút 
S_LINEwidth = 1  #Đồ phì của kim giây

#Tạo Window
Clock = Tk()
Clock.title("Quang's clock")

w = Canvas(Clock, width = WINwidth, height = WINheight, background = WINcolor)
w.pack()

w.create_oval(WINwidth / 2 - 5, WINheight / 2 - 5, WINwidth / 2 + 5, WINheight / 2 + 5, fill="black") 
w.create_oval(5, 5, WINwidth-5, WINheight-5, width = 2)  #Tạo vòng tròn bên ngoài đồng hồ

FontSize = int(WINwidth / 14)  #Size của chữ 
Fx = 0  #Sửa vị trí của chữ hiển thị giờ
Fy = FontSize / 10
R = S_length + FontSize * 0.9  #Bán kính của chữ hiển thị giờ
A = 0  #Độ lớn của góc tạo với chữ hiển thị giờ
for i in range(1,13):  #Hiển thị chữ
    A = A + 30
    Tx = R * math.cos(A / 180 * math.pi)  #Tọa độ của chữ hiển thị giờ
    Ty = R * math.sin(A / 180 * math.pi)
    w.create_text(WINwidth / 2 + Ty - Fx, WINheight / 2 - Tx + Fy, text = i, font = ("", FontSize))

try:
    while True:
        #Bắt đầu vòng lặp tính giờ
        now = datetime.now()  #lấy thời gian hiện tại
        if now.hour > 12:  #Biểu thị thời gian dưới dạng 12h
            nowhour = now.hour - 12
        else:
            nowhour = now.hour
        #Nếu kim giây chạy thì kim phút cũng chạy theo
        nowhour = nowhour + now.minute / 60 + now.second / 3600  #Thay đổi định dạng thời gian
        nowminute = now.minute + now.second / 60  #Thay đổi định dạng phút

        H_A = nowhour / 12 * 360 * math.pi /180  #Độ lớn của góc tạo với kim
        M_A = nowminute / 60 * 360 * math.pi / 180
        S_A = now.second / 60 * 360 * math.pi / 180

        H_x = math.cos(H_A) * H_length  #tính toán độ dài của kim so với trung tâm đồng hồ
        H_y = math.sin(H_A) * H_length
        M_x = math.cos(M_A) * M_length
        M_y = math.sin(M_A) * M_length
        S_x = math.cos(S_A) * S_length
        S_y = math.sin(S_A) * S_length

        w.create_text(WINwidth / 2 , WINheight / 2 + WINwidth / 8, text = datetime.now().strftime('%d/%m/%Y.  %H:%M:%S'), font = ("", int(FontSize / 1.5)), tag="Y")  #Hiển thị Năm tháng ngày giờ phút giây

        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + H_y, WINheight / 2 - H_x, width = H_LINEwidth, tag="H") #Kim giờ
        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + M_y, WINheight / 2 - M_x, width = M_LINEwidth, tag="M") #Kim phút
        w.create_line(WINwidth / 2, WINheight / 2, WINwidth / 2 + S_y, WINheight / 2 - S_x, width = S_LINEwidth, tag="S") #Kim giây

        w.update()  #Update thời gian mới

        w.delete("H")  #Xóa thời gian cũ
        w.delete("M")
        w.delete("S")
        w.delete("Y")

        time.sleep(0.1)  #update đồng hồ sau mỗi 0.1s
except:
    pass
