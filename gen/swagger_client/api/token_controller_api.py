# coding: utf-8

"""
    GoPlus Security API Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TokenControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_access_token_using_post(self, app_key, sign, time, **kwargs):  # noqa: E501
        """get token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_token_using_post(app_key, sign, time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_key: app_key (required)
        :param str sign: Concatenate app_key, time, app_secret in turn, and do sha1().app_key = mBOMg20QW11BbtyH4Zh0 \\n\" +             \"time = 1647847498 \\n\" +             \"app_secret = V6aRfxlPJwN3ViJSIFSCdxPvneajuJsh \\n\" +             \"sign = sha1(mBOMg20QW11BbtyH4Zh01647847498V6aRfxlPJwN3ViJSIFSCdxPvneajuJsh)\\n\" +             \"        = 7293d385b9225b3c3f232b76ba97255d0e21063e (required)
        :param int time: Quest timestamp (Second) (required)
        :return: ResponseWrapperGetAccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_access_token_using_post_with_http_info(app_key, sign, time, **kwargs)  # noqa: E501
        else:
            (data) = self.get_access_token_using_post_with_http_info(app_key, sign, time, **kwargs)  # noqa: E501
            return data

    def get_access_token_using_post_with_http_info(self, app_key, sign, time, **kwargs):  # noqa: E501
        """get token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_access_token_using_post_with_http_info(app_key, sign, time, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_key: app_key (required)
        :param str sign: Concatenate app_key, time, app_secret in turn, and do sha1().app_key = mBOMg20QW11BbtyH4Zh0 \\n\" +             \"time = 1647847498 \\n\" +             \"app_secret = V6aRfxlPJwN3ViJSIFSCdxPvneajuJsh \\n\" +             \"sign = sha1(mBOMg20QW11BbtyH4Zh01647847498V6aRfxlPJwN3ViJSIFSCdxPvneajuJsh)\\n\" +             \"        = 7293d385b9225b3c3f232b76ba97255d0e21063e (required)
        :param int time: Quest timestamp (Second) (required)
        :return: ResponseWrapperGetAccessTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_key', 'sign', 'time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_token_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_key' is set
        if ('app_key' not in params or
                params['app_key'] is None):
            raise ValueError("Missing the required parameter `app_key` when calling `get_access_token_using_post`")  # noqa: E501
        # verify the required parameter 'sign' is set
        if ('sign' not in params or
                params['sign'] is None):
            raise ValueError("Missing the required parameter `sign` when calling `get_access_token_using_post`")  # noqa: E501
        # verify the required parameter 'time' is set
        if ('time' not in params or
                params['time'] is None):
            raise ValueError("Missing the required parameter `time` when calling `get_access_token_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'app_key' in params:
            query_params.append(('appKey', params['app_key']))  # noqa: E501
        if 'sign' in params:
            query_params.append(('sign', params['sign']))  # noqa: E501
        if 'time' in params:
            query_params.append(('time', params['time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseWrapperGetAccessTokenResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
