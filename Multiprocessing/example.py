from multiprocessing import Pool
import time

_time = time.time()


def count(name):
	for i in range(1, 50000):
		print(name, i)


if __name__ == "__main__":
	num_list = ["p1", "p2", "p3", "p4"]

	pool = Pool(processes=2)
	pool.map(count, num_list)
	pool.close()
	pool.join()

print("---- %s seconds ----" % (time.time() - _time))
