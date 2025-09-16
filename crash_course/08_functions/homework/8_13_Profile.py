# Homework from file tasks/8_13_Profile.md
## Task ## : 8.13
# 8_13_Profile
from typing import Dict, Any

def build_profile(user_name: str, last_name: str, **user_info: Any) -> Dict[str,Any]:
    """
    Profile with user and all info about him!
    - Can be extend with **userinfo -> double params in Dict
    """
    user_info['user_name'] = user_name.title()
    user_info['last_name'] = last_name.title()
    return user_info

get_profile = build_profile('serhii',
                            'andriievskyi',
                            age = 37,
                            salary = 1200,
                            languange = 'python')

print(get_profile)
