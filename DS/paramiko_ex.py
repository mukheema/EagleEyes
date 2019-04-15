#!/usr/bin/python

import paramiko
import datetime


class RemoteTalk(object):
    _BUFFER_SZ = 1024

    def __init__(self, addr=None, port=22, username=username, password=password):
        self._addr = addr
        self._port = port # if forward-port used let user pass it
        self._username = username
        self._password = password
        self._sshClient = None
        self._sshSession = None
        self._stdout  = []
        self._stderr = []

    def startSsh(self):
        if self._sshClient:
            print "Already ssh client / session exist"
            return
        self._sshClient = paramiko.Transport(self._addr, self._port)
        self._sshClient.connect(username=self._username, password=self._password)
        self._sshSession = self._sshClient.open_channel(kind='session')

    def endSsh(self):
        self._sshClient.close()
        self._sshSession.close()
        self._sshClient = None
        self._sshSession = None

    def RunCmdAsync(self, cmd=None, timeout=None):
        if not cmd:
           raise "Pass a valid cmd"
        self._sshSession.exec_command(cmd)
        startTime = datetime.datetime()
        while True:
            if self._sshSession.recv_ready():
                self._stdout.appned(self._sshSession.recv[cls._BUFFER_SZ])
            if self._sshSession.recv_stderr_ready():
                self._stderr.append(self._sshSession.recv_stderr[cls._BUFFER_SZ])
            if self._sshSession.exit_status_ready():
                break
            deltaTime = datetime.datetime()
            if not timeout and deltaTime - startTime > timeout:
                break
        print "exit status: " , self._sshSession.exit_status()
        print "".join(self._stdout)
        print "".join(self._stderr)



class RemoteComm(object):

    def __init__(self, host, port, username, password):
        self._host = host
        self._port = int(port)
        if self._port is None:
            self._port = 22
        self._username = username

if __name__ == '__main__':
    rt = RemoteTalk(addr='den00aci.us.oracle.com', username='nhudson', password='nimbula')
    rt.startSsh()
    rt.RunCmdAsync(cmd="hostname -i ; uptime")
