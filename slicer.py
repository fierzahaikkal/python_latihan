# ini adalah project latihan email slicer

email = input("Masukkan Email anda: ").strip()

username = email[:email.index("@")]
domain = email[email.index("@")+1:]

user_out = 'usernaem: {}'.format(username)
domain_out = 'domain: {}'.format(domain)

print(user_out)
print(domain_out)