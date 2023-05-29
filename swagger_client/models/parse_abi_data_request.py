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

class ParseAbiDataRequest(object):
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
        'chain_id': 'str',
        'contract_address': 'str',
        'data': 'str',
        'input': 'dict(str, object)',
        'signer': 'str',
        'transcation_type': 'str'
    }

    attribute_map = {
        'chain_id': 'chain_id',
        'contract_address': 'contract_address',
        'data': 'data',
        'input': 'input',
        'signer': 'signer',
        'transcation_type': 'transcation_type'
    }

    def __init__(self, chain_id=None, contract_address=None, data=None, input=None, signer=None, transcation_type=None):  # noqa: E501
        """ParseAbiDataRequest - a model defined in Swagger"""  # noqa: E501
        self._chain_id = None
        self._contract_address = None
        self._data = None
        self._input = None
        self._signer = None
        self._transcation_type = None
        self.discriminator = None
        self.chain_id = chain_id
        if contract_address is not None:
            self.contract_address = contract_address
        self.data = data
        if input is not None:
            self.input = input
        if signer is not None:
            self.signer = signer
        if transcation_type is not None:
            self.transcation_type = transcation_type

    @property
    def chain_id(self):
        """Gets the chain_id of this ParseAbiDataRequest.  # noqa: E501

        Chain id, (ETH: 1, Cronos:25, BSC: 56, Heco: 128, Polygon: 137, Fantom:250, KCC: 321, Arbitrum: 42161, Avalanche: 43114)  # noqa: E501

        :return: The chain_id of this ParseAbiDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this ParseAbiDataRequest.

        Chain id, (ETH: 1, Cronos:25, BSC: 56, Heco: 128, Polygon: 137, Fantom:250, KCC: 321, Arbitrum: 42161, Avalanche: 43114)  # noqa: E501

        :param chain_id: The chain_id of this ParseAbiDataRequest.  # noqa: E501
        :type: str
        """
        if chain_id is None:
            raise ValueError("Invalid value for `chain_id`, must not be `None`")  # noqa: E501

        self._chain_id = chain_id

    @property
    def contract_address(self):
        """Gets the contract_address of this ParseAbiDataRequest.  # noqa: E501

        Carrying the signer and contract address will help to decode more information.  # noqa: E501

        :return: The contract_address of this ParseAbiDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._contract_address

    @contract_address.setter
    def contract_address(self, contract_address):
        """Sets the contract_address of this ParseAbiDataRequest.

        Carrying the signer and contract address will help to decode more information.  # noqa: E501

        :param contract_address: The contract_address of this ParseAbiDataRequest.  # noqa: E501
        :type: str
        """

        self._contract_address = contract_address

    @property
    def data(self):
        """Gets the data of this ParseAbiDataRequest.  # noqa: E501

        Transaction input  # noqa: E501

        :return: The data of this ParseAbiDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ParseAbiDataRequest.

        Transaction input  # noqa: E501

        :param data: The data of this ParseAbiDataRequest.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def input(self):
        """Gets the input of this ParseAbiDataRequest.  # noqa: E501

        input info  # noqa: E501

        :return: The input of this ParseAbiDataRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this ParseAbiDataRequest.

        input info  # noqa: E501

        :param input: The input of this ParseAbiDataRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._input = input

    @property
    def signer(self):
        """Gets the signer of this ParseAbiDataRequest.  # noqa: E501

        Carrying the signer and contract address will help to decode more information.  # noqa: E501

        :return: The signer of this ParseAbiDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._signer

    @signer.setter
    def signer(self, signer):
        """Sets the signer of this ParseAbiDataRequest.

        Carrying the signer and contract address will help to decode more information.  # noqa: E501

        :param signer: The signer of this ParseAbiDataRequest.  # noqa: E501
        :type: str
        """

        self._signer = signer

    @property
    def transcation_type(self):
        """Gets the transcation_type of this ParseAbiDataRequest.  # noqa: E501

        Transaction type  # noqa: E501

        :return: The transcation_type of this ParseAbiDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._transcation_type

    @transcation_type.setter
    def transcation_type(self, transcation_type):
        """Sets the transcation_type of this ParseAbiDataRequest.

        Transaction type  # noqa: E501

        :param transcation_type: The transcation_type of this ParseAbiDataRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["common", "eth_signTypedData_v4", "personal_sign", "eth_sign"]  # noqa: E501
        if transcation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transcation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transcation_type, allowed_values)
            )

        self._transcation_type = transcation_type

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
        if issubclass(ParseAbiDataRequest, dict):
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
        if not isinstance(other, ParseAbiDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
