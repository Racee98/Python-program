#get user email
email=input("what is your email?.").strip()
#slice out user name
user=email[:email.index('@')]
#slice out domain
domain= email[email.index('@')+1:]
#format message
output="your username is {} and your domain name is {}".format(user,domain)
#display output message 
print(output)
