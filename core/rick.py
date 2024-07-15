import json
import requests
from os import system
system("clear")

# адамнын информациясын шыгару 
character_id = int(input("Enter character id: "))

if character_id > 826:
    print(f"Invalid character id: {character_id}")
    exit()

# location_id = int(input("Enter character id: "))

# if location_id > 826:
#     print(f"Invalid character id: {location_id}")
#     exit()

# url = "https://rickandmortyapi.com/api"
url = f"https://rickandmortyapi.com/api/character/{character_id}"
# url = f"https://rickandmortyapi.com/api/location/{location_id}"
# url = "https://rickandmortyapi.com/api/episode"


def get_data(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json() # > Dict
    
    return None # > None


data: dict | None = get_data(url)

with open('rick_and_morty.json', 'w') as file:
    # data это что мы записываем
    # file - это куда мы записываем
    # indent - размер пробелов в деление obj
    # ensure_ascii - Если True тогда файл понимает только English
    json.dump(data, file, indent=4, ensure_ascii=False)

    # open()                  # json
    # write() - записать      # dump() - записать
    # read() - прочитать      # load() - прочитать


# def get_location_informations(data: dict):
#     location_id = data['id']
#     location_name = data['name']
#     location_type = data['type']
#     location_dimension = data['dimension']
#     location_residents = data['residents']
#     residents = []

#     for resident in location_residents:
#         resident_id = resident.split('/')[-1]
#         residents.append(resident_id)

#     text = f"""
#     Идентификатор локации: {location_id}
#     Название: {location_name}
#     Тип: {location_type}
#     Размерность: {location_dimension}
#     Резиденты: {', '.join(residents)}
#     """

#     return text

# print(get_location_informations(data))


def get_character_informations(data: dict):
    character_id = data['id']
    character_name = data['name']
    character_status = data['status']
    character_species = data['species']
    character_type = data['type']
    character_gender = data['gender']
    character_origin = data['origin']['name']
    character_location = data['location']['name']
    
    character_episode = data['episode']
    if len(character_episode) > 1:
        episode_start = character_episode[0].split('/')[-1]
        episode_end = character_episode[-1].split('/')[-1]
        # "https://rickandmortyapi.com/api/episode/1"
        # ['https:', '', 'rickandmortyapi.com', 'api', 'episode', '1']
        # '1'
        character_episode = f"{episode_start}, {episode_end}"
    else:
        character_episode = character_episode[0].split('/')[-1]
        

    text = f"""
    Идентификатор персонажа: {character_id}
    Имя: {character_name}
    Статус: {character_status}
    Вид: {character_species}
    Тип: {character_type}
    Пол: {character_gender}
    Место проживания: {character_origin}
    Местоположение: {character_location}
    Был в серии: {character_episode}
    """
    return text
print(get_character_informations(data))
