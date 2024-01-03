from web3 import Web3
import json

# Load in the ABI (Application Binary Interface) for the contract
with open("files/PAIR_ABI.json") as f:
    abi = json.loads(json.load(f).get("ABI"))

# Configure an RPC connection to an Ethereum node
NODE_URL = "https://rpc.flashbots.net"
rpc = Web3(Web3.HTTPProvider(NODE_URL))

# Create a Web3.py Contract object for a specific pair
PAIR_ADDRESS = "0x0d4a11d5EEaaC28EC3F61d100daF4d40471f1852"
pair = rpc.eth.contract(address=PAIR_ADDRESS, abi=abi)

# Get the current block number on the chain
block_number = rpc.eth.block_number
print(f"Current block number: {block_number}")

# Look back 2000 blocks and fetch all Swap events for the pair
swap_events = pair.events.Swap.get_logs(fromBlock=block_number - 2000)
print(f"Found {len(swap_events)} Swap events")

# Let's analyze the first swap event in the response
swap = swap_events[0]

args = dict(swap.args) # The Swap event data dictionary
tx_hash = swap.transactionHash.hex() # The hash of the transaction that included the Swap event
tx_index = swap.transactionIndex # The index of the transaction in the block
block_number = swap.blockNumber # The block number of the block that included the Swap event

# Print out the data for the first Swap event
print(f"\nTransaction Hash:\t{tx_hash}")
print(f"Transaction Index:\t{tx_index}")
print(f"Block Number:\t\t{block_number}")
print(f"\nEvent Data:\n{args}")
