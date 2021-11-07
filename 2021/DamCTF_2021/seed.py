#!/usr/bin/env python3
import sys
import time
import random
import hashlib


def seed():
    return round(time.time())


def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()


def main():
    print(1636231462 - 1630231462)
    print(time.ctime(1630231462))
    # exit()
    for s in range(1630231462, 1636231462):
        random.seed(round(s), version=2)

        x = random.random()
        flag = hash(x)

        if 'b9ff3ebf' in flag:
            with open("./flag", "w") as f:
                f.write(f"dam{{{flag}}}")
            f.close()
            break

        print(f"Incorrect: {x}")
    print("Good job <3")


if __name__ == "__main__":
    sys.exit(main())
