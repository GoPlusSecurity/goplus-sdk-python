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

class ResponseWrapperGetDefiInfoResult(object):
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
        'owner': 'ResponseWrapperGetDefiInfoResultOwner',
        'privilege_withdraw': 'int',
        'withdraw_missing': 'int',
        'is_open_source': 'int',
        'blacklist': 'int',
        'contract_name': 'str',
        'selfdestruct': 'int',
        'is_proxy': 'int',
        'approval_abuse': 'int'
    }

    attribute_map = {
        'owner': 'owner',
        'privilege_withdraw': 'privilege_withdraw',
        'withdraw_missing': 'withdraw_missing',
        'is_open_source': 'is_open_source',
        'blacklist': 'blacklist',
        'contract_name': 'contract_name',
        'selfdestruct': 'selfdestruct',
        'is_proxy': 'is_proxy',
        'approval_abuse': 'approval_abuse'
    }

    def __init__(self, owner=None, privilege_withdraw=None, withdraw_missing=None, is_open_source=None, blacklist=None, contract_name=None, selfdestruct=None, is_proxy=None, approval_abuse=None):  # noqa: E501
        """ResponseWrapperGetDefiInfoResult - a model defined in Swagger"""  # noqa: E501
        self._owner = None
        self._privilege_withdraw = None
        self._withdraw_missing = None
        self._is_open_source = None
        self._blacklist = None
        self._contract_name = None
        self._selfdestruct = None
        self._is_proxy = None
        self._approval_abuse = None
        self.discriminator = None
        if owner is not None:
            self.owner = owner
        if privilege_withdraw is not None:
            self.privilege_withdraw = privilege_withdraw
        if withdraw_missing is not None:
            self.withdraw_missing = withdraw_missing
        if is_open_source is not None:
            self.is_open_source = is_open_source
        if blacklist is not None:
            self.blacklist = blacklist
        if contract_name is not None:
            self.contract_name = contract_name
        if selfdestruct is not None:
            self.selfdestruct = selfdestruct
        if is_proxy is not None:
            self.is_proxy = is_proxy
        if approval_abuse is not None:
            self.approval_abuse = approval_abuse

    @property
    def owner(self):
        """Gets the owner of this ResponseWrapperGetDefiInfoResult.  # noqa: E501


        :return: The owner of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :rtype: ResponseWrapperGetDefiInfoResultOwner
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ResponseWrapperGetDefiInfoResult.


        :param owner: The owner of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :type: ResponseWrapperGetDefiInfoResultOwner
        """

        self._owner = owner

    @property
    def privilege_withdraw(self):
        """Gets the privilege_withdraw of this ResponseWrapperGetDefiInfoResult.  # noqa: E501

        It descirbes whether the contract owner can withdraw all the assets in the contract, without uses' permission. \"1\" means true; \"0\" means false;  \"-1\" means unknown.  # noqa: E501

        :return: The privilege_withdraw of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._privilege_withdraw

    @privilege_withdraw.setter
    def privilege_withdraw(self, privilege_withdraw):
        """Sets the privilege_withdraw of this ResponseWrapperGetDefiInfoResult.

        It descirbes whether the contract owner can withdraw all the assets in the contract, without uses' permission. \"1\" means true; \"0\" means false;  \"-1\" means unknown.  # noqa: E501

        :param privilege_withdraw: The privilege_withdraw of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :type: int
        """

        self._privilege_withdraw = privilege_withdraw

    @property
    def withdraw_missing(self):
        """Gets the withdraw_missing of this ResponseWrapperGetDefiInfoResult.  # noqa: E501

        It describes whether the contract lacks withdrawal method. If it is missing, users will be unable to withdraw the assets they have putted in. \"1\" means true; \"0\" means false;  \"-1\" means unknown.  # noqa: E501

        :return: The withdraw_missing of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._withdraw_missing

    @withdraw_missing.setter
    def withdraw_missing(self, withdraw_missing):
        """Sets the withdraw_missing of this ResponseWrapperGetDefiInfoResult.

        It describes whether the contract lacks withdrawal method. If it is missing, users will be unable to withdraw the assets they have putted in. \"1\" means true; \"0\" means false;  \"-1\" means unknown.  # noqa: E501

        :param withdraw_missing: The withdraw_missing of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :type: int
        """

        self._withdraw_missing = withdraw_missing

    @property
    def is_open_source(self):
        """Gets the is_open_source of this ResponseWrapperGetDefiInfoResult.  # noqa: E501

        It describes whether this contract is open source.  \"1\" means true;  \"0\" means false.  # noqa: E501

        :return: The is_open_source of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._is_open_source

    @is_open_source.setter
    def is_open_source(self, is_open_source):
        """Sets the is_open_source of this ResponseWrapperGetDefiInfoResult.

        It describes whether this contract is open source.  \"1\" means true;  \"0\" means false.  # noqa: E501

        :param is_open_source: The is_open_source of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :type: int
        """

        self._is_open_source = is_open_source

    @property
    def blacklist(self):
        """Gets the blacklist of this ResponseWrapperGetDefiInfoResult.  # noqa: E501

        It describes whether the contract has blacklist function that would block user from withdrawing their assets. \"1\" means true; \"0\" means false;  \"-1\" means unknown.  # noqa: E501

        :return: The blacklist of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._blacklist

    @blacklist.setter
    def blacklist(self, blacklist):
        """Sets the blacklist of this ResponseWrapperGetDefiInfoResult.

        It describes whether the contract has blacklist function that would block user from withdrawing their assets. \"1\" means true; \"0\" means false;  \"-1\" means unknown.  # noqa: E501

        :param blacklist: The blacklist of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :type: int
        """

        self._blacklist = blacklist

    @property
    def contract_name(self):
        """Gets the contract_name of this ResponseWrapperGetDefiInfoResult.  # noqa: E501

        Name of the contract.  # noqa: E501

        :return: The contract_name of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._contract_name

    @contract_name.setter
    def contract_name(self, contract_name):
        """Sets the contract_name of this ResponseWrapperGetDefiInfoResult.

        Name of the contract.  # noqa: E501

        :param contract_name: The contract_name of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :type: str
        """

        self._contract_name = contract_name

    @property
    def selfdestruct(self):
        """Gets the selfdestruct of this ResponseWrapperGetDefiInfoResult.  # noqa: E501

        It describes whether this contract can self destruct. \"1\" means true;  \"0\" means false; “-1” means unknown.  # noqa: E501

        :return: The selfdestruct of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._selfdestruct

    @selfdestruct.setter
    def selfdestruct(self, selfdestruct):
        """Sets the selfdestruct of this ResponseWrapperGetDefiInfoResult.

        It describes whether this contract can self destruct. \"1\" means true;  \"0\" means false; “-1” means unknown.  # noqa: E501

        :param selfdestruct: The selfdestruct of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :type: int
        """

        self._selfdestruct = selfdestruct

    @property
    def is_proxy(self):
        """Gets the is_proxy of this ResponseWrapperGetDefiInfoResult.  # noqa: E501

        It describes whether this contract has a proxy contract.  \"1\" means true;  \"0\" means false; “-1” means unknown.  # noqa: E501

        :return: The is_proxy of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._is_proxy

    @is_proxy.setter
    def is_proxy(self, is_proxy):
        """Sets the is_proxy of this ResponseWrapperGetDefiInfoResult.

        It describes whether this contract has a proxy contract.  \"1\" means true;  \"0\" means false; “-1” means unknown.  # noqa: E501

        :param is_proxy: The is_proxy of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :type: int
        """

        self._is_proxy = is_proxy

    @property
    def approval_abuse(self):
        """Gets the approval_abuse of this ResponseWrapperGetDefiInfoResult.  # noqa: E501

        It describes whether the owner can spend the allowance that obtained by the contract. If so, this function could potentially be abused to steal user assets. \"1\" means true;  \"0\" means false; “-1” means unknown.  # noqa: E501

        :return: The approval_abuse of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._approval_abuse

    @approval_abuse.setter
    def approval_abuse(self, approval_abuse):
        """Sets the approval_abuse of this ResponseWrapperGetDefiInfoResult.

        It describes whether the owner can spend the allowance that obtained by the contract. If so, this function could potentially be abused to steal user assets. \"1\" means true;  \"0\" means false; “-1” means unknown.  # noqa: E501

        :param approval_abuse: The approval_abuse of this ResponseWrapperGetDefiInfoResult.  # noqa: E501
        :type: int
        """

        self._approval_abuse = approval_abuse

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
        if issubclass(ResponseWrapperGetDefiInfoResult, dict):
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
        if not isinstance(other, ResponseWrapperGetDefiInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
