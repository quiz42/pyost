from pyost.iost import IOST

if __name__ == '__main__':
    iost = IOST('35.180.171.246:30002')

    tx_hash = 'A62QESiGS8xNk2dD1WYebA3zxGMhpcQmY8oG8wFCYkdp'
    print(iost.get_tx_receipt_by_tx_hash(tx_hash))

    # print('Node Info:')
    # print(iost.get_node_info())
    #
    # print('Chain Info:')
    # print(iost.get_chain_info())
    #
    # print('RAM Info:')
    # print(iost.get_ram_info())
    #
    # print('Gas Ratio:')
    # print(iost.get_gas_ratio())
    #
    # print('Block #0 Info:')
    # block0 = iost.get_block_by_num(0)
    # print(block0)
    #
    # print(iost.get_block_by_hash(block0.hash, complete=True))