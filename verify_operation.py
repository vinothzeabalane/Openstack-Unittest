import unittest
import socket
import os
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TestVerifyOperation(unittest.TestCase):
    
    def setUp(self):
        try:
            with open('input.json') as data_file:    
                self.data = json.load(data_file)
                
            self.ip = socket.gethostbyname(socket.gethostname())
            if self.ip:
                self.data['newton_auth']['admin']['OS_AUTH_URL'] = 'http://%s:35357/v3' % self.ip
            
            for k,v in self.data['newton_auth']['admin'].items():
                os.environ[k] = v
        except Exception as e:
            print(e)
        
    def test_image_verify(self):
        logger.info('Start executing image verify operation')
        res= os.system("openstack image list | grep 'deactivated'")
        if res == 0:
            self.fail("Image verification failed")
        else:
            print os.system("openstack image list")
    
    def test_compute_verify(self):
        logger.info('Start executing compute verify operation')
        res= os.system("openstack compute service list | grep 'down'")
        if res == 0:
            self.fail("Compute verification failed")
        else:
            print os.system("openstack compute service list")
         
    def test_network_verify(self):
        logger.info('Start executing network verify operation')
        res= os.system("openstack network agent list | grep 'False'")
        if res == 0:
            self.fail("Network verification failed")
        else:
            print os.system("openstack network agent list")
         
    def test_storage_verify(self):
        logger.info('Start executing storage verify operation')
        res= os.system("openstack volume service list | grep 'down'")
        if res == 0:
            self.fail("Storage verification failed")
        else:
            print os.system("openstack volume service list")
            
    def test_heat_verify(self):
        logger.info('Start executing heat verify operation')
        res= os.system("openstack orchestration service list | grep 'down'")
        if res == 0:
            self.fail("Heat verification failed")
        else:
            print os.system("openstack orchestration service list")
        
        
if __name__ == '__main__':
    unittest.main()
    
    
