import asyncio
from web3 import Web3
from web3.gevent import AsyncWeb3
from dsc_sdk.wallet import Wallet
from dsc_sdk.client import DecimalClient


class EventSubscription:
    def __init__(self, client: DecimalClient, event_name: str, contract_address: str, callback):
        self.client = client
        self.event_name = event_name
        self.contract_address = contract_address
        self.callback = callback
        self.loop = asyncio.get_event_loop()
        self.web3_async = AsyncWeb3(Web3.HTTPProvider(client.rpc_url))

    async def start(self):
        while True:
            try:
                event_filter = self.web3_async.eth.filter({
                    "address": self.contract_address,
                    "topics": [self.event_name]
                })

                async for event in event_filter.poll():
                    await self.callback(event)

            except Exception as e:
                print(f"Error in event subscription: {e}")
                await asyncio.sleep(5)


class BlockSubscription:
    def __init__(self, client: DecimalClient, callback):
        self.client = client
        self.callback = callback
        self.loop = asyncio.get_event_loop()
        self.web3_async = AsyncWeb3(Web3.HTTPProvider(client.rpc_url))

    async def start(self):
        last_block = await self.web3_async.eth.block_number
        while True:
            current_block = await self.web3_async.eth.block_number
            if current_block > last_block:
                new_blocks = range(last_block + 1, current_block + 1)
                for block_num in new_blocks:
                    block = await self.web3_async.eth.get_block(block_num)
                    await self.callback(block)
                last_block = current_block
            await asyncio.sleep(1)
