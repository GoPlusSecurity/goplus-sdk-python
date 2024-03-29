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

class ParseAbiDataResponse(object):
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
        'contract_description': 'str',
        'contract_name': 'str',
        'malicious_contract': 'int',
        'method': 'str',
        'params': 'list[AbiParamInfo]',
        'risk': 'str',
        'risky_signature': 'int',
        'signature_detail': 'str'
    }

    attribute_map = {
        'contract_description': 'contract_description',
        'contract_name': 'contract_name',
        'malicious_contract': 'malicious_contract',
        'method': 'method',
        'params': 'params',
        'risk': 'risk',
        'risky_signature': 'risky_signature',
        'signature_detail': 'signature_detail'
    }

    def __init__(self, contract_description=None, contract_name=None, malicious_contract=None, method=None, params=None, risk=None, risky_signature=None, signature_detail=None):  # noqa: E501
        """ParseAbiDataResponse - a model defined in Swagger"""  # noqa: E501
        self._contract_description = None
        self._contract_name = None
        self._malicious_contract = None
        self._method = None
        self._params = None
        self._risk = None
        self._risky_signature = None
        self._signature_detail = None
        self.discriminator = None
        if contract_description is not None:
            self.contract_description = contract_description
        if contract_name is not None:
            self.contract_name = contract_name
        if malicious_contract is not None:
            self.malicious_contract = malicious_contract
        if method is not None:
            self.method = method
        if params is not None:
            self.params = params
        if risk is not None:
            self.risk = risk
        if risky_signature is not None:
            self.risky_signature = risky_signature
        if signature_detail is not None:
            self.signature_detail = signature_detail

    @property
    def contract_description(self):
        """Gets the contract_description of this ParseAbiDataResponse.  # noqa: E501

        Description of the contract.  # noqa: E501

        :return: The contract_description of this ParseAbiDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._contract_description

    @contract_description.setter
    def contract_description(self, contract_description):
        """Sets the contract_description of this ParseAbiDataResponse.

        Description of the contract.  # noqa: E501

        :param contract_description: The contract_description of this ParseAbiDataResponse.  # noqa: E501
        :type: str
        """

        self._contract_description = contract_description

    @property
    def contract_name(self):
        """Gets the contract_name of this ParseAbiDataResponse.  # noqa: E501

        The name of the contract that the user is interacting with.  # noqa: E501

        :return: The contract_name of this ParseAbiDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._contract_name

    @contract_name.setter
    def contract_name(self, contract_name):
        """Sets the contract_name of this ParseAbiDataResponse.

        The name of the contract that the user is interacting with.  # noqa: E501

        :param contract_name: The contract_name of this ParseAbiDataResponse.  # noqa: E501
        :type: str
        """

        self._contract_name = contract_name

    @property
    def malicious_contract(self):
        """Gets the malicious_contract of this ParseAbiDataResponse.  # noqa: E501

        It tells if contract that the user is interacting with is malicious contract.  # noqa: E501

        :return: The malicious_contract of this ParseAbiDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._malicious_contract

    @malicious_contract.setter
    def malicious_contract(self, malicious_contract):
        """Sets the malicious_contract of this ParseAbiDataResponse.

        It tells if contract that the user is interacting with is malicious contract.  # noqa: E501

        :param malicious_contract: The malicious_contract of this ParseAbiDataResponse.  # noqa: E501
        :type: int
        """

        self._malicious_contract = malicious_contract

    @property
    def method(self):
        """Gets the method of this ParseAbiDataResponse.  # noqa: E501

        It describes the method name in ABI, for example \"transfer\".  # noqa: E501

        :return: The method of this ParseAbiDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ParseAbiDataResponse.

        It describes the method name in ABI, for example \"transfer\".  # noqa: E501

        :param method: The method of this ParseAbiDataResponse.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def params(self):
        """Gets the params of this ParseAbiDataResponse.  # noqa: E501

        It describes the parameter info  # noqa: E501

        :return: The params of this ParseAbiDataResponse.  # noqa: E501
        :rtype: list[AbiParamInfo]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ParseAbiDataResponse.

        It describes the parameter info  # noqa: E501

        :param params: The params of this ParseAbiDataResponse.  # noqa: E501
        :type: list[AbiParamInfo]
        """

        self._params = params

    @property
    def risk(self):
        """Gets the risk of this ParseAbiDataResponse.  # noqa: E501

        It explains why the transaction that users are signing contains risk.(Notice:Even non-malicious, commonly used, well-known contracts can be highly risky if not used properly.)  # noqa: E501

        :return: The risk of this ParseAbiDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """Sets the risk of this ParseAbiDataResponse.

        It explains why the transaction that users are signing contains risk.(Notice:Even non-malicious, commonly used, well-known contracts can be highly risky if not used properly.)  # noqa: E501

        :param risk: The risk of this ParseAbiDataResponse.  # noqa: E501
        :type: str
        """

        self._risk = risk

    @property
    def risky_signature(self):
        """Gets the risky_signature of this ParseAbiDataResponse.  # noqa: E501

        It tells if the transaction that users are signing contains risk.(Notice:Even non-malicious, commonly used, well-known contracts can be highly risky if not used properly.)  # noqa: E501

        :return: The risky_signature of this ParseAbiDataResponse.  # noqa: E501
        :rtype: int
        """
        return self._risky_signature

    @risky_signature.setter
    def risky_signature(self, risky_signature):
        """Sets the risky_signature of this ParseAbiDataResponse.

        It tells if the transaction that users are signing contains risk.(Notice:Even non-malicious, commonly used, well-known contracts can be highly risky if not used properly.)  # noqa: E501

        :param risky_signature: The risky_signature of this ParseAbiDataResponse.  # noqa: E501
        :type: int
        """

        self._risky_signature = risky_signature

    @property
    def signature_detail(self):
        """Gets the signature_detail of this ParseAbiDataResponse.  # noqa: E501

        It explain the function of the method  # noqa: E501

        :return: The signature_detail of this ParseAbiDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._signature_detail

    @signature_detail.setter
    def signature_detail(self, signature_detail):
        """Sets the signature_detail of this ParseAbiDataResponse.

        It explain the function of the method  # noqa: E501

        :param signature_detail: The signature_detail of this ParseAbiDataResponse.  # noqa: E501
        :type: str
        """

        self._signature_detail = signature_detail

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
        if issubclass(ParseAbiDataResponse, dict):
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
        if not isinstance(other, ParseAbiDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
