def generate_passwords(platform, name, father_name, wife_name, gf_names, mobile, fav_thing, hobby, best_friend):
    inputs = [
        platform, name, father_name, wife_name,
        gf_names, mobile, fav_thing, hobby, best_friend
    ]

    passwords = set()
    for i in inputs:
        for j in inputs:
            if i and j and i != j:
                passwords.add(i + j)
                passwords.add(i + "@" + j)
                passwords.add(i + "123")
                passwords.add(j + "786")
                passwords.add(i[:2] + j[-2:] + "2025")

    return list(passwords)[:20]