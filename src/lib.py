import base64


def get_decoded_parameters(ds_merchantparameters):
    return eval(base64.standard_b64decode(ds_merchantparameters))


def get_encoded_parameters(parameters):
    return base64.b64encode(parameters.encode())
