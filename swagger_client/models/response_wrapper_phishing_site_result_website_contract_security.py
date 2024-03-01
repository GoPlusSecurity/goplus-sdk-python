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

class ResponseWrapperPhishingSiteResultWebsiteContractSecurity(object):
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
        'standard': 'str',
        'is_contract': 'int',
        'address_risk': 'list[str]',
        'contract': 'str',
        'is_open_source': 'int',
        'nft_risk': 'ResponseWrapperPhishingSiteResultNftRisk'
    }

    attribute_map = {
        'standard': 'standard',
        'is_contract': 'is_contract',
        'address_risk': 'address_risk',
        'contract': 'contract',
        'is_open_source': 'is_open_source',
        'nft_risk': 'nft_risk'
    }

    def __init__(self, standard=None, is_contract=None, address_risk=None, contract=None, is_open_source=None, nft_risk=None):  # noqa: E501
        """ResponseWrapperPhishingSiteResultWebsiteContractSecurity - a model defined in Swagger"""  # noqa: E501
        self._standard = None
        self._is_contract = None
        self._address_risk = None
        self._contract = None
        self._is_open_source = None
        self._nft_risk = None
        self.discriminator = None
        if standard is not None:
            self.standard = standard
        if is_contract is not None:
            self.is_contract = is_contract
        if address_risk is not None:
            self.address_risk = address_risk
        if contract is not None:
            self.contract = contract
        if is_open_source is not None:
            self.is_open_source = is_open_source
        if nft_risk is not None:
            self.nft_risk = nft_risk

    @property
    def standard(self):
        """Gets the standard of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501

        contract type(erc20, erc721, erc1155)  # noqa: E501

        :return: The standard of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        """Sets the standard of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.

        contract type(erc20, erc721, erc1155)  # noqa: E501

        :param standard: The standard of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :type: str
        """

        self._standard = standard

    @property
    def is_contract(self):
        """Gets the is_contract of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501

        It describes whether the holder is a contract \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The is_contract of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :rtype: int
        """
        return self._is_contract

    @is_contract.setter
    def is_contract(self, is_contract):
        """Sets the is_contract of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.

        It describes whether the holder is a contract \"1\" means true; \"0\" means false.  # noqa: E501

        :param is_contract: The is_contract of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :type: int
        """

        self._is_contract = is_contract

    @property
    def address_risk(self):
        """Gets the address_risk of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501

        address risk  # noqa: E501

        :return: The address_risk of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_risk

    @address_risk.setter
    def address_risk(self, address_risk):
        """Sets the address_risk of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.

        address risk  # noqa: E501

        :param address_risk: The address_risk of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :type: list[str]
        """

        self._address_risk = address_risk

    @property
    def contract(self):
        """Gets the contract of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501

        contract address  # noqa: E501

        :return: The contract of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.

        contract address  # noqa: E501

        :param contract: The contract of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def is_open_source(self):
        """Gets the is_open_source of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501

        It describes whether this contract is open source.  \"1\" means true;  \"0\" means false.(Notice:Un-open-sourced contracts may hide various unknown mechanisms and are extremely risky. When the contract is not open source, we will not be able to detect other risk items.)  # noqa: E501

        :return: The is_open_source of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :rtype: int
        """
        return self._is_open_source

    @is_open_source.setter
    def is_open_source(self, is_open_source):
        """Sets the is_open_source of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.

        It describes whether this contract is open source.  \"1\" means true;  \"0\" means false.(Notice:Un-open-sourced contracts may hide various unknown mechanisms and are extremely risky. When the contract is not open source, we will not be able to detect other risk items.)  # noqa: E501

        :param is_open_source: The is_open_source of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :type: int
        """

        self._is_open_source = is_open_source

    @property
    def nft_risk(self):
        """Gets the nft_risk of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501


        :return: The nft_risk of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :rtype: ResponseWrapperPhishingSiteResultNftRisk
        """
        return self._nft_risk

    @nft_risk.setter
    def nft_risk(self, nft_risk):
        """Sets the nft_risk of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.


        :param nft_risk: The nft_risk of this ResponseWrapperPhishingSiteResultWebsiteContractSecurity.  # noqa: E501
        :type: ResponseWrapperPhishingSiteResultNftRisk
        """

        self._nft_risk = nft_risk

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
        if issubclass(ResponseWrapperPhishingSiteResultWebsiteContractSecurity, dict):
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
        if not isinstance(other, ResponseWrapperPhishingSiteResultWebsiteContractSecurity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
