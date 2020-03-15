import json
import numpy as np
import random
import datetime

#这个脚本的文件名
recordname = '剿灭'
#每一局的时间
time = 900000
#循环次数
rounds = 2
#雷电模拟器脚本路径
route = "C:\\ChangZhi\\dnplayer2\\vms\\operationRecords"

def click(x,y,clicktime):
    rx = x + random.randint(-200,200)
    ry = y + random.randint(-100,100)
    #print(rx)
    #print(ry)
    fclickt = [0,0,0,0]
    fclickt[0] = int(clicktime) + random.randint(-5,5)
    fclickt[1] = int(fclickt[0] + random.randint(1,5))
    fclickt[2] = int(fclickt[1] + random.randint(200,300))
    fclickt[3] = int(fclickt[2] + random.randint(1,5))
    #print(fclickt)
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

def clicks(fclick_tablet):
    fclick = []
    for i in range(0,rounds): 
        fclick0 = click(ax,ay,fclick_tablet[i*4])
        fclick1 = click(bx,by,fclick_tablet[i*4+1])
        fclick2 = click(cx,cy,fclick_tablet[i*4+2])
        fclick3 = click(cx,cy,fclick_tablet[i*4+3])
        fclick = fclick + fclick0 + fclick1 + fclick2 + fclick3
    return fclick

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
ctime = time

click_tablet = np.zeros([rounds,4], dtype = float)
click_tablet[0][0] = atime
click_tablet[0][1] = btime + atime
click_tablet[0][2] = time + btime + atime
click_tablet[0][3] = time + btime + atime + 2000
for i in range(1,rounds):
        click_tablet[i] = click_tablet[0] + click_tablet[i-1][3]
click_tablet = click_tablet.ravel()

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
operation = clicks(click_tablet)
record = {"operations": operation,
         "recordInfo": recordinfo}
#srecord = str(record).replace("'", '"')
#srecord = srecord.replace("False", 'false')
#myscript = json.dumps(record, indent=4, separators=(',', ':'))
#print(myscript)
with open(route + "\\" + recordname + ".record",'w',encoding='utf-8') as json_file:
    json.dump(record,json_file,ensure_ascii=False,indent=4,separators=(',', ':'))
