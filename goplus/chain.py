from swagger_client.api.token_controller_v_1_api import TokenControllerV1Api


class Chain(object):
    """
    Supported Blockchains
    """

    @classmethod
    def get_chain_list(cls, **kwargs):
        return TokenControllerV1Api().get_chains_list_using_get(**kwargs)
