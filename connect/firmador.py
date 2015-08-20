# -*- coding: utf-8 -*-

from OpenSSL import crypto
from OpenSSL.crypto import FILETYPE_PEM
from signxml import xmldsig
import signxml
#from  xml.etree import ElementTree 
from lxml import etree
import os
from connect.conector import _connect_GetTokenFromSeed


def _entregaFirma (xml_factura):
    path = os.getcwd() + '/Project_django/connect/firma/%s'
    p12 = path % 'cert_econube_2016.p12'
    p12 = crypto.load_pkcs12(file(p12, 'rb').read(), 'oleole09')
    certificate = p12.get_certificate()
    private_key = p12.get_privatekey()
    type_ = FILETYPE_PEM
    signature = certificate.get_signature_algorithm()
    type_pk = private_key.type()
    print signature
    print type_pk 
    str_private_key=crypto.dump_privatekey(type_, private_key)
    str_certificate_key=crypto.dump_certificate(type_, certificate)
    fields = certificate.get_subject().get_components()
    print(fields)
    root = etree.fromstring(xml_factura.strip())
#    root = etree.XML(xml_factura)
    xmldsig(root).sign(algorithm='rsa-sha1',key=str_private_key, cert=str_certificate_key,c14n_algorithm='REC-xml-c14n-20010315')
    xml_firmado =  etree.tostring(root,encoding="ISO-8859-1", method="xml")
    print xml_firmado
#    xml_firmado=xml_firmado.replace(':ds','')
#    xml_firmado=xml_firmado.replace('ds:','')
    verified_data = xmldsig(xml_firmado).verify(x509_cert=str_certificate_key)
    xml_verificado =  etree.tostring(verified_data,encoding="ISO-8859-1", method="xml")
    print xml_verificado
    client = _connect_GetTokenFromSeed()                 
    res = client.service.getToken(xml_verificado)
    xml_verificado =  etree.tostring(verified_data, pretty_print = True, method="xml")
#    res = etree.tostring(res, pretty_print = True, method="xml")
    return res,xml_verificado

def sign_file(tmpl_file, key_file):
        
    """sign *tmpl_file* with key in *key_file*.
    
     *tmpl_file* actually contains an XML document containing a signature
     template. It can be a file, a filename string or an HTTP/FTP url.
    
     *key_file* contains the PEM encoded private key. It must be a filename string.
     """
    from lxml.etree import parse, tostring
    doc = etree.parse(tmpl_file)
    # find signature node
    node = xmlsec.findNode(doc, xmlsec.dsig("Signature"))
    dsigCtx = xmlsec.DSigCtx()
    # Note: we do not provide read access to `dsigCtx.signKey`.
    #  Therefore, unlike the `xmlsec` example, we must set the key name
    #  before we assign it to `dsigCtx`
    signKey = xmlsec.Key.load(key_file, xmlsec.KeyDataFormatPem, None)
    signKey.name = basename(key_file)
    # Note: the assignment below effectively copies the key
    dsigCtx.signKey = signKey
    dsigCtx.sign(node)
    return etree.tostring(doc)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:#