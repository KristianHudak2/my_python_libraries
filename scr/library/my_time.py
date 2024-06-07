import time

def show_me_time():
    print('start_time\tfunkcion\tnone\treturn time, save in variable\nstop_time\tfunkcion\tvariable with sart time\t\t print it')

def start_time():
    return time.time()

def stop_time(start):
    end = time.time()
    duration = end - start
    return duration

