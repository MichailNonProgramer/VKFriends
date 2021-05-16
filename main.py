import vk_api

def get_user_friends(api_vk, user_id):
        friends = api_vk.friends.get(user_id=user_id, fields='nickname')
        friends_count = friends['count']
        print(f"Всего друзей {friends_count}")
        for friend in friends['items']:
            try:
                print(f"{friend['first_name']} {friend['last_name']}")
            except:
                print("Input incorrect token")

def start(token):
    target_id = int(input("Введите id пользователя: "))
    api_vk = vk_api.VkApi(token=token).get_api()
    get_user_friends(api_vk, target_id)

if __name__ == '__main__':
    token = input("Введите ваш токен VK: ")
    start(token)