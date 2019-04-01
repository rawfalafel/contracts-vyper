from tests.constants import (
    ETH_RESERVE,
    YUT_RESERVE,
    INITIAL_ETH,
)

def test_balance_liquidity(w3, YUT_token, YUT_exchange):
    ## Verify balance

    a0, a1, a2 = w3.eth.accounts[:3]

    assert w3.eth.getBalance(a1) == INITIAL_ETH
    
     
     


