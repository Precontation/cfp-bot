from upstash_redis import Redis
redis = Redis.from_env()

try:
    response = redis.get('766046835109789716')
  
    if response is not None:
        print("Response successful, returning " + str(response))
    else:
        print("No value found for that key! weird because that's my key... hm")
except Exception as e:
    print("Redis request failed:", e)
