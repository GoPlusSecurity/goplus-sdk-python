# GoPlus SDK  For Python

### Installation

```
pip install goplus
```

### Get AccessToken
```python
from goplus.auth import Auth

token_data = Auth(key="", secret="").get_access_token()
print(token_data)
```


### Get Supported Blockchains

```python
from goplus.chain import Chain

chain_list = Chain.get_chain_list()
print(chain_list)
```

### Token Security

```python
from goplus.token import Token

data = Token(access_token=None).token_security(chain_id="1", addresses=["0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"])
print(data)
```

### Address Security

```python
from goplus.address import Address

res = Address(access_token=None).address_security(address="0xc8b759860149542a98a3eb57c14aadf59d6d89b9")
print(res)
```


### Approval Security API v1
```python
from goplus.approve import Approve

res = Approve(access_token=None).approve_security_v1(chain_id="1", address="0x4639cd8cd52ec1cf2e496a606ce28d8afb1c792f")
print(res)
```


### Approval Security API v2

#### Token Approval Security

```python
from goplus.approve import Approve

res = Approve(access_token=None).token_approve_security(chain_id="56", address="0xd018e2b543a2669410537f96293590138cacedf3")
print(res)
```

#### ERC721 NFT Approval Security

```python
from goplus.approve import Approve

res = Approve(access_token=None).erc721_approve_security(chain_id="1", address="0xd95dbdab08a9fed2d71ac9c3028aac40905d8cf3")
print(res)
```

#### ERC1155 NFT Approval Security

```python
from goplus.approve import Approve

res = Approve(access_token=None).erc1155_approve_security(chain_id="56", address="0xb0dccbb9c4a65a94a41a0165aaea79c8b2fc54ce")
print(res)

```


### Signature Data Decode
```python
from goplus.decode import Decode

res = Decode(access_token=None).signature_data_decode(chain_id="1",
                                                    address="0x4cc8aa0c6ffbe18534584da9b592aa438733ee66",
                                                    data="0xa0712d680000000000000000000000000000000000000000000000000000000062fee481")
print(res)

```
### NFT Security
```python
from goplus.nft import Nft

res = Nft(access_token=None).nft_security(chain_id="1", address="0x82f5ef9ddc3d231962ba57a9c2ebb307dc8d26c2")
print(res)

```

### dApp Security Info API
```python
from goplus.dapp import Dapp

res = Dapp(access_token=None).dapp_security(url="https://for.tube")
print(res)

```

### Phishing Site Detection API
```python
from goplus.phishing_site import PushingSite

res = PushingSite(access_token=None).pushing_site_security(url="https://xn--cm-68s.cc/")
print(res)

```
