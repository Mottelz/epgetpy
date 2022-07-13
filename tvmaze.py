import requests


def search_for_show(query, return_as_lists=False):
    res = requests.get('https://api.tvmaze.com/search/shows', params={'q': query})
    return process_search_results(res.json(), return_as_lists)


def process_search_results(search_results, return_as_lists):
    out = []
    for search_result in search_results:
        sid = search_result['show']['id'] if search_result['show']['id'] else 'N/A'
        name = search_result['show']['name'] if search_result['show']['name'] else 'N/A'
        year = search_result['show']['premiered'][:4] if search_result['show']['premiered'] else 'N/A'
        if return_as_lists:
            out.append([sid, name, year])
        else:
            out.append(f"{sid} {name} ({year})")
    return out


def get_episode_list(show_id):
    res = requests.get(f'https://api.tvmaze.com/shows/{show_id}/episodes')
    return res.json()


def trim_to_season(full_list, season):
    out = []
    for episode in full_list:
        if str(episode['season']) == season:
            out.append(episode)
    return out


def trim_episode_list(full_list, start_season, start_episode, end_season, end_episode):
    out = []
    for episode in full_list:
        if start_season == end_season == episode['season']:
            if start_episode <= episode['number'] <= end_episode:
                out.append(episode)
        elif episode['season'] == start_season and episode['number'] >= start_episode:
            out.append(episode)
        elif episode['season'] == end_season and episode['number'] <= end_episode:
            out.append(episode)
        elif end_season > episode['season'] > start_season:
            out.append(episode)
    return out


def process_episode_dict(episode_json, return_as_lists=False):
    out = []
    if not return_as_lists:
        for episode in episode_json:
            if episode["number"] > 9:
                out.append(f'{episode["season"]}{episode["number"]} {episode["name"]}')
            else:
                out.append(f'{episode["season"]}0{episode["number"]} {episode["name"]}')
    else:
        for episode in episode_json:
            out.append([episode["season"], episode["number"], episode["name"]])
    return out


if __name__ == '__main__':
    print(search_for_show('doctor who', True))
