import numpy as np
from graph import plot_two_graphs 




class Node:
    def __init__(self, data):
        self.arrivalTime = data
        self.next = None



def generate_exp(mu: int) -> int: 
    u = np.random.uniform(0, 1)
    return -(np.log(1-u)/mu)



def simmulate_poisson_process(NUM_JOBS: float, ARRIVAL_RATE: float, JOB_SIZE_RATE: float) -> tuple[float, float, float]: 

    INF = np.inf
    arrival_counter, completed_counter = 0, 0


    # recording stats
    mean_response_time = 0
    mean_jobs_in_system = 0

    # define our initial state below
    global_clock = 0
    jobs_in_system = 0
    time_to_next_arrival = generate_exp(ARRIVAL_RATE)
    time_to_next_completion = INF

    head = Node(time_to_next_arrival)
    tail = head

    running_average_busy_server = 0

    while completed_counter < NUM_JOBS: 
        
        # if next event is arrival
        if time_to_next_arrival < time_to_next_completion: 

            # update global clock
            global_clock += time_to_next_arrival

            # decrease time to next completion since we just decremented
            time_to_next_completion -= time_to_next_arrival

            # increase jobs in the system
            jobs_in_system += 1

            # generate new arrival
            time_to_next_arrival = generate_exp(ARRIVAL_RATE)

            # add the arrival time to our linked list
            new_arrival_node = Node(global_clock)

            # case on if the linked list is empty or not
            if tail: 
                tail.next = new_arrival_node
                tail = tail.next
            else: 
                assert(head == None)
                head = new_arrival_node
                tail = new_arrival_node

            # if this is the only job in the system, 
            if jobs_in_system == 1: 
                # generate a completion time for this job since it will be immedeately started
                time_to_next_completion = generate_exp(JOB_SIZE_RATE)
                running_average_busy_server = (running_average_busy_server / (arrival_counter + 1)) * arrival_counter
            else: 
                running_average_busy_server = (running_average_busy_server / (arrival_counter + 1)) * arrival_counter + 1/(arrival_counter + 1)
        
            # record stats for mean number of jobs in the system (PASTA)
            mean_jobs_in_system = (mean_jobs_in_system / (arrival_counter + 1)) * arrival_counter + (jobs_in_system / (arrival_counter + 1))

            # update arrival counter every time event arrives
            arrival_counter += 1
        

        # else if next event is completion
        else: 
            assert(time_to_next_completion < time_to_next_arrival)

            # update global clock
            global_clock += time_to_next_completion

            # update the time to next arrival since we passed time
            time_to_next_arrival -= time_to_next_completion

            # decrement jobs in the system
            jobs_in_system -= 1
            assert(jobs_in_system >= 0)

            # if no jobs are in the system, 
            if (jobs_in_system == 0):
                # set time to next completion to inf
                time_to_next_completion = INF

            # if there is still a job in the sytem  
            else: 
                # generate new completion time
                time_to_next_completion = generate_exp(JOB_SIZE_RATE)

            # get the head of the linked list and find the deperature time. also delete the head
            assert(head)
            oldest_arrival_time = head.arrivalTime
            head = head.next

            # update the average with global clock - departure time
            response_time = global_clock - oldest_arrival_time
            mean_response_time = response_time / (completed_counter + 1) + mean_response_time * completed_counter / (completed_counter + 1)

            # increment completed counter
            completed_counter += 1

    print(f"Just simulated Poisson Process. Arrival Rate: {ARRIVAL_RATE} Job Size Rate: {JOB_SIZE_RATE} Mean Response Time: {mean_response_time} Mean Jobs In System: {mean_jobs_in_system}")
    
    return (mean_response_time, mean_jobs_in_system, running_average_busy_server)
    


def get_stats_for_poisson_process(JOB_SIZE_RATE, rates_to_check: list[float], NUMBER_OF_JOBS=10**6, with_graph=True):
    print(f"Simulating Poisson Processes with {NUMBER_OF_JOBS} number of jobs of the following arrival rates: ", rates_to_check)

    mean_response_times_list, mean_jobs_in_system_list, server_utilization_list = [], [], []

    for arrival_rate in rates_to_check: 
        mean_response_time, mean_jobs_in_system, server_utilization = simmulate_poisson_process(NUMBER_OF_JOBS, arrival_rate, JOB_SIZE_RATE)
        mean_response_times_list.append(mean_response_time)
        mean_jobs_in_system_list.append(mean_jobs_in_system)
        server_utilization_list.append(server_utilization)

    print("!!FINISHED PROCESS!!")

    if (with_graph):
        plot_two_graphs(rates_to_check, mean_jobs_in_system_list,  mean_response_times_list, server_utilization_list)


if __name__ == "__main__":
    rates_to_check1 = [i/10.0 for i in range(5, 10, 1)]  
    get_stats_for_poisson_process(1, rates_to_check1)

    rates_to_check2 = [2*i/10.0 for i in range(5, 10, 1)]
    get_stats_for_poisson_process(2, rates_to_check2)
    
    


        