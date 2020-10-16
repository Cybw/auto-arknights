import tkinter as tk  # 使用Tkinter前需要先导入
import json
import random
import datetime

log = []
try:
    with open("D:\\arknights_leidian_json_config.txt",mode='r',encoding='utf-8') as ff:
        for i in ff.readlines():
            if i != None:
                log.append(i.strip("\n"))
except FileNotFoundError:
    with open("D:\\arknights_leidian_json_config.txt", mode='w', encoding='utf-8') as ff:
        print("Config file created as: D:\\arknights_leidian_json_config.txt")


# 第1步，实例化object，建立窗口window
window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
window.title('ArknightsLeidianJsonmaker')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x200')  # 这里的乘是小x


txt0 = tk.StringVar()

txt1 = tk.StringVar()
txt2 = tk.StringVar()
txt3 = tk.StringVar()

txt4 = tk.StringVar()
txt5 = tk.StringVar()
txt6 = tk.StringVar()

txt7 = tk.StringVar()
txt8 = tk.StringVar()
txt9 = tk.StringVar()


if(log == None or len(log) == 0 ):
    txt0.set('C:\\ChangZhi\\dnplayer2\\vms\\operationRecords')

    txt1.set('short')
    txt2.set('90')
    txt3.set('20')

    txt4.set('medium')
    txt5.set('140')
    txt6.set('10')

    txt7.set('long')
    txt8.set('190')
    txt9.set('10')

else:
    txt0.set(log[0])

    txt1.set(log[1])
    txt2.set(log[2])
    txt3.set(log[3])

    txt4.set(log[4])
    txt5.set(log[5])
    txt6.set(log[6])

    txt7.set(log[7])
    txt8.set(log[8])
    txt9.set(log[9])


fileroute = tk.Entry(window,textvariable = txt0, show = None, width = 40)
#模拟器脚本文件地址
fileroute.pack()


filename1 = tk.Entry(window,textvariable=txt1, show = None)#时间较短适合1-7
filename1.place(x=25, y=25)
roundtime1 = tk.Entry(window,textvariable=txt2, show = None)
roundtime1.place(x=25, y=45)
roundtimes1 = tk.Entry(window,textvariable=txt3, show = None)
roundtimes1.place(x=25, y=65)
filename2 = tk.Entry(window,textvariable=txt4, show = None)#时间中等适合狗粮龙门币
filename2.place(x=175, y=25)
roundtime2 = tk.Entry(window,textvariable=txt5, show = None)
roundtime2.place(x=175, y=45)
roundtimes2 = tk.Entry(window,textvariable=txt6, show = None)
roundtimes2.place(x=175, y=65)
filename3 = tk.Entry(window,textvariable=txt7, show = None)#时间较长适合6-16
filename3.place(x=325, y=25)
roundtime3 = tk.Entry(window,textvariable=txt8, show = None)
roundtime3.place(x=325, y=45)
roundtimes3 = tk.Entry(window,textvariable=txt9, show = None)
roundtimes3.place(x=325, y=65)



def click(x,y,clicktime):
    rx = x + random.randint(-100,100)
    ry = y + random.randint(-50,50)
    fclickt = [0,0,0,0]
    fclickt[0] = int(clicktime) + random.randint(-5,5)
    fclickt[1] = int(fclickt[0] + random.randint(1,5))
    fclickt[2] = int(fclickt[1] + random.randint(200,300))
    fclickt[3] = int(fclickt[2] + random.randint(1,5))
    click0 = {
        "timing": fclickt[0],
        "operationId": "PutMultiTouch",
        "points": [
            {
                "id": 1,
                "x": rx,
                "y": ry,
                "state": 1
            }
        ]
    }
    click1 = {
        "timing": fclickt[1],
        "operationId": "PutMultiTouch",
        "points": []
    }
    click2 = {
        "timing": fclickt[2],
        "operationId": "PutMultiTouch",
        "points": [
            {
                "id": 1,
                "x": rx,
                "y": ry,
                "state": 0
            }
        ]
    }
    click3 = {
        "timing": fclickt[3],
        "operationId": "PutMultiTouch",
        "points": []
    }
    oneclick = [click0,click1,click2,click3]
    return oneclick

def clicks(fclick_tablet,ax,ay,bx,by,cx,cy,rounds):
    fclick = []
    for i in range(0,rounds): 
        fclick0 = click(ax,ay,fclick_tablet[i*4])
        fclick1 = click(bx,by,fclick_tablet[i*4+1])
        fclick2 = click(cx,cy,fclick_tablet[i*4+2])
        fclick3 = click(cx,cy,fclick_tablet[i*4+3])
        fclick = fclick + fclick0 + fclick1 + fclick2 + fclick3
    return fclick

def jsonmaker(route,name,oneroundtime,times):
    #这个脚本的文件名
    recordname = name
    #每一局的时间
    time = int(oneroundtime) * 1000
    #循环次数
    rounds = int(times)
    #这个是采样率，哪个分辨率都一样
    resolution = [1920,1080]
    #开始1
    ax = round(resolution[0] * 10 * 0.898682)
    ay = round(resolution[1] * 10 * 0.909909)
    atime = 3000
    #开始2
    bx = round(resolution[0] * 10 * 0.861195)
    by = round(resolution[1] * 10 * 0.699099)
    btime = 2000
    #跳过
    cx = round(resolution[0] * 10 * 0.870314)
    cy = round(resolution[1] * 10 * 0.322522)

    click_tablet = [0] * (rounds*4)
    click_tablet[0] = atime
    click_tablet[1] = btime + atime
    click_tablet[2] = time + btime + atime
    click_tablet[3] = time + btime + atime + 3000
    for i in range(1,rounds):
        click_tablet[i*4] = click_tablet[0] + click_tablet[i*4-1]
        click_tablet[i*4+1] = click_tablet[1] + click_tablet[i*4-1]
        click_tablet[i*4+2] = click_tablet[2] + click_tablet[i*4-1]
        click_tablet[i*4+3] = click_tablet[3] + click_tablet[i*4-1]

    localtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    recordinfo = {
            "loopType": 0,
            "loopTimes": 1,
            "circleDuration": int(click_tablet[-1] + 2000),
            "loopInterval": 0,
            "loopDuration": 0,
            "accelerateTimes": 1,
            "recordName": "",
            "createTime": localtime,
            "playOnBoot": False,
            "rebootTiming": 0
    }
    operation = clicks(click_tablet,ax,ay,bx,by,cx,cy,rounds)
    record = {"operations": operation,
             "recordInfo": recordinfo}
    with open(route + "\\" + recordname + "_" + oneroundtime + "_" + times + ".record",'w',encoding='utf-8') as json_file:
        json.dump(record,json_file,ensure_ascii=False,indent=4,separators=(',', ':'))
        var = 'Saved as: ' + route + "\\" + recordname + "_" + oneroundtime + "_" + times + ".record" + "\n"
        t.insert('end', var)
def generate():
    
    jsonmaker(fileroute.get(),filename1.get(),roundtime1.get(),roundtimes1.get())
    jsonmaker(fileroute.get(),filename2.get(),roundtime2.get(),roundtimes2.get())
    jsonmaker(fileroute.get(),filename3.get(),roundtime3.get(),roundtimes3.get())
    log = [txt0.get() , txt1.get() , txt2.get() , txt3.get() , txt4.get() , txt5.get() , txt6.get() , txt7.get() , txt8.get(), txt9.get()]
    f=open('D:\\arknights_leidian_json_config.txt', "r+")
    f.truncate()
    f=open("D:\\arknights_leidian_json_config.txt","w")
    for line in log:
        f.write(line+'\n')
    f.close()
    t.insert('end', "Config saved as: D:\\arknights_leidian_json_config.txt\n")
    
def reset():
    
    txt1.set('short')
    txt2.set('90')
    txt3.set('20')

    txt4.set('medium')
    txt5.set('140')
    txt6.set('10')

    txt7.set('long')
    txt8.set('190')
    txt9.set('10')    
    
    
b1 = tk.Button(window, text='make', width=10,
               height=2, command=generate)
b1.place(x=200, y=90)

b2 = tk.Button(window, text='reset', width=5,
               height=1, command=reset)
b2.place(x=450, y=105)


t = tk.Text(window, height=4)
t.place(x=0, y=140)
 
window.mainloop()
