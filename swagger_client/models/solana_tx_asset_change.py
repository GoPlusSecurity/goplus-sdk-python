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

class SolanaTxAssetChange(object):
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
        'mint': 'str',
        'symbol': 'str',
        'change_detail': 'list[SolanaTxChangeDetail]',
        'decimals': 'int',
        'name': 'str'
    }

    attribute_map = {
        'mint': 'mint',
        'symbol': 'symbol',
        'change_detail': 'change_detail',
        'decimals': 'decimals',
        'name': 'name'
    }

    def __init__(self, mint=None, symbol=None, change_detail=None, decimals=None, name=None):  # noqa: E501
        """SolanaTxAssetChange - a model defined in Swagger"""  # noqa: E501
        self._mint = None
        self._symbol = None
        self._change_detail = None
        self._decimals = None
        self._name = None
        self.discriminator = None
        if mint is not None:
            self.mint = mint
        if symbol is not None:
            self.symbol = symbol
        if change_detail is not None:
            self.change_detail = change_detail
        if decimals is not None:
            self.decimals = decimals
        if name is not None:
            self.name = name

    @property
    def mint(self):
        """Gets the mint of this SolanaTxAssetChange.  # noqa: E501


        :return: The mint of this SolanaTxAssetChange.  # noqa: E501
        :rtype: str
        """
        return self._mint

    @mint.setter
    def mint(self, mint):
        """Sets the mint of this SolanaTxAssetChange.


        :param mint: The mint of this SolanaTxAssetChange.  # noqa: E501
        :type: str
        """

        self._mint = mint

    @property
    def symbol(self):
        """Gets the symbol of this SolanaTxAssetChange.  # noqa: E501


        :return: The symbol of this SolanaTxAssetChange.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this SolanaTxAssetChange.


        :param symbol: The symbol of this SolanaTxAssetChange.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def change_detail(self):
        """Gets the change_detail of this SolanaTxAssetChange.  # noqa: E501


        :return: The change_detail of this SolanaTxAssetChange.  # noqa: E501
        :rtype: list[SolanaTxChangeDetail]
        """
        return self._change_detail

    @change_detail.setter
    def change_detail(self, change_detail):
        """Sets the change_detail of this SolanaTxAssetChange.


        :param change_detail: The change_detail of this SolanaTxAssetChange.  # noqa: E501
        :type: list[SolanaTxChangeDetail]
        """

        self._change_detail = change_detail

    @property
    def decimals(self):
        """Gets the decimals of this SolanaTxAssetChange.  # noqa: E501


        :return: The decimals of this SolanaTxAssetChange.  # noqa: E501
        :rtype: int
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """Sets the decimals of this SolanaTxAssetChange.


        :param decimals: The decimals of this SolanaTxAssetChange.  # noqa: E501
        :type: int
        """

        self._decimals = decimals

    @property
    def name(self):
        """Gets the name of this SolanaTxAssetChange.  # noqa: E501


        :return: The name of this SolanaTxAssetChange.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SolanaTxAssetChange.


        :param name: The name of this SolanaTxAssetChange.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(SolanaTxAssetChange, dict):
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
        if not isinstance(other, SolanaTxAssetChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
