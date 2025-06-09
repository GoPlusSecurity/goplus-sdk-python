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
from swagger_client.api.lock_controller_api import LockControllerApi


class Locker(Base):
    def __init__(self, access_token=None):
        super().__init__(access_token=access_token)
        self.api = LockControllerApi()

    def locker_token(
        self, chain_id: str, token_address: str, page_num: int, page_size: int, **kwargs
    ):
        return self.api.get_token_lockers_using_get(
            chain_id=chain_id,
            token_address=token_address,
            page_num=page_num,
            page_size=page_size,
            **self.authorization,
            **kwargs
        )

    def locker_lp_v3(
        self, chain_id: str, pool_address: str, page_num: int, page_size: int, **kwargs
    ):
        return self.api.get_nft_lockers_using_get(
            chain_id=chain_id,
            pool_address=pool_address,
            page_num=page_num,
            page_size=page_size,
            **self.authorization,
            **kwargs
        )
