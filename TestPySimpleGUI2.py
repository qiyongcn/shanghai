import PySimpleGUI as sg 
from random import randint
import operator

sg.theme('Light Grey 3')
sg.popup_quick_message('上海大学，文物材料分析工具', auto_close=True, non_blocking=True)
MAX_ROWS, MAX_COLS, COL_HEADINGS = 15, 6, ('A', 'B', 'C', 'D', 'E', '平均值',)


tab1_layout = [[sg.Text('样本均值', background_color='#eeeeee', text_color='black',font='宋体 18')]] + \
              [[sg.Text(' ' * 10)] + [sg.Text(s, key=s, enable_events=True, font='宋体 18', size=(7, 1)) for i, s in enumerate(COL_HEADINGS)]] + \
              [[sg.T(r, size=(4, 1))] + [sg.Input(randint(0, 100), justification='r', key=(r, c)) for c in range(MAX_COLS)] for r in range(MAX_ROWS)] + \
              [[sg.Button('Show Table As Lists'), sg.Button('Exit')]] + \
              [[sg.Input(key='-in1-')]]

tab2_layout = [[sg.Text('方差计算', background_color='#eeeeee',font='宋体 18')],
               [sg.Input(key='-in2-')]]

tab3_layout = [[sg.Text('线性回归')],
               [sg.Input(key='-in3-')]]

tab4_layout = [[sg.Text('非线性回归')],
               [sg.Input(key='-in4-')]]

tab5_layout = [[sg.Text('聚类分析')],
               [sg.Input(key='-in5-')]]

tab6_layout = [[sg.Text('最小支撑树分析')],
               [sg.Input(key='-in6-')]]

tab7_layout = [[sg.Text('对应分析')],
               [sg.Input(key='-in7-')]]

tab8_layout = [[sg.Text('判别分析')],
               [sg.Input(key='-in8-')]]

tab9_layout = [[sg.Text('时序分析')],
               [sg.Input(key='-in9-')]]

layout = [  [sg.TabGroup([[sg.Tab('均值', tab1_layout, background_color='#eeeeee', key='-mykey-'),
                         sg.Tab('方差', tab2_layout, background_color='#eeeeee'),
                         sg.Tab('线性回归', tab3_layout),
                         sg.Tab('非线性回归', tab4_layout),
                         sg.Tab('聚类分析', tab5_layout),
                         sg.Tab('最小支撑树分析', tab6_layout),
                         sg.Tab('对应分析', tab7_layout),
                         sg.Tab('判别分析', tab8_layout),
                         sg.Tab('时序分析', tab9_layout)]],
                       key='-group2-', title_color='black',
                       selected_title_color='red', tab_location='topleft')],
            [sg.Text('Enter something:'), sg.Input(key='-IN-')],
            [sg.Text('Our output will go here', size=(10,1), key='-OUT-')],
            [sg.Button('OK'),sg.Button('Exit')]]
         

window = sg.Window('文物数据分析工具',font='宋体 12', icon='image/logo.ico',finalize=True, keep_on_top=True, default_element_size=(12, 1), element_padding=(1, 1), return_keyboard_events=True).Layout(layout)



while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    # window.Normal()

    window['-OUT-'].update(values['-IN-'])

window.close()