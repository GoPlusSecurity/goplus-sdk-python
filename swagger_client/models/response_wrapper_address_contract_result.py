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

class ResponseWrapperAddressContractResult(object):
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
        'cybercrime': 'str',
        'money_laundering': 'str',
        'number_of_malicious_contracts_created': 'str',
        'gas_abuse': 'str',
        'financial_crime': 'str',
        'darkweb_transactions': 'str',
        'reinit': 'str',
        'phishing_activities': 'str',
        'contract_address': 'str',
        'fake_kyc': 'str',
        'blacklist_doubt': 'str',
        'data_source': 'str',
        'fake_standard_interface': 'str',
        'stealing_attack': 'str',
        'blackmail_activities': 'str',
        'sanctioned': 'str',
        'malicious_mining_activities': 'str',
        'mixer': 'str',
        'fake_token': 'str',
        'honeypot_related_address': 'str'
    }

    attribute_map = {
        'cybercrime': 'cybercrime',
        'money_laundering': 'money_laundering',
        'number_of_malicious_contracts_created': 'number_of_malicious_contracts_created',
        'gas_abuse': 'gas_abuse',
        'financial_crime': 'financial_crime',
        'darkweb_transactions': 'darkweb_transactions',
        'reinit': 'reinit',
        'phishing_activities': 'phishing_activities',
        'contract_address': 'contract_address',
        'fake_kyc': 'fake_kyc',
        'blacklist_doubt': 'blacklist_doubt',
        'data_source': 'data_source',
        'fake_standard_interface': 'fake_standard_interface',
        'stealing_attack': 'stealing_attack',
        'blackmail_activities': 'blackmail_activities',
        'sanctioned': 'sanctioned',
        'malicious_mining_activities': 'malicious_mining_activities',
        'mixer': 'mixer',
        'fake_token': 'fake_token',
        'honeypot_related_address': 'honeypot_related_address'
    }

    def __init__(self, cybercrime=None, money_laundering=None, number_of_malicious_contracts_created=None, gas_abuse=None, financial_crime=None, darkweb_transactions=None, reinit=None, phishing_activities=None, contract_address=None, fake_kyc=None, blacklist_doubt=None, data_source=None, fake_standard_interface=None, stealing_attack=None, blackmail_activities=None, sanctioned=None, malicious_mining_activities=None, mixer=None, fake_token=None, honeypot_related_address=None):  # noqa: E501
        """ResponseWrapperAddressContractResult - a model defined in Swagger"""  # noqa: E501
        self._cybercrime = None
        self._money_laundering = None
        self._number_of_malicious_contracts_created = None
        self._gas_abuse = None
        self._financial_crime = None
        self._darkweb_transactions = None
        self._reinit = None
        self._phishing_activities = None
        self._contract_address = None
        self._fake_kyc = None
        self._blacklist_doubt = None
        self._data_source = None
        self._fake_standard_interface = None
        self._stealing_attack = None
        self._blackmail_activities = None
        self._sanctioned = None
        self._malicious_mining_activities = None
        self._mixer = None
        self._fake_token = None
        self._honeypot_related_address = None
        self.discriminator = None
        if cybercrime is not None:
            self.cybercrime = cybercrime
        if money_laundering is not None:
            self.money_laundering = money_laundering
        if number_of_malicious_contracts_created is not None:
            self.number_of_malicious_contracts_created = number_of_malicious_contracts_created
        if gas_abuse is not None:
            self.gas_abuse = gas_abuse
        if financial_crime is not None:
            self.financial_crime = financial_crime
        if darkweb_transactions is not None:
            self.darkweb_transactions = darkweb_transactions
        if reinit is not None:
            self.reinit = reinit
        if phishing_activities is not None:
            self.phishing_activities = phishing_activities
        if contract_address is not None:
            self.contract_address = contract_address
        if fake_kyc is not None:
            self.fake_kyc = fake_kyc
        if blacklist_doubt is not None:
            self.blacklist_doubt = blacklist_doubt
        if data_source is not None:
            self.data_source = data_source
        if fake_standard_interface is not None:
            self.fake_standard_interface = fake_standard_interface
        if stealing_attack is not None:
            self.stealing_attack = stealing_attack
        if blackmail_activities is not None:
            self.blackmail_activities = blackmail_activities
        if sanctioned is not None:
            self.sanctioned = sanctioned
        if malicious_mining_activities is not None:
            self.malicious_mining_activities = malicious_mining_activities
        if mixer is not None:
            self.mixer = mixer
        if fake_token is not None:
            self.fake_token = fake_token
        if honeypot_related_address is not None:
            self.honeypot_related_address = honeypot_related_address

    @property
    def cybercrime(self):
        """Gets the cybercrime of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is involved in cybercrime. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The cybercrime of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._cybercrime

    @cybercrime.setter
    def cybercrime(self, cybercrime):
        """Sets the cybercrime of this ResponseWrapperAddressContractResult.

        It describes whether this address is involved in cybercrime. \"1\" means true; \"0\" means false.  # noqa: E501

        :param cybercrime: The cybercrime of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._cybercrime = cybercrime

    @property
    def money_laundering(self):
        """Gets the money_laundering of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is involved in money laundering. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The money_laundering of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._money_laundering

    @money_laundering.setter
    def money_laundering(self, money_laundering):
        """Sets the money_laundering of this ResponseWrapperAddressContractResult.

        It describes whether this address is involved in money laundering. \"1\" means true; \"0\" means false.  # noqa: E501

        :param money_laundering: The money_laundering of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._money_laundering = money_laundering

    @property
    def number_of_malicious_contracts_created(self):
        """Gets the number_of_malicious_contracts_created of this ResponseWrapperAddressContractResult.  # noqa: E501

        This parameter describes how many malicious contracts have been created by this address.  # noqa: E501

        :return: The number_of_malicious_contracts_created of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._number_of_malicious_contracts_created

    @number_of_malicious_contracts_created.setter
    def number_of_malicious_contracts_created(self, number_of_malicious_contracts_created):
        """Sets the number_of_malicious_contracts_created of this ResponseWrapperAddressContractResult.

        This parameter describes how many malicious contracts have been created by this address.  # noqa: E501

        :param number_of_malicious_contracts_created: The number_of_malicious_contracts_created of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._number_of_malicious_contracts_created = number_of_malicious_contracts_created

    @property
    def gas_abuse(self):
        """Gets the gas_abuse of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is cheating other user's gas fee to mint other assets.(Notice:Any interaction with such addresses may result in loss of property.)  # noqa: E501

        :return: The gas_abuse of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._gas_abuse

    @gas_abuse.setter
    def gas_abuse(self, gas_abuse):
        """Sets the gas_abuse of this ResponseWrapperAddressContractResult.

        It describes whether this address is cheating other user's gas fee to mint other assets.(Notice:Any interaction with such addresses may result in loss of property.)  # noqa: E501

        :param gas_abuse: The gas_abuse of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._gas_abuse = gas_abuse

    @property
    def financial_crime(self):
        """Gets the financial_crime of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is involved in financial crime. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The financial_crime of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._financial_crime

    @financial_crime.setter
    def financial_crime(self, financial_crime):
        """Sets the financial_crime of this ResponseWrapperAddressContractResult.

        It describes whether this address is involved in financial crime. \"1\" means true; \"0\" means false.  # noqa: E501

        :param financial_crime: The financial_crime of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._financial_crime = financial_crime

    @property
    def darkweb_transactions(self):
        """Gets the darkweb_transactions of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is involved in darkweb transactions. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The darkweb_transactions of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._darkweb_transactions

    @darkweb_transactions.setter
    def darkweb_transactions(self, darkweb_transactions):
        """Sets the darkweb_transactions of this ResponseWrapperAddressContractResult.

        It describes whether this address is involved in darkweb transactions. \"1\" means true; \"0\" means false.  # noqa: E501

        :param darkweb_transactions: The darkweb_transactions of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._darkweb_transactions = darkweb_transactions

    @property
    def reinit(self):
        """Gets the reinit of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address/contract has been deployed more than onces, and can be deployed again.(Notice:If a contract can be reinited, the developer can change the contract code whenever he wants.)  # noqa: E501

        :return: The reinit of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._reinit

    @reinit.setter
    def reinit(self, reinit):
        """Sets the reinit of this ResponseWrapperAddressContractResult.

        It describes whether this address/contract has been deployed more than onces, and can be deployed again.(Notice:If a contract can be reinited, the developer can change the contract code whenever he wants.)  # noqa: E501

        :param reinit: The reinit of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._reinit = reinit

    @property
    def phishing_activities(self):
        """Gets the phishing_activities of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address has implemented phishing activities. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The phishing_activities of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._phishing_activities

    @phishing_activities.setter
    def phishing_activities(self, phishing_activities):
        """Sets the phishing_activities of this ResponseWrapperAddressContractResult.

        It describes whether this address has implemented phishing activities. \"1\" means true; \"0\" means false.  # noqa: E501

        :param phishing_activities: The phishing_activities of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._phishing_activities = phishing_activities

    @property
    def contract_address(self):
        """Gets the contract_address of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is a contract address. \"1\" means true; \"0\" means false.(Notice:If only the address is sent to the API and not the chain id, the \"contract_address\" will not be returned (This is because there are cases where the same address is a contract in one public chain but not in other public chains.) Determining the contract address is achieved by calling a third-party blockchain browser interface. Since it takes time for the browser interface to return, the field may be empty on the first request. Solution: the second call around 5s can return whether the address is the value of the contract normally.)  # noqa: E501

        :return: The contract_address of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._contract_address

    @contract_address.setter
    def contract_address(self, contract_address):
        """Sets the contract_address of this ResponseWrapperAddressContractResult.

        It describes whether this address is a contract address. \"1\" means true; \"0\" means false.(Notice:If only the address is sent to the API and not the chain id, the \"contract_address\" will not be returned (This is because there are cases where the same address is a contract in one public chain but not in other public chains.) Determining the contract address is achieved by calling a third-party blockchain browser interface. Since it takes time for the browser interface to return, the field may be empty on the first request. Solution: the second call around 5s can return whether the address is the value of the contract normally.)  # noqa: E501

        :param contract_address: The contract_address of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._contract_address = contract_address

    @property
    def fake_kyc(self):
        """Gets the fake_kyc of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is involved in fake KYC. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The fake_kyc of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._fake_kyc

    @fake_kyc.setter
    def fake_kyc(self, fake_kyc):
        """Sets the fake_kyc of this ResponseWrapperAddressContractResult.

        It describes whether this address is involved in fake KYC. \"1\" means true; \"0\" means false.  # noqa: E501

        :param fake_kyc: The fake_kyc of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._fake_kyc = fake_kyc

    @property
    def blacklist_doubt(self):
        """Gets the blacklist_doubt of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is suspected of malicious behavior. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The blacklist_doubt of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._blacklist_doubt

    @blacklist_doubt.setter
    def blacklist_doubt(self, blacklist_doubt):
        """Sets the blacklist_doubt of this ResponseWrapperAddressContractResult.

        It describes whether this address is suspected of malicious behavior. \"1\" means true; \"0\" means false.  # noqa: E501

        :param blacklist_doubt: The blacklist_doubt of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._blacklist_doubt = blacklist_doubt

    @property
    def data_source(self):
        """Gets the data_source of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes the data source for this address information. For example: GoPlus/SlowMist  # noqa: E501

        :return: The data_source of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this ResponseWrapperAddressContractResult.

        It describes the data source for this address information. For example: GoPlus/SlowMist  # noqa: E501

        :param data_source: The data_source of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._data_source = data_source

    @property
    def fake_standard_interface(self):
        """Gets the fake_standard_interface of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this contract contains standard interfaces that do not conform the requirements of the standard protocol.(Notice:Fake Standard Interface is mostly seen in scam assets.)  # noqa: E501

        :return: The fake_standard_interface of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._fake_standard_interface

    @fake_standard_interface.setter
    def fake_standard_interface(self, fake_standard_interface):
        """Sets the fake_standard_interface of this ResponseWrapperAddressContractResult.

        It describes whether this contract contains standard interfaces that do not conform the requirements of the standard protocol.(Notice:Fake Standard Interface is mostly seen in scam assets.)  # noqa: E501

        :param fake_standard_interface: The fake_standard_interface of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._fake_standard_interface = fake_standard_interface

    @property
    def stealing_attack(self):
        """Gets the stealing_attack of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address has implemented stealing attacks. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The stealing_attack of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._stealing_attack

    @stealing_attack.setter
    def stealing_attack(self, stealing_attack):
        """Sets the stealing_attack of this ResponseWrapperAddressContractResult.

        It describes whether this address has implemented stealing attacks. \"1\" means true; \"0\" means false.  # noqa: E501

        :param stealing_attack: The stealing_attack of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._stealing_attack = stealing_attack

    @property
    def blackmail_activities(self):
        """Gets the blackmail_activities of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address has implemented blackmail activities. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The blackmail_activities of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._blackmail_activities

    @blackmail_activities.setter
    def blackmail_activities(self, blackmail_activities):
        """Sets the blackmail_activities of this ResponseWrapperAddressContractResult.

        It describes whether this address has implemented blackmail activities. \"1\" means true; \"0\" means false.  # noqa: E501

        :param blackmail_activities: The blackmail_activities of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._blackmail_activities = blackmail_activities

    @property
    def sanctioned(self):
        """Gets the sanctioned of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is coin sanctioned address. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The sanctioned of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._sanctioned

    @sanctioned.setter
    def sanctioned(self, sanctioned):
        """Sets the sanctioned of this ResponseWrapperAddressContractResult.

        It describes whether this address is coin sanctioned address. \"1\" means true; \"0\" means false.  # noqa: E501

        :param sanctioned: The sanctioned of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._sanctioned = sanctioned

    @property
    def malicious_mining_activities(self):
        """Gets the malicious_mining_activities of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is involved in malicious mining activities. \"1\" means true; \"0\" means false.  # noqa: E501

        :return: The malicious_mining_activities of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._malicious_mining_activities

    @malicious_mining_activities.setter
    def malicious_mining_activities(self, malicious_mining_activities):
        """Sets the malicious_mining_activities of this ResponseWrapperAddressContractResult.

        It describes whether this address is involved in malicious mining activities. \"1\" means true; \"0\" means false.  # noqa: E501

        :param malicious_mining_activities: The malicious_mining_activities of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._malicious_mining_activities = malicious_mining_activities

    @property
    def mixer(self):
        """Gets the mixer of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is coin mixer address. \"1\" means true; \"0\" means false.(Notice:Interacting with coin mixer may result in your address being added to the risk list of third-party institutions.)  # noqa: E501

        :return: The mixer of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._mixer

    @mixer.setter
    def mixer(self, mixer):
        """Sets the mixer of this ResponseWrapperAddressContractResult.

        It describes whether this address is coin mixer address. \"1\" means true; \"0\" means false.(Notice:Interacting with coin mixer may result in your address being added to the risk list of third-party institutions.)  # noqa: E501

        :param mixer: The mixer of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._mixer = mixer

    @property
    def fake_token(self):
        """Gets the fake_token of this ResponseWrapperAddressContractResult.  # noqa: E501

        It indicates whether the token is a counterfeit of a mainstream asset.  # noqa: E501

        :return: The fake_token of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._fake_token

    @fake_token.setter
    def fake_token(self, fake_token):
        """Sets the fake_token of this ResponseWrapperAddressContractResult.

        It indicates whether the token is a counterfeit of a mainstream asset.  # noqa: E501

        :param fake_token: The fake_token of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._fake_token = fake_token

    @property
    def honeypot_related_address(self):
        """Gets the honeypot_related_address of this ResponseWrapperAddressContractResult.  # noqa: E501

        It describes whether this address is related to honeypot tokens or has created scam tokens. \"1\" means true; \"0\" means false.(Notice:Addresses related to honeypot mean the creators or owners of the honeypot tokens. This is a dangerous address if the address is ralated to honeypot tokens.)  # noqa: E501

        :return: The honeypot_related_address of this ResponseWrapperAddressContractResult.  # noqa: E501
        :rtype: str
        """
        return self._honeypot_related_address

    @honeypot_related_address.setter
    def honeypot_related_address(self, honeypot_related_address):
        """Sets the honeypot_related_address of this ResponseWrapperAddressContractResult.

        It describes whether this address is related to honeypot tokens or has created scam tokens. \"1\" means true; \"0\" means false.(Notice:Addresses related to honeypot mean the creators or owners of the honeypot tokens. This is a dangerous address if the address is ralated to honeypot tokens.)  # noqa: E501

        :param honeypot_related_address: The honeypot_related_address of this ResponseWrapperAddressContractResult.  # noqa: E501
        :type: str
        """

        self._honeypot_related_address = honeypot_related_address

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
        if issubclass(ResponseWrapperAddressContractResult, dict):
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
        if not isinstance(other, ResponseWrapperAddressContractResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
