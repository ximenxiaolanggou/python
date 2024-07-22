'''
深圳市普中科技有限公司（PRECHIN 普中）
技术支持：www.prechin.net
PRECHIN
 普中

实验名称：WIFI实验-MQTT通信（订阅者）
接线说明：LED模块-->ESP32 IO
         (D1)-->(15)
         
实验现象：程序下载成功后，软件shell控制台输出当前IP、子网掩码、网关的地址信息，
         MQTT在线助手，输入网址：http://www.tongxinmao.com/txm/webmqtt.php#
         进入，按默认设置，选择连接，然后在Publish发布主题中选择程序中设置的Topic主题：
         /public/pz_esp32/1
         ，设置要发送的信息，点击发布，在Shell控制台即可输出主题和消息
         
注意事项：ESP32 WIFI作为客户端连接路由器热点，然后电脑也连接路由器，此时可连接成功输出信息

'''

#导入Pin模块
from machine import Pin
from machine import Timer
import time
import network
from simple import MQTTClient

#定义LED控制对象
led1=Pin(15,Pin.OUT)

#路由器WIFI账号和密码
ssid="prinfoESXi"
password="Prinfo123!"

#WIFI连接
def wifi_connect():
    wlan=network.WLAN(network.STA_IF)  #STA模式
    wlan.active(True)  #激活
    start_time=time.time()  #记录时间做超时判断
    
    if not wlan.isconnected():
        print("conneting to network...")
        wlan.connect(ssid,password)  #输入WIFI账号和密码
        
        while not wlan.isconnected():
            led1.value(1)
            time.sleep_ms(300)
            led1.value(0)
            time.sleep_ms(300)
            
            #超时判断,15 秒没连接成功判定为超时
            #if time.time()-start_time>150:
             #   print("WIFI Connect Timeout!")
              #  break
        #return False
        led1.value(0)
        print("network information:", wlan.ifconfig())          
        return True
    else:
        led1.value(0)
        print("network information:", wlan.ifconfig())
        return True
    

#设置 MQTT 回调函数,有信息时候执行
def mqtt_callback(topic,msg):
    print("topic: {}".format(topic.decode("UTF-8")))
    print("msg: {}".format(msg.decode("UTF-8")))
    
#接收数据任务
def mqtt_recv(tim):
    client.check_msg()
    

#程序入口
if __name__=="__main__":
    
    if wifi_connect():
        led1.value(0)
        SERVER="192.168.111.101"
        PORT=1883
        CLIENT_ID="PZ-ESP32"  #客户端ID
        TOPIC="/public/pz_esp32/1"  #TOPIC名称
        client = MQTTClient(CLIENT_ID, SERVER, PORT)  #建立客户端
        client.set_callback(mqtt_callback)  #配置回调函数
        client.connect()
        led1.value(1)
        client.subscribe(TOPIC)  #订阅主题
        
        #开启RTOS定时器,周期 300ms，执行MQTT通信接收任务
        tim = Timer(0)
        tim.init(period=300, mode=Timer.PERIODIC,callback=mqtt_recv)
        
