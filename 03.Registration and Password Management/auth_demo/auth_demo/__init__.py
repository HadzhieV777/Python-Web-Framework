"""
    FORGOTTEN PASSWORD

 1. Create new password for the account and send to email, phone...
   - Must be changed on first login with new password.

new_password = random_generate_password()
user = getUser(username)
user.set_password(new_password)
user.should_change_password = True
user.save()
send_mail(new_password)

 2. Send an email/phone with change password link.
   - On open, change password
"""
