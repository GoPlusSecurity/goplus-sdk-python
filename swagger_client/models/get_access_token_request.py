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

class GetAccessTokenRequest(object):
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
        'app_key': 'str',
        'sign': 'str',
        'time': 'int'
    }

    attribute_map = {
        'app_key': 'app_key',
        'sign': 'sign',
        'time': 'time'
    }

    def __init__(self, app_key=None, sign=None, time=None):  # noqa: E501
        """GetAccessTokenRequest - a model defined in Swagger"""  # noqa: E501
        self._app_key = None
        self._sign = None
        self._time = None
        self.discriminator = None
        self.app_key = app_key
        self.sign = sign
        self.time = time

    @property
    def app_key(self):
        """Gets the app_key of this GetAccessTokenRequest.  # noqa: E501

        app_key  # noqa: E501

        :return: The app_key of this GetAccessTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this GetAccessTokenRequest.

        app_key  # noqa: E501

        :param app_key: The app_key of this GetAccessTokenRequest.  # noqa: E501
        :type: str
        """
        if app_key is None:
            raise ValueError("Invalid value for `app_key`, must not be `None`")  # noqa: E501

        self._app_key = app_key

    @property
    def sign(self):
        """Gets the sign of this GetAccessTokenRequest.  # noqa: E501

        Sign Method Concatenate app_key, time, app_secret in turn, and do sha1() . Example app_key = mBOMg20QW11BbtyH4Zh0 time = 1647847498 app_secret = V6aRfxlPJwN3ViJSIFSCdxPvneajuJsh sign = sha1(mBOMg20QW11BbtyH4Zh01647847498V6aRfxlPJwN3ViJSIFSCdxPvneajuJsh)        = 7293d385b9225b3c3f232b76ba97255d0e21063e  # noqa: E501

        :return: The sign of this GetAccessTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        """Sets the sign of this GetAccessTokenRequest.

        Sign Method Concatenate app_key, time, app_secret in turn, and do sha1() . Example app_key = mBOMg20QW11BbtyH4Zh0 time = 1647847498 app_secret = V6aRfxlPJwN3ViJSIFSCdxPvneajuJsh sign = sha1(mBOMg20QW11BbtyH4Zh01647847498V6aRfxlPJwN3ViJSIFSCdxPvneajuJsh)        = 7293d385b9225b3c3f232b76ba97255d0e21063e  # noqa: E501

        :param sign: The sign of this GetAccessTokenRequest.  # noqa: E501
        :type: str
        """
        if sign is None:
            raise ValueError("Invalid value for `sign`, must not be `None`")  # noqa: E501

        self._sign = sign

    @property
    def time(self):
        """Gets the time of this GetAccessTokenRequest.  # noqa: E501

        Quest timestamp (Second), should be within +-1000s around current timestamp  # noqa: E501

        :return: The time of this GetAccessTokenRequest.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this GetAccessTokenRequest.

        Quest timestamp (Second), should be within +-1000s around current timestamp  # noqa: E501

        :param time: The time of this GetAccessTokenRequest.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if issubclass(GetAccessTokenRequest, dict):
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
        if not isinstance(other, GetAccessTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
