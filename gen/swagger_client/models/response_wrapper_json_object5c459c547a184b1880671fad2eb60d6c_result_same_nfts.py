# coding: utf-8

"""
    GoPlus Security API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts(object):
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
        'nft_address': 'str',
        'nft_name': 'str',
        'nft_owner_number': 'int',
        'create_block_number': 'int',
        'nft_symbol': 'str'
    }

    attribute_map = {
        'nft_address': 'nft_address',
        'nft_name': 'nft_name',
        'nft_owner_number': 'nft_owner_number',
        'create_block_number': 'create_block_number',
        'nft_symbol': 'nft_symbol'
    }

    def __init__(self, nft_address=None, nft_name=None, nft_owner_number=None, create_block_number=None, nft_symbol=None):  # noqa: E501
        """ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts - a model defined in Swagger"""  # noqa: E501
        self._nft_address = None
        self._nft_name = None
        self._nft_owner_number = None
        self._create_block_number = None
        self._nft_symbol = None
        self.discriminator = None
        if nft_address is not None:
            self.nft_address = nft_address
        if nft_name is not None:
            self.nft_name = nft_name
        if nft_owner_number is not None:
            self.nft_owner_number = nft_owner_number
        if create_block_number is not None:
            self.create_block_number = create_block_number
        if nft_symbol is not None:
            self.nft_symbol = nft_symbol

    @property
    def nft_address(self):
        """Gets the nft_address of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501

        It describes the address of the NFTs;  # noqa: E501

        :return: The nft_address of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
        :rtype: str
        """
        return self._nft_address

    @nft_address.setter
    def nft_address(self, nft_address):
        """Sets the nft_address of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.

        It describes the address of the NFTs;  # noqa: E501

        :param nft_address: The nft_address of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
        :type: str
        """

        self._nft_address = nft_address

    @property
    def nft_name(self):
        """Gets the nft_name of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501

        It describes the name of the NFT;  # noqa: E501

        :return: The nft_name of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
        :rtype: str
        """
        return self._nft_name

    @nft_name.setter
    def nft_name(self, nft_name):
        """Sets the nft_name of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.

        It describes the name of the NFT;  # noqa: E501

        :param nft_name: The nft_name of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
        :type: str
        """

        self._nft_name = nft_name

    @property
    def nft_owner_number(self):
        """Gets the nft_owner_number of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501

        It describes the holders of the NFT;  # noqa: E501

        :return: The nft_owner_number of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
        :rtype: int
        """
        return self._nft_owner_number

    @nft_owner_number.setter
    def nft_owner_number(self, nft_owner_number):
        """Sets the nft_owner_number of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.

        It describes the holders of the NFT;  # noqa: E501

        :param nft_owner_number: The nft_owner_number of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
        :type: int
        """

        self._nft_owner_number = nft_owner_number

    @property
    def create_block_number(self):
        """Gets the create_block_number of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501

        describes the number of blocks created for the NFT. Return \"null\" means no NFTs with duplicate name and symbol.  # noqa: E501

        :return: The create_block_number of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
        :rtype: int
        """
        return self._create_block_number

    @create_block_number.setter
    def create_block_number(self, create_block_number):
        """Sets the create_block_number of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.

        describes the number of blocks created for the NFT. Return \"null\" means no NFTs with duplicate name and symbol.  # noqa: E501

        :param create_block_number: The create_block_number of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
        :type: int
        """

        self._create_block_number = create_block_number

    @property
    def nft_symbol(self):
        """Gets the nft_symbol of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501

        It describes the symbol of the NFT;  # noqa: E501

        :return: The nft_symbol of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
        :rtype: str
        """
        return self._nft_symbol

    @nft_symbol.setter
    def nft_symbol(self, nft_symbol):
        """Sets the nft_symbol of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.

        It describes the symbol of the NFT;  # noqa: E501

        :param nft_symbol: The nft_symbol of this ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts.  # noqa: E501
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
        if issubclass(ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts, dict):
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
        if not isinstance(other, ResponseWrapperJSONObject5c459c547a184b1880671fad2eb60d6cResultSameNfts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
