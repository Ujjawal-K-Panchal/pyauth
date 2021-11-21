# pyauth2: Python Library for Easy OAuth2 Implementation.

## Generating sample public and private keys: (you don't need to do it. It's here only for reproducibility, unit testing and future analysis.)
1. `openssl genrsa -out ./creds/private-key.pem`
2. `openssl rsa -in ./creds/private-key.pem -pubout -out ./creds/public-key.pem`

