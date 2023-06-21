# coding: utf-8

"""
    GoPlus Security API Document

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefiControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_defi_info_using_get(self, contract_addresses, chain_id, **kwargs):  # noqa: E501
        """Rug-pull Detection API Beta  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_defi_info_using_get(contract_addresses, chain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str contract_addresses: Defi protocol address (required)
        :param str chain_id: Chain id, (eth: 1, bsc: 56) (required)
        :param str authorization: Authorization (test：Bearer 81|9ihH8JzEuFu4MQ9DjWmH5WrNCPW...)
        :return: GetDefiInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_defi_info_using_get_with_http_info(contract_addresses, chain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_defi_info_using_get_with_http_info(contract_addresses, chain_id, **kwargs)  # noqa: E501
            return data

    def get_defi_info_using_get_with_http_info(self, contract_addresses, chain_id, **kwargs):  # noqa: E501
        """Rug-pull Detection API Beta  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_defi_info_using_get_with_http_info(contract_addresses, chain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str contract_addresses: Defi protocol address (required)
        :param str chain_id: Chain id, (eth: 1, bsc: 56) (required)
        :param str authorization: Authorization (test：Bearer 81|9ihH8JzEuFu4MQ9DjWmH5WrNCPW...)
        :return: GetDefiInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contract_addresses', 'chain_id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_defi_info_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contract_addresses' is set
        if ('contract_addresses' not in params or
                params['contract_addresses'] is None):
            raise ValueError("Missing the required parameter `contract_addresses` when calling `get_defi_info_using_get`")  # noqa: E501
        # verify the required parameter 'chain_id' is set
        if ('chain_id' not in params or
                params['chain_id'] is None):
            raise ValueError("Missing the required parameter `chain_id` when calling `get_defi_info_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'chain_id' in params:
            path_params['chain_id'] = params['chain_id']  # noqa: E501

        query_params = []
        if 'contract_addresses' in params:
            query_params.append(('contract_addresses', params['contract_addresses']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/rugpull_detecting/{chain_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetDefiInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
