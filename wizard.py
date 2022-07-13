import PySimpleGUI as sg
import tvmaze
import namer
import utils


def main():
    show_list = [['000', 'Null', 'Null']]
    episode_list = [['00', '000', 'Null', ]]
    sg.theme("PythonPlus")
    
    # Tab Layouts
    show_search_tab = [
        [sg.Text('Enter show name:'), sg.InputText(key='show_query'), sg.Button('Search')],
        [
            sg.Table(show_list,
                     headings=['ID', 'Name', 'Released'],
                     num_rows=15,
                     key='shows',
                     col_widths=[7, 50, 7],
                     auto_size_columns=False,
                     justification='left')
        ]
    ]
    show_details_tab = [
        [sg.Text('Enter show id: '), sg.InputText(key='show_id'), sg.Button('Lookup')],
        [
            sg.Table(episode_list,
                     headings=['Sea', 'Ep', 'Name'],
                     num_rows=31,
                     key='episodes',
                     col_widths=[5, 5, 50],
                     auto_size_columns=False,
                     justification='left')
        ]
    ]
    renamer_tab = [
        [sg.Text('Start season: '),
         sg.InputText(key='start_season', size=5),
         sg.Text('Episode: '),
         sg.InputText(key='start_episode', size=5),
         sg.Text('End season: '),
         sg.InputText(key='end_season', size=5),
         sg.Text('Episode: '),
         sg.InputText(key='end_episode', size=5),
         sg.Button('Trim')],
        [sg.Text('Folder: '),
         sg.InputText(key='folder'),
         sg.Text('Filetype: '),
         sg.InputText(key='type', size=5),
         sg.Button('Test'),
         sg.Button('Run')],
        [sg.Text('Values will go here', key='output')]
    ]

    tabs = [[sg.TabGroup([[
            sg.Tab('Shows', show_search_tab),
            sg.Tab('Episodes', show_details_tab),
            sg.Tab('Rename', renamer_tab)
            ]])]]

    window = sg.Window('Ep Get', tabs)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Search':
            show_list = tvmaze.search_for_show(values['show_query'], True)
            window['shows'].update(values=show_list)
        elif event == 'Lookup':
            episode_list = tvmaze.get_episode_list(values['show_id'])
            window['episodes'].update(values=tvmaze.process_episode_dict(episode_list, True))
        elif event == 'Trim':
            episode_list = tvmaze.trim_episode_list(episode_list,
                                                    start_season=int(values['start_season']),
                                                    start_episode=int(values['start_episode']),
                                                    end_season=int(values['end_season']),
                                                    end_episode=int(values['end_episode']))
            window['episodes'].update(values=tvmaze.process_episode_dict(episode_list, True))
        elif event == 'Test':
            output = namer.rename_files(values['folder'], tvmaze.process_episode_dict(episode_list), values['type'], False)
            output = utils.list_to_string(output)
            print(output)
            window['output'].update(output)
        elif event == 'Run':
            namer.rename_files(values['folder'], tvmaze.process_episode_dict(episode_list), values['type'], True)
            window['output'].update('Operation complete')

    window.close()


if __name__ == '__main__':
    main()
