from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
# print(config.get("url", "testurl"))
# print(config.get("waits", "explicit.wait"))

def readConfig(section,key):
    config = ConfigParser()
    config.read("config.ini")
    return config.get(section,key)

print(readConfig("url", "testurl"))
print(readConfig("waits", "explicit.wait"))
