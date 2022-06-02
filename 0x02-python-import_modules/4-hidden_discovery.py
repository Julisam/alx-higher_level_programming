#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    # list_dir = dir(hidden_4)
    for var in dir(hidden_4):
        if(var[:2] != "__"):
            print('{}'.format(var))
