import redis
import json

ITEM_KEY = 'books:items'

def process_item(item):
    #添加处理数据的代码

def main():
    r = redis.StrictRedis(host = '39.107.99.146', port = 6379)
    for _ in range(r.llen(ITEM_KEY)):
        data = r.lpop(ITEM_KEY)
        item = json.loads(data.decode('utf8'))
        process_item(item)

if __name__ == '__main__':
    main()
