import os
from threading import Thread
from time import perf_counter


def replace(filename, substr, new_substr):
    print(f'Processing the file {filename}')
    # get the contents of the file
    with open(filename, 'r') as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, 'w') as f:
        f.write(content)


def main():

    targetDir = "texts"
    scriptPath = os.path.abspath(__file__)
    scriptDir = os.path.dirname(scriptPath)
    filenames = []
    for i in range(10000):
        fileName = "test"+str(i)+".txt"
        targetFilePath = os.path.join(scriptDir,targetDir,fileName)
        filenames.append(targetFilePath)

    # create threads
    threads = [Thread(target=replace, args=(filename, 'test', 'replaced'))
            for filename in filenames]

    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f'It took {end_time- start_time :0.2f} second(s) to complete.')
