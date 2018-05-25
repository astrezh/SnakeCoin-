# coding=utf-8
import hashlib as hasher

# Для шифрования строк предназначен модуль hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdigest()

import datetime as date

def create_genesis_block():
    # Вручную создаем блок с нулевым индексом
    #  и произвольным хэшем предыдущего блока
    return Block(0, date.datetime.now(), "Genesis Block", "0")

# Цепь хэшей играет роль криптографического доказательства и дает гарантию, что однажды добавленный в блокчейн блок нельзя будет изменить или вовсе удалить.

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# создаем блокчейн и первый блок
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# определяем количество блоков,
# которые добавим после первого
num_of_blocks_to_add = 20

# добавим блоки в цепь
for block in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    # расскажем всем об этом!
    print "Блок #{} был добавлен в блокчейн!".format(block_to_add.index)
    print "Хэш: {}\n".format(block_to_add.hash)