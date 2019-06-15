import os
import random


def generate_test_file(N, file_number):
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            "test-" + str(N) + "-" + str(file_number) + ".txt")
    f = open(filename, "w+")
    f.write(str(N) + "\n")
    for i in range(2 * N - 2):
        f.write(str(random.uniform(-200.0, 200.0)) + " ")
    f.write(str(random.uniform(-200.0, 200.0)) + "\n")
    for i in range(N - 1):
        f.write(str(random.uniform(-200.0, 200.0)) + " ")
    f.write(str(random.uniform(-200.0, 200.0)) + "\n")
    f.close()
    return filename


if __name__ == '__main__':

    sizes = [4096]
    for s in sizes:
        print("Testing instances of size: " + str(s))
        instance_size = s
        times_elapsed = []
        for i in range(3):
            print("Performing test number " + str(i))
            filename = generate_test_file(instance_size, i)
        #     start = time.time()
        #     results = teoplitz(*file_to_array(filename))
        #     end = time.time()
        #     time_elapsed = end - start
        #     times_elapsed.append(time_elapsed)
        #     print("Time elapsed (in seconds): "+str(time_elapsed))
        #     write_results_to_file(filename, results)
        # mean_time_elapsed = sum(times_elapsed) / float(len(times_elapsed))
        # print("Mean elapsed time for instances: "+ str(mean_time_elapsed))
