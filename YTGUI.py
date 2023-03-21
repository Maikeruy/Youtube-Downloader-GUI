import PySimpleGUI as sg
import pytube as pt

layout = [  [sg.Text('Youtube link:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Youtube Downloader', layout)

while True:
    event, values = window.read()
    if event == 'Ok':
        try:
            yt = pt.YouTube(values[0])
            print("Title:", yt.title)
        except:
            print('Make sure that you insert a Youtube link')
            continue
        try:
            yt.streams.first().download()
            print('Video Downloaded', yt.title)
        except:
            print("You might not have the rights to download videos")
        
    elif event == "Cancel" or event == sg.WIN_CLOSED:
        window.close()
        break
