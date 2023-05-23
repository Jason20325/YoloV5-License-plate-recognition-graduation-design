import base64
import PySimpleGUI as sg
from io import BytesIO
import os

win_size = (1250, 500)  # 窗口大小(宽，高)
button_size = (10, 4)  # 按键大小
image_button_size = (50, 20)  # 按键大小
image_size = (400, 400)  # 按键大小
text_font = ('微软雅黑', '12')
title_font = ('微软雅黑', '15', 'bold')

sg.theme('GreenTan')
sg.set_options(font=text_font)


# 若img.save()报错 cannot write mode RGBA as JPEG
# 则img = Image.open(image_path).convert('RGB')
def image_to_base64(img, fmt='png'):
    output_buffer = BytesIO()
    img.save(output_buffer, format=fmt)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data).decode('utf-8')
    # return f'data:image/{fmt};base64,' + base64_str
    return base64_str


path1 = r'./inference/images/'
path2 = r'./inference/output/'


def get_img_path(path):
    file_path = path
    for file in os.listdir(path):
        if file.endswith('jpg'):
            file_path = os.path.join(path, file)
    return file_path


file_lay = [

    [sg.Button('Select Image', key='load', auto_size_button=True, enable_events=True, size=button_size)],
    [sg.Button('Identify Plate', key='do', auto_size_button=True, enable_events=True, size=button_size)],
]

img1_lay = [
    [sg.Text('识别前图片')],
    [sg.Button(key='qian', size=image_button_size, button_color=("white", "white"), image_size=image_size)]
]
img2_lay = [
    [sg.Text('识别后图片')],
    [sg.Button(key='hou', size=image_button_size, button_color=("white", "white"), image_size=image_size)]
]

layout = [[sg.Column(file_lay),
           sg.VSeparator(),
           sg.Column(img1_lay),
           sg.VSeparator(),
           sg.Column(img2_lay),
           ]]

# # 创造窗口
# window = sg.Window('车牌识别界面', layout, size=win_size, resizable=True,
#                    auto_size_text=True,
#                    auto_size_buttons=True)
# while True:
#     event, values = window.read(timeout=500)  # 用于读取页面上的事件和输入的数据。
#     if event is None:  # 如果用户关闭窗口
#         break
#     if event == 'load':
#         file_path1 = get_img_path(path1)
#         img = Image.open(file_path1)
#         img = img.resize(image_size)
#         base = image_to_base64(img)
#         # window['qian'].update(image_filename=path, image_size=image_size)
#         window['qian'].update(image_data=base, image_size=image_size)
#     if event == 'do':
#
# window.close()
