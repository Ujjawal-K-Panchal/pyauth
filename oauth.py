"""
Title: OAuth2.
	
Created on Mon Nov 21 11:34:20 2021
@author: Ujjawal.K.Panchal, @Email: ujjawalpanchal32@gmail.com

Copyright (C) Ujjawal K. Panchal - All Rights Reserved.

---
To use this code, propogate the copyright into your repository.
"""
from typing import Union, Optional, Iterable
from pathlib import Path
from pydantic import BaseModel
from datetime import datetime, timedelta

from jose import jwt

class OAuth2():
    def __init__(self,
        TokenClass: BaseModel,
        private_key: Optional[str] = None,
        public_key: Optional[str] = None,
        private_key_file: Union[str, Path] = "creds/private-key.pem",
        public_key_file: Union[str, Path] = "creds/public-key.pem",
        encryption_algorithm: str = "RS256",
        default_expire: int = 5
    ):
        #0. assert tokenclass has "exp" for token expire.
        assert "exp" in TokenClass.__fields__.keys()
        #1. Set Encryption params.
        self.default_expire = default_expire
        self.TokenClass = TokenClass
        self.encryption_algorithm = encryption_algorithm
        #2. get keys.
        if private_key and public_key:
            self.private_key, self.public_key = private_key, public_key
        else: 
            with open(private_key_file, "rb") as privfile:
                self.private_key = privfile.read()
            with open(public_key_file, "rb") as pubfile:
                self.public_key = pubfile.read()
        return
    def payloadTypeCheck(self, payload_data):
                return isinstance(payload_data, dict) or isinstance(payload_data, self.TokenClass) or isinstance(payload_data, Iterable)

    def createToken(self, payload_data: Union[dict, BaseModel, Iterable], expire: Optional[int] = None):
        #0. assert typing.
        assert self.payloadTypeCheck(payload_data), f"`payload_data` can only be instance of types: ({dict},{self.TokenClass}, {Iterable}) but received type: {type(payload_data)}."
        #1. form payload.
        payload = None
        expire = datetime.utcnow() + timedelta(minutes = expire if expire else self.default_expire)
        if isinstance(payload_data, dict):
            payload = self.TokenClass(**payload_data, exp = expire)
        elif isinstance(payload_data, Iterable) and not isinstance(payload_data, BaseModel):
            payload_dict = {key: payload_data[i] for i, key in enumerate(self.TokenClass.__fields__.keys()) if key != "exp"}
            payload_dict["exp"] = expire
            payload = self.TokenClass(**payload_dict)
            
        else: #When payload type = TokenClass.
            payload = payload_data 
        #2. form token.
        token = jwt.encode(payload.dict(), self.private_key, algorithm = self.encryption_algorithm)
        #3. return token.
        return token
    
    def verifyToken(self, token):
        tdata = self.TokenClass(**jwt.decode(token, self.public_key, algorithms = [self.encryption_algorithm]))
        return tdata

if __name__ == "__main__":
    #unit test.
    class BM(BaseModel):
        name: str
        exp: datetime

    oauth2 = OAuth2(BM)
    print(f"{oauth2=}.")

    #1. dict.
    print("===(dict)===")
    token = oauth2.createToken({"name": "JoJo"})
    token_data = oauth2.verifyToken(token)
    print(f"{token=}.")
    print(f"{token_data=}.")
    print("===(/dict)===")
    #2. iterable.
    print("===(iterable)===")
    token = oauth2.createToken(["JoJo",])
    token_data = oauth2.verifyToken(token)
    print(f"{token=}.")
    print(f"{token_data=}.")
    print("===(/iterable)===")
    #3. token class.
    print("===(token class)===")
    token = oauth2.createToken(BM(name = "JoJo", exp = datetime.utcnow() + timedelta(seconds = 5)))
    token_data = oauth2.verifyToken(token)
    print(f"{token=}.")
    print(f"{token_data=}.")
    print("===(/token class)===")


        
