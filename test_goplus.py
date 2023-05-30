import unittest

from goplus.address import Address
from goplus.approve import Approve
from goplus.dapp import Dapp
from goplus.decode import Decode
from goplus.errocode import Code
from goplus.nft import Nft
from goplus.phishing_site import PushingSite
from goplus.rug_pull import RugPull
from goplus.token import Token


class TokenTest(unittest.TestCase):
    def test_token_security(self):
        res = Token().token_security(
            chain_id="1", addresses=["0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"]
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
    def test_rug_pull_detection(self):
        res = RugPull().rug_pull_security(
            chain_id="1", address="0x6B175474E89094C44Da98b954EedeAC495271d0F"
        )
        self.assertEqual(res.code, Code.SUCCESS, res.message)


if __name__ == "__main__":
    unittest.main()
