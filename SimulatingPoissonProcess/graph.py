import matplotlib.pyplot as plt

def plot_two_graphs(x_values, mean_number_of_jobs, mean_response_time, server_busyness):
    """
    Plots two graphs side-by-side: one for mean number of jobs vs. x-axis and 
    one for mean response time vs. x-axis, with an additional line representing
    Little's Law on the mean number of jobs plot.
    
    Parameters:
        x_values (list or array): Values for the x-axis (e.g., lambda).
        mean_number_of_jobs (list or array): Y-values for the mean number of jobs.
        mean_response_time (list or array): Y-values for the mean response time.
    """
    # Calculate Little's Law prediction for mean number of jobs
    littles_law_jobs = [mean_response_time[i] * x_values[i] for i in range(len(x_values))]
    
    # Set up the figure and subplots
    plt.figure(figsize=(12, 5))

    # Plot for mean number of jobs
    plt.subplot(1, 3, 1)  # 1 row, 2 columns, 1st subplot
    plt.plot(x_values, mean_number_of_jobs, marker='o', color='blue', label='Mean Number of Jobs')
    plt.plot(x_values, littles_law_jobs, linestyle='--', color='red', label="Little's Law Prediction")
    plt.xlabel("Lambda")
    plt.ylabel("Mean Number of Jobs")
    plt.title("Mean Number of Jobs vs Lambda")
    plt.legend()

    # Plot for mean response time
    plt.subplot(1, 3, 2)  # 1 row, 2 columns, 2nd subplot
    plt.plot(x_values, mean_response_time, marker='s', color='green', label='Mean Response Time')
    plt.xlabel("Lambda")
    plt.ylabel("Mean Response Time")
    plt.title("Mean Response Time vs Lambda")
    plt.legend()

        # Plot for mean response time
    plt.subplot(1, 3, 3)  # 1 row, 2 columns, 2nd subplot
    plt.plot(x_values, server_busyness, marker='p', color='blue', label='Server Utilization')
    plt.xlabel("Lambda")
    plt.ylabel("Server Utilization")
    plt.title("Mean Response Utilization vs Lambda")
    plt.legend()

    # Display the plots
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()


