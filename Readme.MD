# pyauth2: Python Library for Easy JWT based Authentication Protocols Implementation.

## Generating sample public and private keys: (you don't need to do it. It's here only for reproducibility, unit testing and future analysis.)
1. `openssl genrsa -out ./creds/private-key.pem`
2. `openssl rsa -in ./creds/private-key.pem -pubout -out ./creds/public-key.pem`

## Installation Instructions.
1. Clone the repo: `git clone git@github.com:Ujjawal-K-Panchal/pyauth.git`
2. Create a Virtual Environment: (Optional but Recommended).
  - `pip install virtualenv`.
  - `python -m venv <any-name>`.
  - Linux, Mac: `source <any-name>/bin/activate`. Windows: `<any-name>\Scripts\activate`.
4. Install the repo: `pip install ./pyauth`

## Usage Example:

```python
from datetime import datetime, timedelta
from pydantic import BaseModel
from pyauth.oauth import OAuth2

class BM(BaseModel):
    name: str
    exp: datetime #musthave field.

oauth2 = OAuth2(BM)

#1. dict.
token = oauth2.createToken({"name": "JoJo"})
token_data = oauth2.verifyToken(token)

#2. iterable.
token = oauth2.createToken(["JoJo",])
token_data = oauth2.verifyToken(token)

#3. token class.
token = oauth2.createToken(BM(name = "JoJo", exp = datetime.utcnow() + timedelta(seconds = 5)))
token_data = oauth2.verifyToken(token)
```

