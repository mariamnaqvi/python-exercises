# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and 
# Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

price_per_day = 3
little_mermaid_days = 1
brother_bear_days = 5
hercules_days = 1

total_number_of_days = little_mermaid_days + brother_bear_days + hercules_days

total_rental_cost = price_per_day * (total_number_of_days)

print (total_rental_cost)

# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

google_hourly_rate = 400
google_weekly_hours = 6
pay_for_google = google_hourly_rate * google_weekly_hours

amazon_hourly_rate = 380
amazon_weekly_hours = 4
pay_for_amazon = amazon_hourly_rate * amazon_weekly_hours

facebook_hourly_rate = 350
facebook_weekly_hours = 10
pay_for_facebook = facebook_hourly_rate * facebook_weekly_hours

weekly_payment = pay_for_google + pay_for_amazon + pay_for_facebook

print (weekly_payment)

# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her 
# current schedule.

class_full = False
schedule_doesnt_conflict = True
can_be_enrolled = not class_full and schedule_doesnt_conflict

print (can_be_enrolled)

# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired.
# Premium members do not need to buy a specific amount of products.

premium_member = True
items_purchased_morethan2 = True
offer_expired = False

offer_applied = premium_member or (items_purchased_morethan2 and not offer_expired)

print (offer_applied)

# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
password_atleast5 = len(password) >= 5

# the username must be no more than 20 characters
username_lessthan20 = len(username) <= 20

# the password must not be the same as the username
pass_username_notsame =  password != username

# bonus neither the username or password can start or end with whitespace
pass_nospace = password == password.strip()
username_nospace = username == username.strip()

strong_userpass = (password_atleast5
and username_lessthan20
and pass_username_notsame
and pass_nospace
and username_nospace)

print (strong_userpass)
