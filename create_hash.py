
def decodex(x):
    from base64 import urlsafe_b64decode as decode64
    #x_decoded = bytes.decode(decode64(x.decode()))
    x_ = x.replace("b'", "")
    x_byte = x_.encode()
    x__= decode64(x_byte.decode())
    x_decoded = bytes.decode(x__)
    return x_decoded
def encodex(x):
    from base64 import urlsafe_b64encode as encode64
    x_url = encode64(x.encode())
    return x_url
