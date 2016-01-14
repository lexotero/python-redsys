import base64


def get_decoded_parameters(ds_merchantparameters):
    return eval(base64.standard_b64decode(ds_merchantparameters))
