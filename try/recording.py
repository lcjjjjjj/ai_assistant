import pyaudio
import wave
import threading


import os
# # 尝试更改当前工作目录到脚本所在的目录
# script_directory = "C:\\Users\\86185\\Desktop\\jing"  # 使用双反斜杠或原始字符串
# os.chdir(script_directory)
# # 现在再次获取当前工作目录
# # print(os.getcwd())

# 录音参数
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# 初始化PyAudio
p = pyaudio.PyAudio()

# 用于控制录音的布尔标志
recording_active = True

def record_to_file(filename):
    global recording_active
    try:
        # 打开文件准备写入
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            stream = p.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            frames_per_buffer=CHUNK)
            stream.start_stream()
            
            print("录音开始到文件，输入 'stop' 结束录音。")

            while recording_active:
                data = stream.read(CHUNK)
                if not data:
                    break
                wf.writeframes(data)  # 写入数据到文件

    except KeyboardInterrupt:
        print("用户中断录音。")
    finally:
        recording_active = False
        if stream.is_active():
            stream.stop_stream()
        stream.close()
        p.terminate()
        print("录音结束，文件已保存。")

# 录音文件名
filename = "recording.wav"

# 创建并启动录音线程
record_thread = threading.Thread(target=record_to_file, args=(filename,))
record_thread.start()

# 监听用户输入以结束录音
try:
    while recording_active:
        user_input = input("请输入命令：")
        if user_input.lower() == 'stop':
            print("接收到停止命令，正在结束录音...")
            recording_active = False
except KeyboardInterrupt:
    print("程序被用户中断。")

record_thread.join()  # 等待录音线程结束