import requests


def search_for_show(query):
    res = requests.get('https://api.tvmaze.com/search/shows', params={'q': query})
    return res.json()


def get_episode_list(show_id):
    res = requests.get(f'https://api.tvmaze.com/shows/{show_id}/episodes')
    return res.json()


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


def episode_dict_to_list(episode_json):
    out = []
    for episode in episode_json:
        if episode["number"] > 9:
            out.append(f'{episode["season"]}{episode["number"]} {episode["name"]}')
        else:
            out.append(f'{episode["season"]}0{episode["number"]} {episode["name"]}')
    return out


if __name__ == '__main__':
    ep_list = get_episode_list('99')
    trimmed = trim_episode_list(ep_list, 2, 3, 2, 10)
    for ep in episode_dict_to_list(trimmed):
        print(ep)
