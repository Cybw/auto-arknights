# auto-arknights

新增雷电模拟器内嵌录屏脚本的生成脚本的带图形界面的生成器  
https://github.com/Cybw/auto-arknights/blob/master/jsonmakerwithGUI.py  
  
如图所示，修改框体中的文件名、单次循环时间、循环次数，点击make即可生成到指定文件夹内。  
  
![image](https://github.com/Cybw/auto-arknights/blob/master/JsonMakerGUI.png)  
  
默认生成三个文件  
short适用于1-7  
medium适用于狗粮和龙门币  
long适用于6-16这种时间长的  
  
由于tkinter的限制，不从另外的文件中读取难以实现文件的保存，所以默认在D盘根目录下生成设置文件。如果与你常用的配置不匹配，可以自行修改脚本中的参数，然后用pyinstaller重新生成.exe文件。  


—————————————分割线————————————————  

新增雷电模拟器内嵌录屏脚本的生成脚本  
https://github.com/Cybw/auto-arknights/blob/master/leidianjson_arkningts.py  

1、雷电模拟器内置录屏功能，使用简便但是只能重复录制好的操作，这就导致了每次点击的坐标、按压时间、按压间隔都是固定的，这就有可能会被发现；   
  
2、打开后发现其实就是用json将每一个操作记录下来，所以就写了一个可以直接生成一套连续点击的json，保证每次点击都是随机的；  

3、用法：  
    复制python 脚本到本地，修改：  
    
    #这个脚本的文件名  
    recordname = '剿灭'  
    #每一局的时间  
    time = 900000  
    #循环次数  
    rounds = 2  
    #雷电模拟器脚本路径  
    route = "C:\\ChangZhi\\dnplayer2\\vms\\operationRecords"  

然后运行，就可以在模拟器的屏幕录制里面使用了。  
  
![image](https://github.com/Cybw/auto-arknights/blob/master/demo2.png)  

—————————————分割线————————————————  

明日方舟的按键精灵脚本 an ANJIANJINGLING scripts for arknights  
https://github.com/Cybw/auto-arknights/blob/master/anjianjingling%20arknights  
  
1、目前只支持雷电模拟器，优点在于模拟器可以任意比例缩放；  

2、只需打开到图中界面，勾选代理指挥，修改ftime 和 times 两个变量点调试、运行即可反复刷同一个图；  

3、可使用teamviewer实现远程挂机； 
  
4、记得要插着显示器，笔记本要打开盖子，不然模拟器无法初始化。  


![image](https://github.com/Cybw/auto-arknights/blob/master/demo.png)  
  
—————————————分割线————————————————  

使用须知：  

1、理论上模拟器环境中运行的app无法检测环境外运行的按键精灵，除非模拟器和游戏是一家的（比如MUMU和阴阳师）；  

2、所以为了您的账号安全，请不要使用鹰角或B站推荐的模拟器，以防他们有什么交♂易，如造成损失本人概不负责；  

3、请考虑每天4:00的例行下线和维护造成的下线，遇到这种情况就得重新登录；  

4、使用按键精灵脚本时游戏界面不应有任何阻挡，虽然脚本中设定了模拟器界面总在最前，但以免脚本按到其他地方去，可以配合火绒或者360的弹窗拦截功能；  

5、按键精灵脚本的优势在于门槛低，并且理论上最安全；  

6、雷电模拟器脚本优势在于可以在刷刷刷的时候干其他的事情；  

7、Have fun！  
