users = {
    'aeinstein':{
        'first':'albert',
        'last':'aeinstein',
        'location':'princeton'
    },

    'mcurie':{
        'first': 'marie',
        'last':'curie',
        'location': 'paris'
    }
}

for username , user_info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
