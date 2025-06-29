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


class ApproveControllerV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def address_contract_using_get1(self, address, **kwargs):  # noqa: E501
        """Check if the address is malicious  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_contract_using_get1(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: address (required)
        :param str authorization: Authorization token in the format: Bearer <token> (e.g., Bearer eyJsZXZlbCI6NSwiYXBwTmFtZSI6ImF2cyIsImFwcEtleSI6IjFaW...)
        :param str chain_id: The chain_id of the blockchain. To check the corresponding blockchain name for a given chain_id, please visit: https://docs.gopluslabs.io/reference/response-details-9
        :return: ResponseWrapperAddressContract
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.address_contract_using_get1_with_http_info(address, **kwargs)  # noqa: E501
        else:
            (data) = self.address_contract_using_get1_with_http_info(address, **kwargs)  # noqa: E501
            return data

    def address_contract_using_get1_with_http_info(self, address, **kwargs):  # noqa: E501
        """Check if the address is malicious  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.address_contract_using_get1_with_http_info(address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str address: address (required)
        :param str authorization: Authorization token in the format: Bearer <token> (e.g., Bearer eyJsZXZlbCI6NSwiYXBwTmFtZSI6ImF2cyIsImFwcEtleSI6IjFaW...)
        :param str chain_id: The chain_id of the blockchain. To check the corresponding blockchain name for a given chain_id, please visit: https://docs.gopluslabs.io/reference/response-details-9
        :return: ResponseWrapperAddressContract
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address', 'authorization', 'chain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method address_contract_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `address_contract_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address' in params:
            path_params['address'] = params['address']  # noqa: E501

        query_params = []
        if 'chain_id' in params:
            query_params.append(('chain_id', params['chain_id']))  # noqa: E501

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
            '/api/v1/address_security/{address}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseWrapperAddressContract',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def approval_contract_using_get(self, chain_id, contract_addresses, **kwargs):  # noqa: E501
        """Check if the approval is secure   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.approval_contract_using_get(chain_id, contract_addresses, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chain_id: Chain id, (ETH: 1,  BSC: 56, OKC: 66, Heco: 128, Polygon: 137, Fantom:250, Arbitrum: 42161, Avalanche: 43114) (required)
        :param str contract_addresses: Contract needs to be detected (required)
        :param str authorization: Authorization token in the format: Bearer <token> (e.g., Bearer eyJsZXZlbCI6NSwiYXBwTmFtZSI6ImF2cyIsImFwcEtleSI6IjFaW...)
        :return: ResponseWrapperContractApproveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.approval_contract_using_get_with_http_info(chain_id, contract_addresses, **kwargs)  # noqa: E501
        else:
            (data) = self.approval_contract_using_get_with_http_info(chain_id, contract_addresses, **kwargs)  # noqa: E501
            return data

    def approval_contract_using_get_with_http_info(self, chain_id, contract_addresses, **kwargs):  # noqa: E501
        """Check if the approval is secure   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.approval_contract_using_get_with_http_info(chain_id, contract_addresses, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chain_id: Chain id, (ETH: 1,  BSC: 56, OKC: 66, Heco: 128, Polygon: 137, Fantom:250, Arbitrum: 42161, Avalanche: 43114) (required)
        :param str contract_addresses: Contract needs to be detected (required)
        :param str authorization: Authorization token in the format: Bearer <token> (e.g., Bearer eyJsZXZlbCI6NSwiYXBwTmFtZSI6ImF2cyIsImFwcEtleSI6IjFaW...)
        :return: ResponseWrapperContractApproveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chain_id', 'contract_addresses', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method approval_contract_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chain_id' is set
        if ('chain_id' not in params or
                params['chain_id'] is None):
            raise ValueError("Missing the required parameter `chain_id` when calling `approval_contract_using_get`")  # noqa: E501
        # verify the required parameter 'contract_addresses' is set
        if ('contract_addresses' not in params or
                params['contract_addresses'] is None):
            raise ValueError("Missing the required parameter `contract_addresses` when calling `approval_contract_using_get`")  # noqa: E501

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
            '/api/v1/approval_security/{chain_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseWrapperContractApproveResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
