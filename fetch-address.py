from uagents import Agent
 
alice = Agent(name="alice", seed="alice recovery phrase")
 
print("Fetch network address: ", alice.wallet.address())

