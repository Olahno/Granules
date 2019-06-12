from datetime import datetime
import time
import socket


class Granule:
    def __init__(self):
        self.sensor = "sensor1"
        self.d = 255
        self.n = 32
        self.ObservationalError = 2
        self.data = 0


def getRange(xdata, xd):
    if xdata > xd:
        xj = round(float((xdata - xd) / xd), 1)
    else:
        xj = round(float((xd - xdata) / xd), 1) * -1

    if xj == -0.0:
        xj = 0.0
    return xj


x = Granule()

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


T = 1.0
temp = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
data = 0
conn, addr = s.accept()
print('Connected by', addr)
while True:
    while T > -1.0:
        data = conn.recv(1024)
        if int(data) > x.d or int(data) < 0:
            response = 'Value is out of bounds'
        else:
            x.data = int(data)
            xd = float(x.d / 2)
            xn = x.data / (x.d / x.n)
            xdr = x.data + x.ObservationalError
            xdl = x.data - x.ObservationalError
            xdr = getRange(xdr, xd)
            xdl = getRange(xdl, xd)

            if temp == xn:
                T = T - 0.1
            else:
                T = 1.0
            temp = xn

            if xdr == xdl:
                marg = str(xdl)
            else:
                marg = str(xdl) + '/' + str(xdr)

            currentTime = datetime.now().time()

            response = ('Sensor:' + str(x.sensor) + '\n' + 'Sensor value: ' +
                           str(x.data) + '\n' + 'Possible range: [0.' +
                           str(x.d) + ']' + '\n' + 'Intervals:' + str(x.n) + '\n' + 'Observational Error:' +
                           str(x.ObservationalError) + '\n' + 'Granule:' + str(xn) + '\n' +
                           'Range:' + marg + '\n' + 'T: ' + str(T) + '\n' + 'Timestamp:' + str(currentTime))
        conn.send(response)

    if not data:
        break
