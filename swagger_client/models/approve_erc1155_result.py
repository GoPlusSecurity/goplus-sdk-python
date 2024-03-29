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

class ApproveErc1155Result(object):
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
        'address_info': 'ApproveAddressInfo',
        'approved_contract': 'str',
        'approved_time': 'int',
        'hash': 'str',
        'initial_approval_hash': 'str',
        'initial_approval_time': 'int'
    }

    attribute_map = {
        'address_info': 'address_info',
        'approved_contract': 'approved_contract',
        'approved_time': 'approved_time',
        'hash': 'hash',
        'initial_approval_hash': 'initial_approval_hash',
        'initial_approval_time': 'initial_approval_time'
    }

    def __init__(self, address_info=None, approved_contract=None, approved_time=None, hash=None, initial_approval_hash=None, initial_approval_time=None):  # noqa: E501
        """ApproveErc1155Result - a model defined in Swagger"""  # noqa: E501
        self._address_info = None
        self._approved_contract = None
        self._approved_time = None
        self._hash = None
        self._initial_approval_hash = None
        self._initial_approval_time = None
        self.discriminator = None
        if address_info is not None:
            self.address_info = address_info
        if approved_contract is not None:
            self.approved_contract = approved_contract
        if approved_time is not None:
            self.approved_time = approved_time
        if hash is not None:
            self.hash = hash
        if initial_approval_hash is not None:
            self.initial_approval_hash = initial_approval_hash
        if initial_approval_time is not None:
            self.initial_approval_time = initial_approval_time

    @property
    def address_info(self):
        """Gets the address_info of this ApproveErc1155Result.  # noqa: E501


        :return: The address_info of this ApproveErc1155Result.  # noqa: E501
        :rtype: ApproveAddressInfo
        """
        return self._address_info

    @address_info.setter
    def address_info(self, address_info):
        """Sets the address_info of this ApproveErc1155Result.


        :param address_info: The address_info of this ApproveErc1155Result.  # noqa: E501
        :type: ApproveAddressInfo
        """

        self._address_info = address_info

    @property
    def approved_contract(self):
        """Gets the approved_contract of this ApproveErc1155Result.  # noqa: E501

        Spender Address  # noqa: E501

        :return: The approved_contract of this ApproveErc1155Result.  # noqa: E501
        :rtype: str
        """
        return self._approved_contract

    @approved_contract.setter
    def approved_contract(self, approved_contract):
        """Sets the approved_contract of this ApproveErc1155Result.

        Spender Address  # noqa: E501

        :param approved_contract: The approved_contract of this ApproveErc1155Result.  # noqa: E501
        :type: str
        """

        self._approved_contract = approved_contract

    @property
    def approved_time(self):
        """Gets the approved_time of this ApproveErc1155Result.  # noqa: E501

        Latest approval time  # noqa: E501

        :return: The approved_time of this ApproveErc1155Result.  # noqa: E501
        :rtype: int
        """
        return self._approved_time

    @approved_time.setter
    def approved_time(self, approved_time):
        """Sets the approved_time of this ApproveErc1155Result.

        Latest approval time  # noqa: E501

        :param approved_time: The approved_time of this ApproveErc1155Result.  # noqa: E501
        :type: int
        """

        self._approved_time = approved_time

    @property
    def hash(self):
        """Gets the hash of this ApproveErc1155Result.  # noqa: E501

        Latest approval hash  # noqa: E501

        :return: The hash of this ApproveErc1155Result.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ApproveErc1155Result.

        Latest approval hash  # noqa: E501

        :param hash: The hash of this ApproveErc1155Result.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def initial_approval_hash(self):
        """Gets the initial_approval_hash of this ApproveErc1155Result.  # noqa: E501

        Initial approval hash  # noqa: E501

        :return: The initial_approval_hash of this ApproveErc1155Result.  # noqa: E501
        :rtype: str
        """
        return self._initial_approval_hash

    @initial_approval_hash.setter
    def initial_approval_hash(self, initial_approval_hash):
        """Sets the initial_approval_hash of this ApproveErc1155Result.

        Initial approval hash  # noqa: E501

        :param initial_approval_hash: The initial_approval_hash of this ApproveErc1155Result.  # noqa: E501
        :type: str
        """

        self._initial_approval_hash = initial_approval_hash

    @property
    def initial_approval_time(self):
        """Gets the initial_approval_time of this ApproveErc1155Result.  # noqa: E501

        Initial approval time  # noqa: E501

        :return: The initial_approval_time of this ApproveErc1155Result.  # noqa: E501
        :rtype: int
        """
        return self._initial_approval_time

    @initial_approval_time.setter
    def initial_approval_time(self, initial_approval_time):
        """Sets the initial_approval_time of this ApproveErc1155Result.

        Initial approval time  # noqa: E501

        :param initial_approval_time: The initial_approval_time of this ApproveErc1155Result.  # noqa: E501
        :type: int
        """

        self._initial_approval_time = initial_approval_time

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
        if issubclass(ApproveErc1155Result, dict):
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
        if not isinstance(other, ApproveErc1155Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
