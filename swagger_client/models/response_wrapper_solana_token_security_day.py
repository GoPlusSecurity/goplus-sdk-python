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

class ResponseWrapperSolanaTokenSecurityDay(object):
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
        'volume': 'str',
        'price_min': 'str',
        'price_max': 'str'
    }

    attribute_map = {
        'volume': 'volume',
        'price_min': 'price_min',
        'price_max': 'price_max'
    }

    def __init__(self, volume=None, price_min=None, price_max=None):  # noqa: E501
        """ResponseWrapperSolanaTokenSecurityDay - a model defined in Swagger"""  # noqa: E501
        self._volume = None
        self._price_min = None
        self._price_max = None
        self.discriminator = None
        if volume is not None:
            self.volume = volume
        if price_min is not None:
            self.price_min = price_min
        if price_max is not None:
            self.price_max = price_max

    @property
    def volume(self):
        """Gets the volume of this ResponseWrapperSolanaTokenSecurityDay.  # noqa: E501

        The volume of transactions during this period.  # noqa: E501

        :return: The volume of this ResponseWrapperSolanaTokenSecurityDay.  # noqa: E501
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this ResponseWrapperSolanaTokenSecurityDay.

        The volume of transactions during this period.  # noqa: E501

        :param volume: The volume of this ResponseWrapperSolanaTokenSecurityDay.  # noqa: E501
        :type: str
        """

        self._volume = volume

    @property
    def price_min(self):
        """Gets the price_min of this ResponseWrapperSolanaTokenSecurityDay.  # noqa: E501

        Minimum price during this period.  # noqa: E501

        :return: The price_min of this ResponseWrapperSolanaTokenSecurityDay.  # noqa: E501
        :rtype: str
        """
        return self._price_min

    @price_min.setter
    def price_min(self, price_min):
        """Sets the price_min of this ResponseWrapperSolanaTokenSecurityDay.

        Minimum price during this period.  # noqa: E501

        :param price_min: The price_min of this ResponseWrapperSolanaTokenSecurityDay.  # noqa: E501
        :type: str
        """

        self._price_min = price_min

    @property
    def price_max(self):
        """Gets the price_max of this ResponseWrapperSolanaTokenSecurityDay.  # noqa: E501

        Maximum price during this period.  # noqa: E501

        :return: The price_max of this ResponseWrapperSolanaTokenSecurityDay.  # noqa: E501
        :rtype: str
        """
        return self._price_max

    @price_max.setter
    def price_max(self, price_max):
        """Sets the price_max of this ResponseWrapperSolanaTokenSecurityDay.

        Maximum price during this period.  # noqa: E501

        :param price_max: The price_max of this ResponseWrapperSolanaTokenSecurityDay.  # noqa: E501
        :type: str
        """

        self._price_max = price_max

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
        if issubclass(ResponseWrapperSolanaTokenSecurityDay, dict):
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
        if not isinstance(other, ResponseWrapperSolanaTokenSecurityDay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
