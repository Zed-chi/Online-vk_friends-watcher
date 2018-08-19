import vk_api
import getpass


def get_user_login():
    return input("Login: ")


def get_user_password():
    return getpass.getpass(prompt="Password: ")


def auth_handler():
    key = input("Enter authentication code:")
    remember_device = True
    return key, remember_device


def get_api(login, password):
    session = vk_api.VkApi(
        login,
        password,
        auth_handler=auth_handler
    )
    try:
        session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
    else:
        return session.get_api()


def get_friends_online(api):
    online_ids = api.friends.getOnline()
    online_usernames = api.users.get(
            user_ids=format(online_ids),
            fields="first_name,last_name",
            )
    return online_usernames


def print_online_friends(online_usernames):
    print("\n=== Online friends: {} ===".format(len(online_usernames)))
    for i in online_usernames:
        name = i['first_name']+" "+i['last_name']
        print("=>", name)


def main():
    login = get_user_login()
    password = get_user_password()
    vk_api = get_api(login, password)
    friends_online = get_friends_online(vk_api)
    print_online_friends(friends_online)


if __name__ == '__main__':
    main()
