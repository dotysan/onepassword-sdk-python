# AUTO-GENERATED
from .core import _invoke
from json import loads
from .iterator import SDKIterator
from .types import ItemOverview, Item


class Items:
    """
    The Items API holds all operations the SDK client can perform on 1Password items.
    """

    def __init__(self, client_id):
        self.client_id = client_id

    async def create(self, params):
        """
        Create a new item
        """
        response = await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "ItemsCreate",
                    "parameters": {
                        "params": params.dict(),
                    },
                },
            }
        )
        return Item(**loads(response))

    async def get(self, vault_id, item_id):
        """
        Get an item by vault and item ID
        """
        response = await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "ItemsGet",
                    "parameters": {
                        "item_id": item_id,
                        "vault_id": vault_id,
                    },
                },
            }
        )
        return Item(**loads(response))

    async def put(self, item):
        """
        Update an existing item.
        """
        response = await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "ItemsPut",
                    "parameters": {
                        "item": item.dict(),
                    },
                },
            }
        )
        return Item(**loads(response))

    async def delete(self, vault_id, item_id):
        """
        Delete an item.
        """

        await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "ItemsDelete",
                    "parameters": {
                        "item_id": item_id,
                        "vault_id": vault_id,
                    },
                },
            }
        )

    async def list(self, vault_id):
        """
        List all items
        """
        response = await _invoke(
            {
                "clientId": self.client_id,
                "invocation": {
                    "name": "ItemsList",
                    "parameters": {
                        "vault_id": vault_id,
                    },
                },
            }
        )
        response_data = loads(response)

        objects = [ItemOverview(**data) for data in response_data]

        return SDKIterator(objects)
