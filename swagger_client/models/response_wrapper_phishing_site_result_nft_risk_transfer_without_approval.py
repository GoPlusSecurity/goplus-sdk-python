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

class ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval(object):
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
        'owner_address': 'str',
        'value': 'int',
        'owner_type': 'str'
    }

    attribute_map = {
        'owner_address': 'owner_address',
        'value': 'value',
        'owner_type': 'owner_type'
    }

    def __init__(self, owner_address=None, value=None, owner_type=None):  # noqa: E501
        """ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval - a model defined in Swagger"""  # noqa: E501
        self._owner_address = None
        self._value = None
        self._owner_type = None
        self.discriminator = None
        if owner_address is not None:
            self.owner_address = owner_address
        if value is not None:
            self.value = value
        if owner_type is not None:
            self.owner_type = owner_type

    @property
    def owner_address(self):
        """Gets the owner_address of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.  # noqa: E501

        Owner_address describes the owner address.  null: the owner address cannot be fetched.  # noqa: E501

        :return: The owner_address of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.  # noqa: E501
        :rtype: str
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """Sets the owner_address of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.

        Owner_address describes the owner address.  null: the owner address cannot be fetched.  # noqa: E501

        :param owner_address: The owner_address of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.  # noqa: E501
        :type: str
        """

        self._owner_address = owner_address

    @property
    def value(self):
        """Gets the value of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.  # noqa: E501

        The \"value\" describes the status of the risk. null: the contract is not open source or there is a proxy, it is not possible to detect whether the risk exists. -1: the risk is detected but the ownership give up. If the detection of a code vulnerability, it can also be considered risk-free.  0: the risk is not detected.  1: the risk is detected, and the owner address is a common address (EOA), then it can be said that there is a clear risk.  2: The risk is detected, but the owner address is a contract address, the risk is not significant.  3: The risk is detected, but the owner address is not detectable / or an array.   # noqa: E501

        :return: The value of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.

        The \"value\" describes the status of the risk. null: the contract is not open source or there is a proxy, it is not possible to detect whether the risk exists. -1: the risk is detected but the ownership give up. If the detection of a code vulnerability, it can also be considered risk-free.  0: the risk is not detected.  1: the risk is detected, and the owner address is a common address (EOA), then it can be said that there is a clear risk.  2: The risk is detected, but the owner address is a contract address, the risk is not significant.  3: The risk is detected, but the owner address is not detectable / or an array.   # noqa: E501

        :param value: The value of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def owner_type(self):
        """Gets the owner_type of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.  # noqa: E501

        \"blackhole\" : the owner is a blackhole address. \"contract\" : the owner is a contract. \"eoa\" : the owner is a common address (eoa). \"multi-address\":the owner is an array/list. null: the address is not detected.  # noqa: E501

        :return: The owner_type of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.  # noqa: E501
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.

        \"blackhole\" : the owner is a blackhole address. \"contract\" : the owner is a contract. \"eoa\" : the owner is a common address (eoa). \"multi-address\":the owner is an array/list. null: the address is not detected.  # noqa: E501

        :param owner_type: The owner_type of this ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval.  # noqa: E501
        :type: str
        """

        self._owner_type = owner_type

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
        if issubclass(ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval, dict):
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
        if not isinstance(other, ResponseWrapperPhishingSiteResultNftRiskTransferWithoutApproval):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
