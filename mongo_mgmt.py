import pymongo
# from pprint import pprint as ppt

from akpy.time_mgmt import *
from akpy.stnd_vars import StandardMessages


msg_contactak = StandardMessages.msg_contactak


def check_mongod_connection(max_sev_sel_delay=5):
    print('[', time_stamp(), '] MongoDB: verifying mongod connection')
    try:
        client = pymongo.MongoClient(serverSelectionTimeoutMS=max_sev_sel_delay)
        print('[', time_stamp(), '] CLIENT FOUND:', client)
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print(err)
        sys.exit(msg_contactak)


def get_mongo_client(host='localhost:27017', max_check_retries=5, server_selection_timeout_ms=3000):
    if type(host) is list():
        host_list = host
    elif type(host) is not list():
        host_list = [host]
    else:
        print('[', time_stamp(), '] ERROR: unknown mongo host variable assigned (def check_mongo())')
        sys.exit(msg_contactak)

    for i in range(max_check_retries):
        try:
            client = pymongo.MongoClient(host=host_list, serverSelectionTimeoutMS=server_selection_timeout_ms)
            print('[', time_stamp(), '] DB CONNECTED: MongoDB connection established')
            print('[', time_stamp(), '] SERVER INFO:', client.server_info())
        except pymongo.errors.ServerSelectionTimeoutError as err:
            print('[', time_stamp(), '] ERROR:', err)
            print('[', time_stamp(), '] RETRY',
                  str(i + 1) + ': process will retry to establish connection with MongoDB')
            continue  # retrying
        else:
            return client
    else:
        print('[', time_stamp(), '] DB CONNECTION FAILED: MongoDB connection could not establish after',
              max_check_retries,
              'attempts')


if __name__ == '__main__':
    # get_mongo_client()
    # pass
    check_mongod_connection()
