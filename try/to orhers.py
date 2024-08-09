from pydub import AudioSegment
import os
# # 尝试更改当前工作目录到脚本所在的目录
# script_directory = "C:\\Users\\86185\\Desktop\\jing"  # 使用双反斜杠或原始字符串
# os.chdir(script_directory)
# # 现在再次获取当前工作目录
# # print(os.getcwd())

def convert_mp3_to_others(mp3_file_path, flac_file_path, ctype):
    try:
        # 使用 pydub 加载MP3文件
        audio = AudioSegment.from_file(mp3_file_path, format="mp3")
        
        # 导出为需要格式
        audio.export(flac_file_path, format=ctype)
        print(f"Converted {mp3_file_path} to {flac_file_path}")
    except Exception as e:
        # 打印出任何异常信息
        print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    # 用户输入音频文件路径
    file_path = input("Enter the full path to your audio file: ")
    ctype = input("Enter the type you want to convert to: ")
    # 检查文件是否存在
    if not os.path.isfile(file_path):
        print("The file does not exist. Please enter a valid file path.")
        exit(1)
    
    # 指定文件的路径
    mp3_file_path = file_path  
    # 指定输出 mp3 文件的路径
    w_file_path = 'output.'+ctype  # 输出文件名

    # 调用函数进行转换
    convert_mp3_to_others(mp3_file_path, w_file_path, ctype)