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

class SolanaPrerunTxResponse(object):
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
        'input': 'str',
        'asset_changes': 'SolanaTxAssetChanges',
        'risk_type': 'list[int]',
        'allowance_upgrades': 'list[SolanaAllowanceUpgrade]',
        'ownership_changes': 'list[SolanaOwnershipChange]',
        'sender': 'str',
        'transaction_fee': 'str',
        'risky_txn': 'str',
        'error': 'str',
        'logs': 'list[str]',
        'risk_detail': 'list[str]',
        'slot_height': 'int'
    }

    attribute_map = {
        'input': 'input',
        'asset_changes': 'asset_changes',
        'risk_type': 'risk_type',
        'allowance_upgrades': 'allowance_upgrades',
        'ownership_changes': 'ownership_changes',
        'sender': 'sender',
        'transaction_fee': 'transaction_fee',
        'risky_txn': 'risky_txn',
        'error': 'error',
        'logs': 'logs',
        'risk_detail': 'risk_detail',
        'slot_height': 'slot_height'
    }

    def __init__(self, input=None, asset_changes=None, risk_type=None, allowance_upgrades=None, ownership_changes=None, sender=None, transaction_fee=None, risky_txn=None, error=None, logs=None, risk_detail=None, slot_height=None):  # noqa: E501
        """SolanaPrerunTxResponse - a model defined in Swagger"""  # noqa: E501
        self._input = None
        self._asset_changes = None
        self._risk_type = None
        self._allowance_upgrades = None
        self._ownership_changes = None
        self._sender = None
        self._transaction_fee = None
        self._risky_txn = None
        self._error = None
        self._logs = None
        self._risk_detail = None
        self._slot_height = None
        self.discriminator = None
        if input is not None:
            self.input = input
        if asset_changes is not None:
            self.asset_changes = asset_changes
        if risk_type is not None:
            self.risk_type = risk_type
        if allowance_upgrades is not None:
            self.allowance_upgrades = allowance_upgrades
        if ownership_changes is not None:
            self.ownership_changes = ownership_changes
        if sender is not None:
            self.sender = sender
        if transaction_fee is not None:
            self.transaction_fee = transaction_fee
        if risky_txn is not None:
            self.risky_txn = risky_txn
        if error is not None:
            self.error = error
        if logs is not None:
            self.logs = logs
        if risk_detail is not None:
            self.risk_detail = risk_detail
        if slot_height is not None:
            self.slot_height = slot_height

    @property
    def input(self):
        """Gets the input of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The input of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this SolanaPrerunTxResponse.


        :param input: The input of this SolanaPrerunTxResponse.  # noqa: E501
        :type: str
        """

        self._input = input

    @property
    def asset_changes(self):
        """Gets the asset_changes of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The asset_changes of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: SolanaTxAssetChanges
        """
        return self._asset_changes

    @asset_changes.setter
    def asset_changes(self, asset_changes):
        """Sets the asset_changes of this SolanaPrerunTxResponse.


        :param asset_changes: The asset_changes of this SolanaPrerunTxResponse.  # noqa: E501
        :type: SolanaTxAssetChanges
        """

        self._asset_changes = asset_changes

    @property
    def risk_type(self):
        """Gets the risk_type of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The risk_type of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        """Sets the risk_type of this SolanaPrerunTxResponse.


        :param risk_type: The risk_type of this SolanaPrerunTxResponse.  # noqa: E501
        :type: list[int]
        """

        self._risk_type = risk_type

    @property
    def allowance_upgrades(self):
        """Gets the allowance_upgrades of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The allowance_upgrades of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: list[SolanaAllowanceUpgrade]
        """
        return self._allowance_upgrades

    @allowance_upgrades.setter
    def allowance_upgrades(self, allowance_upgrades):
        """Sets the allowance_upgrades of this SolanaPrerunTxResponse.


        :param allowance_upgrades: The allowance_upgrades of this SolanaPrerunTxResponse.  # noqa: E501
        :type: list[SolanaAllowanceUpgrade]
        """

        self._allowance_upgrades = allowance_upgrades

    @property
    def ownership_changes(self):
        """Gets the ownership_changes of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The ownership_changes of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: list[SolanaOwnershipChange]
        """
        return self._ownership_changes

    @ownership_changes.setter
    def ownership_changes(self, ownership_changes):
        """Sets the ownership_changes of this SolanaPrerunTxResponse.


        :param ownership_changes: The ownership_changes of this SolanaPrerunTxResponse.  # noqa: E501
        :type: list[SolanaOwnershipChange]
        """

        self._ownership_changes = ownership_changes

    @property
    def sender(self):
        """Gets the sender of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The sender of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this SolanaPrerunTxResponse.


        :param sender: The sender of this SolanaPrerunTxResponse.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def transaction_fee(self):
        """Gets the transaction_fee of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The transaction_fee of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: str
        """
        return self._transaction_fee

    @transaction_fee.setter
    def transaction_fee(self, transaction_fee):
        """Sets the transaction_fee of this SolanaPrerunTxResponse.


        :param transaction_fee: The transaction_fee of this SolanaPrerunTxResponse.  # noqa: E501
        :type: str
        """

        self._transaction_fee = transaction_fee

    @property
    def risky_txn(self):
        """Gets the risky_txn of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The risky_txn of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: str
        """
        return self._risky_txn

    @risky_txn.setter
    def risky_txn(self, risky_txn):
        """Sets the risky_txn of this SolanaPrerunTxResponse.


        :param risky_txn: The risky_txn of this SolanaPrerunTxResponse.  # noqa: E501
        :type: str
        """

        self._risky_txn = risky_txn

    @property
    def error(self):
        """Gets the error of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The error of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this SolanaPrerunTxResponse.


        :param error: The error of this SolanaPrerunTxResponse.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def logs(self):
        """Gets the logs of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The logs of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this SolanaPrerunTxResponse.


        :param logs: The logs of this SolanaPrerunTxResponse.  # noqa: E501
        :type: list[str]
        """

        self._logs = logs

    @property
    def risk_detail(self):
        """Gets the risk_detail of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The risk_detail of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._risk_detail

    @risk_detail.setter
    def risk_detail(self, risk_detail):
        """Sets the risk_detail of this SolanaPrerunTxResponse.


        :param risk_detail: The risk_detail of this SolanaPrerunTxResponse.  # noqa: E501
        :type: list[str]
        """

        self._risk_detail = risk_detail

    @property
    def slot_height(self):
        """Gets the slot_height of this SolanaPrerunTxResponse.  # noqa: E501


        :return: The slot_height of this SolanaPrerunTxResponse.  # noqa: E501
        :rtype: int
        """
        return self._slot_height

    @slot_height.setter
    def slot_height(self, slot_height):
        """Sets the slot_height of this SolanaPrerunTxResponse.


        :param slot_height: The slot_height of this SolanaPrerunTxResponse.  # noqa: E501
        :type: int
        """

        self._slot_height = slot_height

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
        if issubclass(SolanaPrerunTxResponse, dict):
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
        if not isinstance(other, SolanaPrerunTxResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
