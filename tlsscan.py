import urllib.request as request 
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,time, timedelta
from pprint import pprint
import ssl 
import socket


context = request.ssl.create_default_context()
context.check_hostname = False

def get_certificate(url):
    #handle port
    port = 443
    if ":" in url:
        bits = url.split(':')
        url = bits[0]
        port = int(bits[1])
    try: 
        socket.setdefaulttimeout(3)
        with request.socket.create_connection((url, port)) as sock:
            
            with context.wrap_socket(sock, server_hostname=url, do_handshake_on_connect=True,  ) as wsock:
                cert = wsock.getpeercert()
                return url, cert
    except:
        return url, None

def validate_cert(domain, certificate, expiration_warning_days=14):
    message = []
    domain_match = False 
    if certificate is None:
        return False, ["UNABLE_TO_RETRIEVE_CERTIFICATE"]
    certificate_expired = datetime.now() < datetime.strptime(certificate['notAfter'], "%b %d %H:%M:%S %Y %Z")
    certificate_active =  datetime.now() >= datetime.strptime(certificate['notBefore'], "%b %d %H:%M:%S %Y %Z")
    if datetime.now() + timedelta(days=expiration_warning_days) \
        < datetime.strptime(certificate['notAfter'], "%b %d %H:%M:%S %Y %Z") \
        and not certificate_expired:
        message.append("EXPIRATION_NOTICE")

    for s in certificate['subject'][0] + certificate['subjectAltName']: #combine alts and primary
        key, value = s
        if "*" in value: #handle wildcards
            if value.replace('*.', '') in domain.lower():
                domain_match = True 
        if domain.lower() == value.lower():
            domain_match = True 
    
    if not domain_match:
        message.append("DOMAIN_NAME_INVALID")
    if not certificate_expired:
        message.append("CERTIFICATE_EXPIRED")
    if not certificate_active:
        message.append("CERTIFICATE_NOT_YET_ACTIVE")
    return  domain_match & certificate_expired & certificate_active, message

def load_domains(filename):
    domains = []
    with open(filename, 'r') as f:
        domains = f.read().splitlines()
    return domains

def retrieve_certs(domains):
    with ThreadPoolExecutor(max_workers=100) as pool:
        results = pool.map(get_certificate, domains)
    return results
        
def process_domains(domain_certs, expire_warning_days=14):
    results = {}
    for domain, cert in domain_certs:
        valid, messages = validate_cert(domain, cert, expiration_warning_days=expire_warning_days)

        results[domain]={
            'valid': valid,
            'messages': messages
        }
        if cert:
            results[domain]['expire'] = cert['notAfter']
        else:
            results[domain]['expire'] = 'MISSING'
    return results 










