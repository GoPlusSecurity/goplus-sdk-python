from swagger_client.api.website_controller_api import WebsiteControllerApi

from goplus.base import Base


class PushingSite(Base):

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)

    def pushing_site_security(self, url: str, **kwargs):
        return WebsiteControllerApi().phishing_site_using_get(url, **self.authorization, **kwargs)
