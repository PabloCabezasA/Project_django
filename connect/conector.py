# -*- coding: utf-8 -*-

from suds.client import Client

def _connect_soap (self, cr, uid, ids):
    config_ids = self.pool.get("account.config.firma").search(cr,uid,[("id","!=","0")])
    config = self.pool.get("account.config.firma").read(cr, uid, config_ids,['connect'])[0]
    client = Client(config['connect'])
    client.set_options(location=config['connect'])
    return (client)

#web service CrSeed permite obtener semilla
def _connect_CrSeed (self):
#    url ="https://palena.sii.cl/DTEWS/CrSeed.jws?wsdl"
    url= "https://maullin.sii.cl/DTEWS/CrSeed.jws?WSDL"
    client = Client(url) 
    client.set_options(location=url)
    return (client)

#web service CrSeed permite obtener token
def _connect_GetTokenFromSeed ():
#    url ="https://palena.sii.cl/DTEWS/GetTokenFromSeed.jws?WSDL"
    url ="https://maullin.sii.cl/DTEWS/GetTokenFromSeed.jws?WSDL"
    client = Client(url) 
    client.set_options(location=url)
    return (client)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:#