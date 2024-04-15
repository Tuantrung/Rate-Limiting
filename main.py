from datetime import datetime, timedelta


def handle_input():
    # Taking input for N and R
    n, r = map(int, input().split())

    # Define the rate limit period in hours
    rate_limit_period = timedelta(hours=1)

    # Initialize variables to keep track of requests and the last request time
    requests_count = 0
    last_request_time = None

    # Handling N requestsR
    for _ in range(n):
        # Take input for each request timestamp
        timestamp_str = input().strip()
        datetime_obj = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S%z")
        epoch_time = int(datetime_obj.timestamp())
        print(epoch_time)

        # # Check if the last request time is within the rate limit period
        # if last_request_time is not None and timestamp - last_request_time < rate_limit_period:
        #     # If not, wait until the rate limit period is over
        #     wait_time = rate_limit_period - (timestamp - last_request_time)
        #     wait_seconds = wait_time.total_seconds()
        #     # Convert wait time from seconds to hours for clarity
        #     wait_hours = wait_seconds / 3600
        #     print(f"Rate limit exceeded. Waiting for {wait_hours:.2f} hours.")
        #     # Update the last request time to reflect the rate limit period
        #     last_request_time += rate_limit_period
        # else:
        #     # If within the rate limit, process the request
        #     print("Processing request:", timestamp)
        #     # Update the last request time to the current timestamp
        #     last_request_time = timestamp
        #     # Increment the request count
        #     requests_count += 1
        #
        #     # Check if the rate limit is reached
        #     if requests_count >= R:
        #         print("Rate limit reached. Please try again later.")
        #         break


def get_usage(current_timestamp, hour_limit):
    usage = {}
    stop = 0
    return usage,top


def rate_limiting_handler():
    return


# Example usage
if __name__ == "__main__":
    handle_input()
