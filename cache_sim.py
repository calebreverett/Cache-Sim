import math

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("This is Caleb Everett's Project \n")
    START_SIZE = 128
    FINAL_SIZE = 16384
    START_BLOCK_SIZE = 4
    FINAL_BLOCK_SIZE = 16

    file = open('Trace files/swim.trace', 'r')
    lines = file.readlines()
    addresses = []
    for line in lines:
        binary = bin(int(line[4:12], 16))[2:].zfill(32)
        addresses.append(binary)

    line_size = START_BLOCK_SIZE
    while line_size <= FINAL_BLOCK_SIZE:
        offset = int(math.log2(line_size))
        # Direct Mapped
        size = START_SIZE
        while size <= FINAL_SIZE:
            lines = size / line_size
            line_set = math.log2(lines)
            i = 0
            cache = dict()
            counter = 0
            hits = 0
            itr = 0
            for address in addresses:
                address_length = len(address)
                tag_length = int(address_length - offset - line_set)
                temp_tag = address[:tag_length]
                counter += 1
                line_num = int(address[tag_length:address_length - offset], 2)
                if line_num in cache and cache[line_num] == temp_tag:
                    hits += 1
                else:
                    cache[line_num] = temp_tag
            print("For a Direct Mapped Cache with a size of " + str(size) + " bytes and a block size of " + str(line_size) + " bytes, the hitrate is " + str(
                hits / counter))
            size *= 2
        print("\n")
    
        # Fully Associative(FIFO)
        size = START_SIZE
        while size <= FINAL_SIZE:
            lines = size/line_size
            i = 0
            cache = []
            counter = 0
            hits = 0
            for address in addresses:
                counter += 1
                address_length = len(address)
                temp_tag = address[:address_length - offset]
                if temp_tag in cache:
                    hits += 1
                elif len(cache) < lines:
                    cache.insert(0, temp_tag)
                else:
                    cache.insert(0, temp_tag)
                    cache.pop()
            print("For a Fully Associative(FIFO) Cache with a size of " + str(size) + " bytes and a block size of " + str(line_size) + " bytes, the hitrate is " + str(
                hits / counter))
            size *= 2
        print("\n")
    
        # Fully Associative(LRU)
        size = START_SIZE
        while size <= FINAL_SIZE:
            lines = size / line_size
            i = 0
            cache = []
            counter = 0
            hits = 0
            itr = 0
            for address in addresses:
                address_length = len(address)
                counter += 1
                temp_tag = address[:address_length - offset]
                if temp_tag in cache:
                    hits += 1
                    cache.remove(temp_tag)
                    cache.insert(0, temp_tag)
                elif len(cache) < lines:
                    cache.insert(0, temp_tag)
                else:
                    cache.pop()
                    cache.insert(0, temp_tag)
            print("For a Fully Associative(LRU) Cache with a size of " + str(size) + " bytes and a block size of " + str(line_size) + " bytes, the hitrate is " + str(
                hits / counter))
            size *= 2
        print("\n")
    
        # 2-way Set Associative(FIFO)
        size = START_SIZE
        while size <= FINAL_SIZE:
            lines = size / line_size
            sets = int(lines / 2)
            line_set = int(math.log2(sets))
            cache = dict()
            for x in range(0, sets):
                cache[x] = list()
            counter = 0
            hits = 0
            for address in addresses:
                address_length = len(address)
                tag_length = int(address_length - offset - line_set)
                temp_tag = address[:tag_length]
                counter += 1
                set_num = int(address[tag_length:address_length - offset], 2)
                if set_num in cache and temp_tag in cache[set_num]:
                    hits += 1
                else:
                    if set_num in cache and len(cache[set_num]) < 2:
                        cache[set_num].insert(0, temp_tag)
                    else:
                        cache[set_num].insert(0, temp_tag)
                        cache[set_num].pop()
            print("For a 2-way Set Associative Cache(FIFO) with a size of " + str(size) + " bytes and a block size of " + str(line_size) + " bytes, the hitrate is " + str(
                hits / counter))
            size *= 2
        print("\n")
    
        # 2-way Set Associative(LRU)
        size = START_SIZE
        while size <= FINAL_SIZE:
            lines = size / line_size
            sets = int(lines / 2)
            line_set = int(math.log2(sets))
            cache = dict()
            for x in range(0, sets):
                cache[x] = list()
            counter = 0
            hits = 0
            for address in addresses:
                address_length = len(address)
                tag_length = int(address_length - offset - line_set)
                temp_tag = address[:tag_length]
                counter += 1
                set_num = int(address[tag_length:address_length - offset], 2)
                if set_num in cache and temp_tag in cache[set_num]:
                    hits += 1
                    cache[set_num].remove(temp_tag)
                    cache[set_num].insert(0, temp_tag)
                else:
                    if set_num in cache and len(cache[set_num]) < 2:
                        cache[set_num].insert(0, temp_tag)
                    else:
                        cache[set_num].insert(0, temp_tag)
                        cache[set_num].pop()
            print("For a 2-way Set Associative Cache(LRU) with a size of " + str(size) + " bytes and a block size of " + str(line_size) + " bytes, the hitrate is " + str(
                hits / counter))
            size *= 2
        print("\n")
    
        # 4-way Set Associative(FIFO)
        size = START_SIZE
        while size <= FINAL_SIZE:
            lines = size / line_size
            sets = int(lines / 4)
            line_set = int(math.log2(sets))
            cache = dict()
            for x in range(0, sets):
                cache[x] = list()
            counter = 0
            hits = 0
            for address in addresses:
                address_length = len(address)
                tag_length = int(address_length - offset - line_set)
                temp_tag = address[:tag_length]
                counter += 1
                set_num = int(address[tag_length:address_length - offset], 2)
                if set_num in cache and temp_tag in cache[set_num]:
                    hits += 1
                else:
                    if set_num in cache and len(cache[set_num]) < 4:
                        cache[set_num].insert(0, temp_tag)
                    else:
                        cache[set_num].insert(0, temp_tag)
                        cache[set_num].pop()
            print("For a 4-way Set Associative Cache(FIFO) with a size of " + str(size) + " bytes and a block size of " + str(line_size) + " bytes, the hitrate is " + str(
                hits / counter))
            size *= 2
        print("\n")
    
        # 4-way Set Associative(LRU)
        size = START_SIZE
        while size <= FINAL_SIZE:
            lines = size / line_size
            sets = int(lines / 4)
            line_set = int(math.log2(sets))
            cache = dict()
            for x in range(0, sets):
                cache[x] = list()
            counter = 0
            hits = 0
            for address in addresses:
                address_length = len(address)
                tag_length = int(address_length - offset - line_set)
                temp_tag = address[:tag_length]
                counter += 1
                set_num = int(address[tag_length:address_length - offset], 2)
                if set_num in cache and temp_tag in cache[set_num]:
                    hits += 1
                    cache[set_num].remove(temp_tag)
                    cache[set_num].insert(0, temp_tag)
                else:
                    if set_num in cache and len(cache[set_num]) < 4:
                        cache[set_num].insert(0, temp_tag)
                    else:
                        cache[set_num].insert(0, temp_tag)
                        cache[set_num].pop()
            print("For a 4-way Set Associative Cache(LRU) with a size of " + str(size) + " bytes and a block size of " + str(line_size) + " bytes, the hitrate is " + str(
                hits / counter))
            size *= 2
        print("\n")
        line_size *= 2
