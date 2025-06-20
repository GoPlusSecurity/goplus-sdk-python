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

class ResponseWrapperSolanaTokenSecurityMetadata(object):
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
        'symbol': 'str',
        'name': 'str',
        'description': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'name': 'name',
        'description': 'description',
        'uri': 'uri'
    }

    def __init__(self, symbol=None, name=None, description=None, uri=None):  # noqa: E501
        """ResponseWrapperSolanaTokenSecurityMetadata - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._name = None
        self._description = None
        self._uri = None
        self.discriminator = None
        if symbol is not None:
            self.symbol = symbol
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if uri is not None:
            self.uri = uri

    @property
    def symbol(self):
        """Gets the symbol of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501

        Symbol of the token.  # noqa: E501

        :return: The symbol of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this ResponseWrapperSolanaTokenSecurityMetadata.

        Symbol of the token.  # noqa: E501

        :param symbol: The symbol of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def name(self):
        """Gets the name of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501

        Name of the token.  # noqa: E501

        :return: The name of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseWrapperSolanaTokenSecurityMetadata.

        Name of the token.  # noqa: E501

        :param name: The name of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501

        Description of the token.  # noqa: E501

        :return: The description of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponseWrapperSolanaTokenSecurityMetadata.

        Description of the token.  # noqa: E501

        :param description: The description of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def uri(self):
        """Gets the uri of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501

        URI pointing to related token information.  # noqa: E501

        :return: The uri of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ResponseWrapperSolanaTokenSecurityMetadata.

        URI pointing to related token information.  # noqa: E501

        :param uri: The uri of this ResponseWrapperSolanaTokenSecurityMetadata.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(ResponseWrapperSolanaTokenSecurityMetadata, dict):
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
        if not isinstance(other, ResponseWrapperSolanaTokenSecurityMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
