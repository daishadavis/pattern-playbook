from collections import defaultdict
# Given a list of emails, return the count of unique email addresses and the full list of unique email addresses.
# Example: ["andy@google.com", "andy+spam@google.com", "and.y@google.com", "andy1@google.com", "a.n.d.y+a.n.d.y@google.com, andy+1+hello@google.com", "and.y2@google.com"]

# Every valid email includes a local name and a domain name, separated by the @ sign.
# For example, in the email "divya@coderpad.com", "divya" is the local name and "coderpad.com" is the domain name.

# Besides lowercase letters, the local name in the email may contain one or more '.' or '+'. If there are "." characters in the local name, emails will be forwarded to the email without the "." characters. If there are "+" characters, everything after the first "+" will be ignored. 
# So, emails to "div.ya@coderpad.com" would be forwarded to "divya@coderpad.com".
# Also, emails to "divya+spam@coderpad.com" would be forwarded to "divya@coderpad.com".

# Cases
emails_1 = ["a@code.com", "b@code.com", "c@code.com", "a+test@code.com"] # 3
emails_2 = ["andy@google.com", "andy+spam@google.com", "and.y@google.com", "andy1@google.com", "a.n.d.y+a.n.d.y@google.com", "andy+says+hello@google.com", "and.y2@google.com"] # 3
emails_3 = ["a@google.com", "a@coderpad.com"] # 2

# ----- BEGIN CODING HERE -----

#duplicate email:
    # same address @google.com and same name
    # even if it has '.' and the characters are in the order 
    # anything after a '+' plus is ignored

# intialize counter
# results array []
# hashmap = {}

# for loop (emails):
    # name, address = email[i].split('@')
    # name = "divya+spam" address = "coderpad.com"
    # name.partition('+')
    # hashmap[address] = name

#for loop hashmap[address]:
    # 



def valid_emails(emails):
    counter = 0
    res = []
    hashmap = defaultdict(list)
    # emails_3 = ["a@google.com", "a@coderpad.com", "b@google.com", "a+spam@google.com"] # 3
    # { "google.com" -> ["a", "b"] }

    for i in range(len(emails)):
        name, address = emails[i].split('@')
        name = name.split('+')[0]
        name = name.strip('.')
        
        if name in hashmap[address]:
            continue
        else:
            hashmap[address].append(name)
            counter += 1
    
    for key,values in hashmap.items():
        for v in values:
            res.append(v + "@" + key)

    return counter, res

print(valid_emails(emails_2))