import blockchain as bc
import block

if __name__ == "__main__":
    bc = bc.Blockchain()
    bc.create_genesis_block()
    bc.next_block(block.Data('a', 'b','c'))
    bc.next_block(block.Data('z', 'a','x'))
    # print(bc.get_last_block().hash)
    c = bc.next_block(block.Data('k','f','g'))
    print(bc.get_block('2').hash)
    print(bc.get_relate_blocks('a'))

    pass