
import datetime
import json
import configparser

conf_file = configparser.RawConfigParser()

def main():
    ip = ""
    port = ""
    conf_file.read('test2.txt')
    sections = conf_file.sections()
    print(conf_file.sections()[0])
    #for section in sections:
    #    print(section)
    #    for value in conf_file[section]:
    #        print(value)
    ip = conf_file[conf_file.sections()[0]]["ip"]
    port = conf_file[conf_file.sections()[0]]["port"]
    print(ip + " " + port)
    return ip, port

if __name__ == '__main__':
    main()
