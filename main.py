import time
from multiprocessing import Process
from pool_mapper import map_network, initialize
from latency_test import update
from awesome_scraper import main


# Time between updates; not possible for script to lag for more than twice this
# plus 110 seconds
UPDATE = 3600


while True:
	start = time.time()
	weights, rpc = initialize()
	# map_network(rpc, weights, choice, is_balance, pause)
	pool_mapper = Process(target=map_network, args=(rpc, weights, 0, False, 0))
	pool_mapper.start()

	latency_test = Process(target=update)
	latency_test.start()

	pool_mapper.join(UPDATE)
	elapsed = min(time.time()-start, UPDATE-100) # give it at least 100s to finish
	latency_test.join(UPDATE-elapsed)

	# awesome_scraper updates gif from latency images, so must be run after latencytest
	elapsed = min(time.time()-start, UPDATE-10) # give it at least 10s to finish
	awesome = Process(target=main)
	awesome.start()
	awesome.join(UPDATE-elapsed)


	awesome.terminate()
	latency_test.terminate()
	pool_mapper.terminate()

	time.sleep(UPDATE)