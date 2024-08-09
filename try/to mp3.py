import os
# # 尝试更改当前工作目录到脚本所在的目录
# script_directory = "C:\\Users\\86185\\Desktop\\jing"  # 使用双反斜杠或原始字符串
# os.chdir(script_directory)
# # 现在再次获取当前工作目录
# # print(os.getcwd())
from pydub import AudioSegment
import filetype

def get_file_type(file_path):
    """使用 filetype 库来判断文件类型"""
    try:
        # 猜测文件类型
        kind = filetype.guess(file_path)
        if kind is not None:
            # 返回文件的 MIME 类型和文件扩展名
            return kind.mime, kind.extension
        else:
            return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
def convert_mp3_to_flac(mp3_file_path, flac_file_path, wtype):
    try:
        # 使用 pydub 加载文件
        audio = AudioSegment.from_file(mp3_file_path, format=wtype)
        
        # 导出为 mp3 格式
        audio.export(flac_file_path, format="mp3")
        print(f"Converted {mp3_file_path} to {flac_file_path}")
    except Exception as e:
        # 打印出任何异常信息
        print(f"An error occurred: {e}")
    
if __name__ == "__main__":
    # 用户输入音频文件路径
    file_path = input("Enter the full path to your audio file: ")

    # 检查文件是否存在
    if not os.path.isfile(file_path):
        print("The file does not exist. Please enter a valid file path.")
        exit(1)
    
    # 获取文件类型
    mime_type, file_extension = get_file_type(file_path)
    
    # if mime_type and file_extension:
    #     print(f"This audio file is of type: {mime_type} with extension {file_extension}")
    # else:
    #     print("Could not determine the file type.")
    wtype=file_extension
    # 指定文件的路径
    now_file_path = file_path  
    # 指定输出 mp3 文件的路径
    mp3_file_path = 'output.mp3'  # 输出文件名

    # 调用函数进行转换
    convert_mp3_to_flac(now_file_path, mp3_file_path, wtype)