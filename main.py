import tvmaze
import namer


def print_list(list_to_print):
    for item in list_to_print:
        print(item)


def main():
    while True:
        # Get episode list
        for result in tvmaze.search_for_show(input("Enter show name: ")):
            print(result)
        episode_list = tvmaze.get_episode_list(input("Enter show id: "))

        # Trim episodes
        if 'y' in input("Do you to trim the list? ").lower():
            if 'y' in input("Trim by season? ").lower():
                episode_list = tvmaze.trim_to_season(episode_list, input("Enter season number: "))
            else:
                episode_list = tvmaze.trim_episode_list(episode_list,
                                                        int(input("Start season: ")),
                                                        int(input("Start episode: ")),
                                                        int(input("End season: ")),
                                                        int(input("End episode: ")))

        # Print current list
        episode_list = tvmaze.episode_dict_to_list(episode_list)
        print_list(episode_list)

        # Rename?
        if 'y' in input("Do you want to rename files? ").lower():
            directory = input("Enter folder: ")
            ext = input("Enter extension: ")
            namer.rename_files(directory, episode_list, ext, False)
            if 'y' in input("Are you sure you want to do this? ").lower():
                namer.rename_files(directory, episode_list, ext)

        # offer an escape
        if 'y' in input("Do you want to quit? ").lower():
            exit()


if __name__ == '__main__':
    main()
