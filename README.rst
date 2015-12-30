==========
redsys-256
==========

This package generate the form parameters for Redsys payment request:
- Ds_MerchantParameters
- Ds_Signature
- Ds_SignatureVersion

The new protocol uses HMAC SHA256 for sign the parameters and JSON format b64 encoded parameters.

This package defines tow Python classes:
- Commerce
- Transaction

The first one allows to define the merchant and the second defines a transaction.

The Commerce class is used to sign the parameters of the transaction created through Transaction class with the function
generate_form_parameters(). This function returns al the required form parameters listed above.

Thanks
------
Thanks to the Python redsys package creators. I use this package to understand the Redsys protocol.

