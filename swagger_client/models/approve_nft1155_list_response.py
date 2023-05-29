# coding: utf-8

"""
    GoPlus Security API Document

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ApproveNFT1155ListResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'approved_list': 'list[ApproveErc1155Result]',
        'chain_id': 'str',
        'is_open_source': 'int',
        'is_verified': 'int',
        'malicious_address': 'int',
        'malicious_behavior': 'list[str]',
        'nft_address': 'str',
        'nft_name': 'str',
        'nft_symbol': 'str'
    }

    attribute_map = {
        'approved_list': 'approved_list',
        'chain_id': 'chain_id',
        'is_open_source': 'is_open_source',
        'is_verified': 'is_verified',
        'malicious_address': 'malicious_address',
        'malicious_behavior': 'malicious_behavior',
        'nft_address': 'nft_address',
        'nft_name': 'nft_name',
        'nft_symbol': 'nft_symbol'
    }

    def __init__(self, approved_list=None, chain_id=None, is_open_source=None, is_verified=None, malicious_address=None, malicious_behavior=None, nft_address=None, nft_name=None, nft_symbol=None):  # noqa: E501
        """ApproveNFT1155ListResponse - a model defined in Swagger"""  # noqa: E501
        self._approved_list = None
        self._chain_id = None
        self._is_open_source = None
        self._is_verified = None
        self._malicious_address = None
        self._malicious_behavior = None
        self._nft_address = None
        self._nft_name = None
        self._nft_symbol = None
        self.discriminator = None
        if approved_list is not None:
            self.approved_list = approved_list
        if chain_id is not None:
            self.chain_id = chain_id
        if is_open_source is not None:
            self.is_open_source = is_open_source
        if is_verified is not None:
            self.is_verified = is_verified
        if malicious_address is not None:
            self.malicious_address = malicious_address
        if malicious_behavior is not None:
            self.malicious_behavior = malicious_behavior
        if nft_address is not None:
            self.nft_address = nft_address
        if nft_name is not None:
            self.nft_name = nft_name
        if nft_symbol is not None:
            self.nft_symbol = nft_symbol

    @property
    def approved_list(self):
        """Gets the approved_list of this ApproveNFT1155ListResponse.  # noqa: E501


        :return: The approved_list of this ApproveNFT1155ListResponse.  # noqa: E501
        :rtype: list[ApproveErc1155Result]
        """
        return self._approved_list

    @approved_list.setter
    def approved_list(self, approved_list):
        """Sets the approved_list of this ApproveNFT1155ListResponse.


        :param approved_list: The approved_list of this ApproveNFT1155ListResponse.  # noqa: E501
        :type: list[ApproveErc1155Result]
        """

        self._approved_list = approved_list

    @property
    def chain_id(self):
        """Gets the chain_id of this ApproveNFT1155ListResponse.  # noqa: E501

        ChainID  # noqa: E501

        :return: The chain_id of this ApproveNFT1155ListResponse.  # noqa: E501
        :rtype: str
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this ApproveNFT1155ListResponse.

        ChainID  # noqa: E501

        :param chain_id: The chain_id of this ApproveNFT1155ListResponse.  # noqa: E501
        :type: str
        """

        self._chain_id = chain_id

    @property
    def is_open_source(self):
        """Gets the is_open_source of this ApproveNFT1155ListResponse.  # noqa: E501

        Whether the contract is verified on blockchain explorer.  # noqa: E501

        :return: The is_open_source of this ApproveNFT1155ListResponse.  # noqa: E501
        :rtype: int
        """
        return self._is_open_source

    @is_open_source.setter
    def is_open_source(self, is_open_source):
        """Sets the is_open_source of this ApproveNFT1155ListResponse.

        Whether the contract is verified on blockchain explorer.  # noqa: E501

        :param is_open_source: The is_open_source of this ApproveNFT1155ListResponse.  # noqa: E501
        :type: int
        """

        self._is_open_source = is_open_source

    @property
    def is_verified(self):
        """Gets the is_verified of this ApproveNFT1155ListResponse.  # noqa: E501

        Whether NFT is certified on a reputable trading platform.  # noqa: E501

        :return: The is_verified of this ApproveNFT1155ListResponse.  # noqa: E501
        :rtype: int
        """
        return self._is_verified

    @is_verified.setter
    def is_verified(self, is_verified):
        """Sets the is_verified of this ApproveNFT1155ListResponse.

        Whether NFT is certified on a reputable trading platform.  # noqa: E501

        :param is_verified: The is_verified of this ApproveNFT1155ListResponse.  # noqa: E501
        :type: int
        """

        self._is_verified = is_verified

    @property
    def malicious_address(self):
        """Gets the malicious_address of this ApproveNFT1155ListResponse.  # noqa: E501

        Whether the NFT is malicious or contains high risk.  # noqa: E501

        :return: The malicious_address of this ApproveNFT1155ListResponse.  # noqa: E501
        :rtype: int
        """
        return self._malicious_address

    @malicious_address.setter
    def malicious_address(self, malicious_address):
        """Sets the malicious_address of this ApproveNFT1155ListResponse.

        Whether the NFT is malicious or contains high risk.  # noqa: E501

        :param malicious_address: The malicious_address of this ApproveNFT1155ListResponse.  # noqa: E501
        :type: int
        """

        self._malicious_address = malicious_address

    @property
    def malicious_behavior(self):
        """Gets the malicious_behavior of this ApproveNFT1155ListResponse.  # noqa: E501

        Specific malicious behaviors or risks of this NFT.  # noqa: E501

        :return: The malicious_behavior of this ApproveNFT1155ListResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._malicious_behavior

    @malicious_behavior.setter
    def malicious_behavior(self, malicious_behavior):
        """Sets the malicious_behavior of this ApproveNFT1155ListResponse.

        Specific malicious behaviors or risks of this NFT.  # noqa: E501

        :param malicious_behavior: The malicious_behavior of this ApproveNFT1155ListResponse.  # noqa: E501
        :type: list[str]
        """

        self._malicious_behavior = malicious_behavior

    @property
    def nft_address(self):
        """Gets the nft_address of this ApproveNFT1155ListResponse.  # noqa: E501

        NFT address  # noqa: E501

        :return: The nft_address of this ApproveNFT1155ListResponse.  # noqa: E501
        :rtype: str
        """
        return self._nft_address

    @nft_address.setter
    def nft_address(self, nft_address):
        """Sets the nft_address of this ApproveNFT1155ListResponse.

        NFT address  # noqa: E501

        :param nft_address: The nft_address of this ApproveNFT1155ListResponse.  # noqa: E501
        :type: str
        """

        self._nft_address = nft_address

    @property
    def nft_name(self):
        """Gets the nft_name of this ApproveNFT1155ListResponse.  # noqa: E501

        NFT name  # noqa: E501

        :return: The nft_name of this ApproveNFT1155ListResponse.  # noqa: E501
        :rtype: str
        """
        return self._nft_name

    @nft_name.setter
    def nft_name(self, nft_name):
        """Sets the nft_name of this ApproveNFT1155ListResponse.

        NFT name  # noqa: E501

        :param nft_name: The nft_name of this ApproveNFT1155ListResponse.  # noqa: E501
        :type: str
        """

        self._nft_name = nft_name

    @property
    def nft_symbol(self):
        """Gets the nft_symbol of this ApproveNFT1155ListResponse.  # noqa: E501

        NFT symbol  # noqa: E501

        :return: The nft_symbol of this ApproveNFT1155ListResponse.  # noqa: E501
        :rtype: str
        """
        return self._nft_symbol

    @nft_symbol.setter
    def nft_symbol(self, nft_symbol):
        """Sets the nft_symbol of this ApproveNFT1155ListResponse.

        NFT symbol  # noqa: E501

        :param nft_symbol: The nft_symbol of this ApproveNFT1155ListResponse.  # noqa: E501
        :type: str
        """

        self._nft_symbol = nft_symbol

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ApproveNFT1155ListResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApproveNFT1155ListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
