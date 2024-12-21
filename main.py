import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme('Black')

archive_label = sg.Text('Select Archive')
archive_input = sg.Input(key='archive_input')
choose_archive_button = sg.FileBrowse('Choose', key='archive', target='archive_input',
                                      tooltip='Select an archive for extraction')

dest_label = sg.Text('Select Destination Directory')
dest_input = sg.Input(key='dest_input')
choose_dest_button = sg.FolderBrowse('Choose', key='dest', target='dest_input',
                                     tooltip='Select a directory to store extracted content')

left_col = sg.Column([[archive_label], [dest_label]])
mid_col = sg.Column([[archive_input], [dest_input]])
right_col = sg.Column([[choose_archive_button], [choose_dest_button]])

extract_button = sg.Button('Extract')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('Archive Extractor',
                   layout=[
                       [left_col, mid_col, right_col],
                       [extract_button, output_label]
                   ])

while True:
    event, values = window.read()
    print(event, values)
    archive, dest = values['archive'], values['dest']
    extract_archive(archive, dest)
    window['output'].update(value='Extraction successful!')
    match event:
        case sg.WINDOW_CLOSED:
            print('Thanks for choosing us, shutting down...')
            break

window.close()
