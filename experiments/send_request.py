# Copyright 2021 - 2022 Kersten Henrik Breuer (kersten-breuer@outlook.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

response = requests.post(
    "http://127.0.0.1:8080/api/v1/greet/en",
    json={"greeting": "Hello", "person": "world"},
    headers={
        "Content-Type": "application/json",
    },
    params={"informal": "true"},
)

print(response.json())
