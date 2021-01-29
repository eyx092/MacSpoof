import random, sys

if sys.platform == "win32":
    random_address = ("%02x%02x%02x%02x%02x%02x" % (random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255))).upper()

else:
    random_address = "%02x:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255),
                                       random.randint(0, 255))
print(random_address)
