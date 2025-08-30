unconfirmed_users = ['alice', 'brian', 'candace'] confirmed_users = []
while unconfirmed_users: ❸
current_user = unconfirmed_users.pop()
print(f"Verifying user: {current_user.title()}")
confirmed_users.append(current_user)
