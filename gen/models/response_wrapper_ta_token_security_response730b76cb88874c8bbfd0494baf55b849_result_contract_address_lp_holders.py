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

class ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders(object):
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
        'is_locked': 'int',
        'is_contract': 'int',
        'address': 'str',
        'balance': 'str',
        'locked_detail': 'list[str]',
        'tag': 'str',
        'percent': 'str'
    }

    attribute_map = {
        'is_locked': 'is_locked',
        'is_contract': 'is_contract',
        'address': 'address',
        'balance': 'balance',
        'locked_detail': 'locked_detail',
        'tag': 'tag',
        'percent': 'percent'
    }

    def __init__(self, is_locked=None, is_contract=None, address=None, balance=None, locked_detail=None, tag=None, percent=None):  # noqa: E501
        """ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders - a model defined in Swagger"""  # noqa: E501
        self._is_locked = None
        self._is_contract = None
        self._address = None
        self._balance = None
        self._locked_detail = None
        self._tag = None
        self._percent = None
        self.discriminator = None
        if is_locked is not None:
            self.is_locked = is_locked
        if is_contract is not None:
            self.is_contract = is_contract
        if address is not None:
            self.address = address
        if balance is not None:
            self.balance = balance
        if locked_detail is not None:
            self.locked_detail = locked_detail
        if tag is not None:
            self.tag = tag
        if percent is not None:
            self.percent = percent

    @property
    def is_locked(self):
        """Gets the is_locked of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501

        It describes whether the tokens owned by the holder are locked \"1\" means true; \"0\" means false;  (3) “tag” describes the address's public tag. Example:Burn (Notice:About \"locked\": We only support the token lock addresses or black hole addresses that we have included. )  # noqa: E501

        :return: The is_locked of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :rtype: int
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.

        It describes whether the tokens owned by the holder are locked \"1\" means true; \"0\" means false;  (3) “tag” describes the address's public tag. Example:Burn (Notice:About \"locked\": We only support the token lock addresses or black hole addresses that we have included. )  # noqa: E501

        :param is_locked: The is_locked of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :type: int
        """

        self._is_locked = is_locked

    @property
    def is_contract(self):
        """Gets the is_contract of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501

        It describes whether the holder is a contract \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The is_contract of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :rtype: int
        """
        return self._is_contract

    @is_contract.setter
    def is_contract(self, is_contract):
        """Sets the is_contract of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.

        It describes whether the holder is a contract \"1\" means true; \"0\" means false.  # noqa: E501

        :param is_contract: The is_contract of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :type: int
        """

        self._is_contract = is_contract

    @property
    def address(self):
        """Gets the address of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501

        It describes the holder address;   # noqa: E501

        :return: The address of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.

        It describes the holder address;   # noqa: E501

        :param address: The address of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def balance(self):
        """Gets the balance of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501

        It describes the balance of the holder.   # noqa: E501

        :return: The balance of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.

        It describes the balance of the holder.   # noqa: E501

        :param balance: The balance of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :type: str
        """

        self._balance = balance

    @property
    def locked_detail(self):
        """Gets the locked_detail of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501

        It is an array, decribes lock position info of this holder, only shows when \"locked\": 1. This Array may contain multiple objects for multiple locking info. In every objetc, \"amount\" describes the number of token locked, \"end_time\" describes when the token will be unlocked, \"opt_time\" describes when the token was locked.(Notice:When \"locked\":0, or lock address is a black hole address,  \"locked_detail\" will be no return.)  # noqa: E501

        :return: The locked_detail of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :rtype: list[str]
        """
        return self._locked_detail

    @locked_detail.setter
    def locked_detail(self, locked_detail):
        """Sets the locked_detail of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.

        It is an array, decribes lock position info of this holder, only shows when \"locked\": 1. This Array may contain multiple objects for multiple locking info. In every objetc, \"amount\" describes the number of token locked, \"end_time\" describes when the token will be unlocked, \"opt_time\" describes when the token was locked.(Notice:When \"locked\":0, or lock address is a black hole address,  \"locked_detail\" will be no return.)  # noqa: E501

        :param locked_detail: The locked_detail of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :type: list[str]
        """

        self._locked_detail = locked_detail

    @property
    def tag(self):
        """Gets the tag of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501

        It describes the address's public tag. Example:Burn Address/Deployer;   # noqa: E501

        :return: The tag of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.

        It describes the address's public tag. Example:Burn Address/Deployer;   # noqa: E501

        :param tag: The tag of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def percent(self):
        """Gets the percent of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501

        It  describes the percentage of tokens held by this holder (Notice:About \"percent\": 1 means 100% here.)  # noqa: E501

        :return: The percent of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :rtype: str
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.

        It  describes the percentage of tokens held by this holder (Notice:About \"percent\": 1 means 100% here.)  # noqa: E501

        :param percent: The percent of this ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders.  # noqa: E501
        :type: str
        """

        self._percent = percent

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
        if issubclass(ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders, dict):
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
        if not isinstance(other, ResponseWrapperTaTokenSecurityResponse730b76cb88874c8bbfd0494baf55b849ResultContractAddressLpHolders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
