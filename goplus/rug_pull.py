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
from swagger_client.api.defi_controller_api import DefiControllerApi


class RugPull(Base):
    """
    Rug-pull detection
    """

    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = DefiControllerApi()

    def rug_pull_security(self, chain_id: str, address: str, **kwargs):
        return self.api.get_defi_info_using_get(
            contract_addresses=address,
            chain_id=chain_id,
            **self.authorization,
            **kwargs
        )
