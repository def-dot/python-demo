import configparser


if __name__ == "__main__":
    conf = configparser.ConfigParser()
    conf.read("config.ini", encoding="utf-8")
    r = conf.items("apps_list")
    print(r)
