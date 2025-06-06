# Copyright 2023 The GoPlus. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from goplus.address import Address
from goplus.approve import Approve
from goplus.dapp import Dapp
from goplus.decode import Decode
from goplus.errorcode import Code
from goplus.locker import Locker
from goplus.nft import Nft
from goplus.phishing_site import PushingSite
from goplus.rug_pull import RugPull
from goplus.token import Token
from goplus.tx_simulation import TxSimulation


class TokenTest(unittest.TestCase):
    def test_token_security(self):
        # token
        res = Token().token_security(
            chain_id="1", addresses=["0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"]
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)

    def test_solana_token_security(self):

        # solana
        res = Token().solana_token_security(
            addresses=["HZ1JovNiVvGrGNiiYvEozEVgZ58xaU3RKwX8eACQBCt3"]
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)

    def test_sui_token_security(self):

        # sui
        res = Token().sui_token_security(
            addresses=[
                "0x40402a987c2f8a71b755561bfbd16c2cbb991e27e609ad148809491c32bacab9::kui::KUI"
            ]
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)


class AddressTest(unittest.TestCase):
    def test_address_security(self):
        res = Address().address_security(
            address="0xc8b759860149542a98a3eb57c14aadf59d6d89b9"
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)


class ApprovalTest(unittest.TestCase):
    def test_approval_security_v1(self):
        res = Approve().approve_security_v1(
            chain_id="1", address="0x4639cd8cd52ec1cf2e496a606ce28d8afb1c792f"
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)

    def test_token_approval_security(self):
        res = Approve().token_approve_security(
            chain_id="56", address="0xd018e2b543a2669410537f96293590138cacedf3"
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)

    def test_erc721_approval_security(self):
        res = Approve().erc721_approve_security(
            chain_id="1", address="0xd95dbdab08a9fed2d71ac9c3028aac40905d8cf3"
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)

    def test_erc1155_approval_security(self):
        res = Approve().erc1155_approve_security(
            chain_id="56", address="0xb0dccbb9c4a65a94a41a0165aaea79c8b2fc54ce"
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)


class DecodeTest(unittest.TestCase):
    def test_signature_data_decode(self):
        res = Decode(access_token=None).signature_data_decode(
            chain_id="1",
            address="0x4cc8aa0c6ffbe18534584da9b592aa438733ee66",
            data="0xa0712d68000000000000000000000000"
            "0000000000000000000000000000000062fee481",
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)


class NftTest(unittest.TestCase):
    def test_nft_security(self):
        res = Nft().nft_security(
            chain_id="1", address="0x82f5ef9ddc3d231962ba57a9c2ebb307dc8d26c2"
        )
        self.assertIn(res.code, [Code.SUCCESS, Code.DATA_PENDING_SYNC], res.message)


class DappTest(unittest.TestCase):
    def test_dapp_security(self):
        res = Dapp().dapp_security(url="https://for.tube")
        self.assertEqual(res.code, Code.SUCCESS, res.message)


class PhishingSiteTest(unittest.TestCase):
    def test_phishing_site_security(self):
        res = PushingSite().pushing_site_security(url="https://xn--cm-68s.cc/")
        self.assertEqual(res.code, Code.SUCCESS, res.message)


class RugPullTest(unittest.TestCase):
    def test_rug_pull_security(self):
        res = RugPull().rug_pull_security(
            chain_id="1", address="0x6B175474E89094C44Da98b954EedeAC495271d0F"
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)


class LockerTest(unittest.TestCase):
    def test_locker_token(self):
        res = Locker().locker_token(
            chain_id="8453",
            page_num=1,
            page_size=100,
            token_address="0x6fd0303649296360f10c07b24521deda9223086d",
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)

    def test_locker_lp_v3(self):
        res = Locker().locker_lp_v3(
            chain_id="56",
            page_num=1,
            page_size=100,
            pool_address="0x579df956c6cE6178fBBD78bbE4f05786cFBA9B76",
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)


class TxSimulationTest(unittest.TestCase):
    def test_solana_tx_simulation(self):
        res = TxSimulation().solana_tx_simulation(
            encoded_transaction="AT+Td4vATQ8bPgyQPt25Hp6Ve2jECOkwS3+PC5Z8HhLK"
            "/7mDbnQ8tW3sKzQnNeVWxsJzo8knzMhQZbnL+FpzVgOAAQADGuG"
            "EgGi3qMErQECfFXEVxCXlALMU02fKK0Yf27WbmN3in"
            "0h2yAJOqRM87lkKfGtIJh/K1ZeTCGy7baAOhr7lAHEGm4hX/quBhPt"
            "of2NGGMA12sQ53BrrO1WYoPAAAAAAAUHVl1rR1ll4q"
            "3QLbxXmVinsWpdivaeQV/mhOzBJCk8REfu0KcAzb3YRg2Ma9lf/One"
            "Tw5veLElNTzFqNrsDkuYLvA+xH7fegRONkq/Pv7gl"
            "UQsHQHoREAxHUw9pcWEqf8JzpBDzmh14iMUco6VGUnJ5JdUmYvy9vVSA"
            "7Oxsk9U/04YFfm4JbWwLmfCCrhw+JkLOorQ/LWaR1"
            "K9ts6sVhyf7Py+Jb8E9fs7m+Yp0tE0aoYujFI/3KfPd+ElqLb+wi+bW5R"
            "6OHe4FtxpdJLGwx6Vpl5tqHI0b/JFzDt2fRX4DOIT6Ynj"
            "6mq18q+cWm0lZkVpKNXSV+WHJK0O+B/b/M7kKPU71EHDfVbbANy9N/"
            "TBkLtvrgPawBy0NzW5ehEMJ/ciXSyf8WLm80PBN0XBjIIT"
            "O5GQy+w8X4b7lC5ENdeNBQtxtFaOMHuCIMKYErfMjPnIdcZyqF/E2"
            "3LNm67pyWhP4BpxgdtdoBCYrCN+usbbjQi3UwAXrm0zVY6"
            "Y/BpSVhMb6evO+2606PWXzaqvJdDGxu+TC0vbg5HymAgNFL11hjqY"
            "6esn2GopdBm3ZyMw1bOMZM/i2kbQAXFV+SN+vT8Fyjbr97"
            "ysVNCK0N0ppW+uvhHyoakZ54IPbNYs9uSpZxVAe6q5A+cCehtHSM5H"
            "1lGMuCl2Xy9kJpwfYFYHGYz5CEdnDZKSvMTjkXNIUKlSi"
            "Fy/yY6fNErKOUn/kfnyrpIcseSoueZv3kcqOWpwwC/t0MMF1LNOwyHxIN"
            "LlxBSA55tlrnVisLQ4iM8cK+92bmKEIM7Kye02Vb0y/Q"
            "Ki7zQUdfHu14hsh7jlG5aOhjOg75OXUg1wpZ5pceJoVtb4l9BcMwoDLa+MZ"
            "LFA4OAHPRDAYD54/hmMiOsgBBpcQ2/fVBwVKU1qZKSEGT"
            "STocWDaOHx8NbXdvJK7geQfqEBBBUSNAwZGb+UhFzL/7K26csOb57yM5bv"
            "F9xJrLEObOkAAAAB/EQusFKXzoXRK459NkGDBTgIsPmYN/3"
            "ocys69vB4asgUXBgABAhobHAkFoIYBAAAAAAAXIhodGxwAAQMeBAIFBg"
            "cICQoYCwwNDh4DBQ8GEBESExgUFRYxAKCGAQAAAAAAjDwA"
            "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcGAAEAGh"
            "scAQYZAAkDmvYAAAAAAAAZAAUCDCsFAAEZjx9MOkUiY9QTs"
            "s0X68vBoOWIc2TmJhoSqBeS6hZaPgAFAgcAAxA="
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)


if __name__ == "__main__":
    unittest.main()
