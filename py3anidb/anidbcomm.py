'''
Created on Jul 14, 2015

@author: brad
'''

import threading
import socket
import random
import string
import time
 
class AnidbComm(threading.Thread):
    '''
    classdocs
    '''
    _tag_list = {}
 
 
    def __init__(self, config):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self._hostname = config.get('anidb', 'anidbhost')
        self._port = int(config.get('anidb', 'anidbport'))
        self._localport = int(config.get('anidb', 'anidblocalport'))
        self._timeout = int(config.get('anidb', 'anidbtimeout'))
        self._delay = int(config.get('anidb', 'anidbdelay'))
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', self._localport))
        self.sock.settimeout(self._timeout)
        self._is_active = True
        self._last_message_time = time.perf_counter()
        print(self._last_message_time)
        self.start()
    
    def get_tag(self):
        return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(8))

    def send_request(self, request, callback):
        if self._last_message_time + self._delay < time.perf_counter():
            time.sleep(self._delay)
        tag = self.get_tag()
        self._tag_list[tag] = callback
        if request.contains(' '):
            req_message = bytes(request + "&tag=%s" % tag, 'utf-8')
        else:
            req_message = bytes(request + " tag=%s" % tag, 'utf-8')
        print(req_message)
        self.sock.sendto(req_message, (self._hostname, self._port))
    
    def stop(self):
        self._is_active = False
        self.sock.close()
        
    def run(self):
        while self._is_active:
            try:
                data = self.sock.recv(8192)
            except socket.timeout:
                self._handle_timeout()
                continue
            print("Received: ", data)

    def _handle_timeout(self):
        print('Timed out')