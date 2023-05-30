# Copyright 2023 The GoPlus. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from goplus.base import Base
from swagger_client.api.website_controller_api import WebsiteControllerApi


class PushingSite(Base):
    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = WebsiteControllerApi()

    def pushing_site_security(self, url: str, **kwargs):
        return self.api.phishing_site_using_get(url, **self.authorization, **kwargs)
