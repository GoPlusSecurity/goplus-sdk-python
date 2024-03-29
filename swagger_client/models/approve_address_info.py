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

class ApproveAddressInfo(object):
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
        'contract_name': 'str',
        'creator_address': 'str',
        'deployed_time': 'int',
        'doubt_list': 'int',
        'is_contract': 'int',
        'is_open_source': 'int',
        'malicious_behavior': 'list[str]',
        'tag': 'str',
        'trust_list': 'int'
    }

    attribute_map = {
        'contract_name': 'contract_name',
        'creator_address': 'creator_address',
        'deployed_time': 'deployed_time',
        'doubt_list': 'doubt_list',
        'is_contract': 'is_contract',
        'is_open_source': 'is_open_source',
        'malicious_behavior': 'malicious_behavior',
        'tag': 'tag',
        'trust_list': 'trust_list'
    }

    def __init__(self, contract_name=None, creator_address=None, deployed_time=None, doubt_list=None, is_contract=None, is_open_source=None, malicious_behavior=None, tag=None, trust_list=None):  # noqa: E501
        """ApproveAddressInfo - a model defined in Swagger"""  # noqa: E501
        self._contract_name = None
        self._creator_address = None
        self._deployed_time = None
        self._doubt_list = None
        self._is_contract = None
        self._is_open_source = None
        self._malicious_behavior = None
        self._tag = None
        self._trust_list = None
        self.discriminator = None
        if contract_name is not None:
            self.contract_name = contract_name
        if creator_address is not None:
            self.creator_address = creator_address
        if deployed_time is not None:
            self.deployed_time = deployed_time
        if doubt_list is not None:
            self.doubt_list = doubt_list
        if is_contract is not None:
            self.is_contract = is_contract
        if is_open_source is not None:
            self.is_open_source = is_open_source
        if malicious_behavior is not None:
            self.malicious_behavior = malicious_behavior
        if tag is not None:
            self.tag = tag
        if trust_list is not None:
            self.trust_list = trust_list

    @property
    def contract_name(self):
        """Gets the contract_name of this ApproveAddressInfo.  # noqa: E501

        Spender name  # noqa: E501

        :return: The contract_name of this ApproveAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._contract_name

    @contract_name.setter
    def contract_name(self, contract_name):
        """Sets the contract_name of this ApproveAddressInfo.

        Spender name  # noqa: E501

        :param contract_name: The contract_name of this ApproveAddressInfo.  # noqa: E501
        :type: str
        """

        self._contract_name = contract_name

    @property
    def creator_address(self):
        """Gets the creator_address of this ApproveAddressInfo.  # noqa: E501

        Spender's deployer  # noqa: E501

        :return: The creator_address of this ApproveAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._creator_address

    @creator_address.setter
    def creator_address(self, creator_address):
        """Sets the creator_address of this ApproveAddressInfo.

        Spender's deployer  # noqa: E501

        :param creator_address: The creator_address of this ApproveAddressInfo.  # noqa: E501
        :type: str
        """

        self._creator_address = creator_address

    @property
    def deployed_time(self):
        """Gets the deployed_time of this ApproveAddressInfo.  # noqa: E501

        Spender's deployed time  # noqa: E501

        :return: The deployed_time of this ApproveAddressInfo.  # noqa: E501
        :rtype: int
        """
        return self._deployed_time

    @deployed_time.setter
    def deployed_time(self, deployed_time):
        """Sets the deployed_time of this ApproveAddressInfo.

        Spender's deployed time  # noqa: E501

        :param deployed_time: The deployed_time of this ApproveAddressInfo.  # noqa: E501
        :type: int
        """

        self._deployed_time = deployed_time

    @property
    def doubt_list(self):
        """Gets the doubt_list of this ApproveAddressInfo.  # noqa: E501

        Whether the spender has a history of malicious behavior or contains high risk.  # noqa: E501

        :return: The doubt_list of this ApproveAddressInfo.  # noqa: E501
        :rtype: int
        """
        return self._doubt_list

    @doubt_list.setter
    def doubt_list(self, doubt_list):
        """Sets the doubt_list of this ApproveAddressInfo.

        Whether the spender has a history of malicious behavior or contains high risk.  # noqa: E501

        :param doubt_list: The doubt_list of this ApproveAddressInfo.  # noqa: E501
        :type: int
        """

        self._doubt_list = doubt_list

    @property
    def is_contract(self):
        """Gets the is_contract of this ApproveAddressInfo.  # noqa: E501

        Whether the spender is a contract.  # noqa: E501

        :return: The is_contract of this ApproveAddressInfo.  # noqa: E501
        :rtype: int
        """
        return self._is_contract

    @is_contract.setter
    def is_contract(self, is_contract):
        """Sets the is_contract of this ApproveAddressInfo.

        Whether the spender is a contract.  # noqa: E501

        :param is_contract: The is_contract of this ApproveAddressInfo.  # noqa: E501
        :type: int
        """

        self._is_contract = is_contract

    @property
    def is_open_source(self):
        """Gets the is_open_source of this ApproveAddressInfo.  # noqa: E501

        Whether the spender is verified on blockchain explorer.  # noqa: E501

        :return: The is_open_source of this ApproveAddressInfo.  # noqa: E501
        :rtype: int
        """
        return self._is_open_source

    @is_open_source.setter
    def is_open_source(self, is_open_source):
        """Sets the is_open_source of this ApproveAddressInfo.

        Whether the spender is verified on blockchain explorer.  # noqa: E501

        :param is_open_source: The is_open_source of this ApproveAddressInfo.  # noqa: E501
        :type: int
        """

        self._is_open_source = is_open_source

    @property
    def malicious_behavior(self):
        """Gets the malicious_behavior of this ApproveAddressInfo.  # noqa: E501

        Specific malicious behaviors or risks of this spender.  # noqa: E501

        :return: The malicious_behavior of this ApproveAddressInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._malicious_behavior

    @malicious_behavior.setter
    def malicious_behavior(self, malicious_behavior):
        """Sets the malicious_behavior of this ApproveAddressInfo.

        Specific malicious behaviors or risks of this spender.  # noqa: E501

        :param malicious_behavior: The malicious_behavior of this ApproveAddressInfo.  # noqa: E501
        :type: list[str]
        """

        self._malicious_behavior = malicious_behavior

    @property
    def tag(self):
        """Gets the tag of this ApproveAddressInfo.  # noqa: E501

        Spender tag  # noqa: E501

        :return: The tag of this ApproveAddressInfo.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ApproveAddressInfo.

        Spender tag  # noqa: E501

        :param tag: The tag of this ApproveAddressInfo.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def trust_list(self):
        """Gets the trust_list of this ApproveAddressInfo.  # noqa: E501

        Whether the spender is on the whitelist, and can be trusted  # noqa: E501

        :return: The trust_list of this ApproveAddressInfo.  # noqa: E501
        :rtype: int
        """
        return self._trust_list

    @trust_list.setter
    def trust_list(self, trust_list):
        """Sets the trust_list of this ApproveAddressInfo.

        Whether the spender is on the whitelist, and can be trusted  # noqa: E501

        :param trust_list: The trust_list of this ApproveAddressInfo.  # noqa: E501
        :type: int
        """

        self._trust_list = trust_list

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
        if issubclass(ApproveAddressInfo, dict):
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
        if not isinstance(other, ApproveAddressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
