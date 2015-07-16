'''
Created on Jul 14, 2015

@author: brad
'''
from py3anidb.entity.anime import Anime
from py3anidb.anidbcomm import AnidbComm
from py3anidb.utility.switch import switch
from py3anidb.utility.config import Config
import time
    
class AnidbAPI(object):
    
    _session_id = ""
 
    def __init__(self, configfilename = None):
        '''
        Constructor
        '''
        self.config = Config(configfilename)
        
        self.config.set_default('anidb', {
            'dbtype' : 'sqlite',
            'dbport' : '3306',
            'dbhostname' : 'localhost',
            'dbuser' : 'anidb',
            'dbpassword' : 'none',
            'dbname' : 'anidb',
            'anidbhost' : 'api.anidb.net',
            'anidbport' : '9000',
            'anidblocalport' : '9876',
            'anidbdelay' : '2',
            'anidbtimeout' : '20',
            'anidbuser' : '',
            'anidbpassword' : ''})
        
        self.anidbcomm = AnidbComm(self.config)
        print(self.config)

    def exit(self):
        self.anidbcomm.stop()

    def auth(self):
        self.anidbcomm.send_request("AUTH user=%s&pass=%s&protover=3&client=pythreeanidb&clientver=1" % \
                           (self.config.get('anidb', 'anidbuser'), self.config.get('anidb', 'anidbpassword')), self.process_result)
        
    def logout(self):
        self.anidbcomm.send_request("LOGOUT", self.process_result)
        
    def ping(self):
        self.anidbcomm.send_request('PING nat=1', self.process_result)
 
    def process_result(self, result):
        tag = result[:8]
        process_method = self._tag_list[tag]
        del self._tag_list[tag]
        values = result.split(' ')  
        status = int(values[1])
        for case in switch(status):
            if case(200):
                # All good
                _session_id = values[2]
                exec(process_method(True))
                break
            if case(201):
                _session_id = values[2]
                # log new version available
                break
            if case(500):
                #fail - bad login - try login again
                break
            if case(501):
                # Not logged in
                break
            if case(502):
                # access denied
                break
            if case(503):
                #fail - bad library version
                break  
            if case(504):
                #fail - banned
                break  
            if case(505):
                #fail - access denied
                break  
            if case(601):
                #fail - anidb down
                break
            if case():
                break
            
if __name__ == '__main__':
    anidbApi = AnidbAPI('py3anidb.ini')
    anidbApi.auth()
    anidbApi.logout()
    time.sleep(10)
    anidbApi.exit()