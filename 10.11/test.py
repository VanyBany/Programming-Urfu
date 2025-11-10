import requests
import json

def send_request(url):
    response = requests.get('https://swapi.dev/api/people/')
    if response.status_code == 200:
        return response.json()
    return None

def save_data(data):
    print("Saving data")
    try:
        with open ("data.json", mode='w') as file:
            json.dump(data,file)
    except:
        print("Ошибка сохранения")

def parser():
    main_url = 'https://swapi.dev/api/people/'
    data_list = []
    for i in range(1,83):
        print(f'Parse people:{i}')
        data = send_request(main_url + '/' + str(i))
        if data:
            data_list.append(data)
    return data_list


# def main():
#     data = parser()
#     save_data(data)

# if __name__ == "__main__":
#     main()


with open ("data.json", mode='r') as file:
        data = json.load(file)


new_data = {}
for index, el in enumerate(data):
    new_data[index+1] = el

save_data(new_data)