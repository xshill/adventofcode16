import hashlib

door_id = "wtnhxymk"

password = ["*"] * 8

i = 0
while "*" in password:
    if i % 500000 == 0:
        print("Index: " + str(i))

    curr_hash = hashlib.md5((door_id + str(i)).encode("utf-8")).hexdigest()
    if curr_hash[:5] == "00000" and curr_hash[5] in "01234567":
        index = int(curr_hash[5])

        if password[index] == "*":
            password[index] = curr_hash[6]
            print("Password: " + "".join(password))

    i += 1
