import requests

def send_request(url:str = None) -> dict | bool:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False

def main():
    url = "https://swapi.dev/api/people/1"
    url_pilots = "https://swapi.dev/api/starships/?search=Millennium%20Falcon"
    response = send_request(url)
    pilots_response = send_request(url_pilots)

    if not pilots_response:
        print("Нет таких пилотов")
        return
    
    print('Пилоты Millennium Falcon')
    
    for pilot in pilots_response['results'][0]['pilots']:
        pilot = send_request(pilot)
        if pilot:
            name = pilot['name']
            print(f'- {name}')

        
    # if not response:
    #     print('Ничего не получилось :')
    #     return

    
    # name = response['name']
    # height = response['height']
    # mass = response['mass']
    # hair_color = response['hair_color']
    # homeworld_url = send_request(response['homeworld'])

    # print(f'Имя: {name}\nРост: {height}\nМасса: {mass}\nЦвет волос: {hair_color}')
    # if not homeworld_url:
    #     print("Планет нет")

    # else:
    #     planet_name = homeworld_url['name']
    #     print(f'Люк Скайуокер родился на планете {planet_name}')



    


if __name__ == "__main__":
    main()