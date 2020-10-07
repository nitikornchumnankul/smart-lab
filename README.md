# smart-lab
## [ทำความเข้าใจเรื่อง การเปิด และ ปิด](https://github.com/nitikornchumnankul/smart-lab/blob/main/Face_DLIB/Face_DLIB.py)
### [1. เชื่อมต่อ Serial Port](https://www.raspberrypi.org/forums/viewtopic.php?t=64968) 
[("/dev/ttyUSB0", 9600) คืออะไร](https://www.youtube.com/watch?v=iyQgmmtIAXQ)

ttyUSB means "USB serial port adapter" and the "0" (or "1" or whatever) is the device number. ttyUSB0 is the first one found, ttyUSB1 is the second etc. (Note that if you have two similar devices, then the ports that they are plugged into may affected the order they are detected in, and so the names).

```
serialPort = serial.Serial("/dev/ttyUSB0", 9600) 
```
จะใช้ K3s ต่อกับ Serial port อย่างไร [Stack Overflow](https://stackoverflow.com/questions/57818941/kubernetes-pod-serial-communication-problem)

![k3s serial port](https://i.imgur.com/RHhlD4S.png)

```
containers:
  - name: acm
    securityContext:
      privileged: true
    volumeMounts:
    - mountPath: /dev/ttyACM0
      name: ttyacm
  volumes:
  - name: ttyacm
    hostPath:
      path: /dev/ttyACM0
```

### 2. Function สิ่งเปิด ปิด
```
def sw1Pressed():
    serialPort.write("SW1 Pressed".encode('utf-8'))
```

## วิธีการใช้ Git
### 1. ตั้งค่า username
```
git config --global user.name "username"
```
### 2. ตั้งค่า email
```
git config --global user.email "email@domain.com"
```
### 3. ดึงโค้ดลงมาบนเครื่อง local computer
```
git clone https://github.com/nitikornchumnankul/smart-lab.git
```
### 4. บันทึกสิ่งที่แก้ไข โค้ดทั้งหมด
```
git add .
```
### 5. เช็คว่าโค้ดได้ถูกบันทึก ทั้งหมดหรือยัง
```
git status
```
### 6. บันทึกโค้ดที่แก้ไข เพราะระบุข้อความ
```
git commit -m "ข้อความการแก้ไข"
```
### 7. นำโค้ดส่งไปยัง Github repository
```
git push
```
## Dependencies

### opencv-python 4.4.0.44 (import cv2)
```
pip install opencv-python
```
### numpy
```
pip install numpy
```
### dlib 19.21.0
```
pip install dlib
```

# References

### 1. วิธีตั้ง Putty บน Rasberry PI
 
[วิธีการตรวจสอบเครือข่ายของคุณโดยใช้ Raspberry PI](https://www.youtube.com/watch?v=zy9xis0IrpM)

[RASPBERRY PI - How to AutoConnect WIFI & view on Windows Laptop](https://www.youtube.com/watch?v=Z2Pjy7zpWZk)

### 2. Config Network กรณีใช้ Hotspot

[UPDATED | How to View Raspberry Pi 3 Desktop on Android Mobile Using Hotspot (Easiest Method)](https://www.youtube.com/watch?v=jHvJ-7lIyRSs)

### 3. Remote Desktop แสดงหน้า Desktop ของ Raspberry pi

[VNC (Virtual Network Computing)](https://www.raspberrypi.org/documentation/remote-access/vnc/)

### 4. ติดตั้ง Kubernetes บน Raspbery Pi

[Setup a Kubernetes 1.9.0 Raspberry Pi cluster on Raspbian using Kubeadm](https://kubecloud.io/setup-a-kubernetes-1-9-0-raspberry-pi-cluster-on-raspbian-using-kubeadm-f8b3b85bc2d1)
### 5. วิธีติดตั้ง Mysql Server on local computer
[How to install MySQL database server 8.0.19 on Windows 10](https://www.sqlshack.com/how-to-install-mysql-database-server-8-0-19-on-windows-10/)

### 6. เชื่อมต่อกับ Database
[Simple Face Recognizing System using python and openCV](https://dev.to/pranay749254/simple-face-recognizing-system-using-python-and-opencv)

### 7. เนื้อหา OpenCV-Face-Recognition
[Source Code ตัวอย่าง](https://github.com/Mjrovai/OpenCV-Face-Recognition)

![OpenCV-Face-Recognition](https://github.com/Mjrovai/OpenCV-Face-Recognition/raw/master/FaceRecogBlock.png?raw=true)

### 8. Python Face Recognition connected mysql database

[Source Code ตัวอย่าง](https://github.com/wilztan/PythonFaceRecognition)


