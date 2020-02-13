#!/usr/bin/env python3

import gnupg

__VERSION__ = '1.0.0'
__encoding__ = 'utf-8'

def GPG(*args, **kwargs):
    gpg = gnupg.GPG(*args, **kwargs)
    gpg.encoding = __encoding__

    return(gpg)

def gen_key(gpg, name_email, name_real, passphrase,
            name_comment='', key_type='RSA', key_length=2048,
            subkey_type='DSA', subkey_length=1024, expire_date='365d'):

    input_data = gpg.gen_key_input(key_type=key_type,
                                   key_length=key_length,
                                   name_real=name_real,
                                   name_comment=name_comment,
                                   name_email=name_email,
                                   subkey_type=subkey_type,
                                   subkey_length=subkey_length,
                                   expire_date=expire_date,
                                   passphrase=passphrase)

    return(gpg.gen_key(input_data))

def list_keys(gpg, *args, **kwargs):
    return(gpg.list_keys(*args, **kwargs))

def delete_keys(gpg, *args, **kwargs):
    return(gpg.delete_keys(*args, **kwargs))

def export_keys(gpg, *args, **kwargs):
    return(gpg.export_keys(*args, **kwargs))

def import_keys(gpg, *args, **kwargs):
    return(gpg.import_keys(*args, **kwargs))

def encrypt(gpg, file=False, *args, **kwargs):
    return(gpg.encrypt(*args, **kwargs) if not (file) else gpg.encrypt_file(*args, **kwargs))

def decrypt(gpg, file=False, *args, **kwargs):
    return(gpg.decrypt(*args, **kwargs) if not (file) else gpg.decrypt_file(*args, **kwargs))

def verify(gpg, file=False, detach=False, *args, **kwargs):
    if (file):
        result = gpg.verify_file(*args, **kwargs)

    elif not (file):
        result = gpg.verify(*args, **kwargs)

    elif (detach):
        result = gpg.verify_data(*args, **kwargs)

def sign(gpg, *args, **kwargs):
    return(gpg.sign(*args, **kwargs))

def scan_keys(gpg, *args, **kwargs):
    return(gpg.scan_keys(*args, **kwargs))

def search_keys(gpg, *args, **kwargs):
    return(gpg.search_keys(*args, **kwargs))

def send_keys(gpg, *args, **kwargs):
    return(gpg.send_keys(*args, **kwargs))

def recv_keys(gpg, *args, **kwargs):
    return(gpg,recv_keys(*args, **kwargs))
