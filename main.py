from datetime import datetime


def input_handler():
    # Taking input for N and R
    n, r = map(int, input().split())

    timestamps_list = []

    # Handling N requests R
    for i in range(n):
        # Take input for each request timestamp
        timestamp_str = input().strip()
        datetime_obj = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S%z")
        # Convert time format to unix time
        epoch_time = int(datetime_obj.timestamp())
        timestamps_list.append(epoch_time)

    return r, timestamps_list


def rate_limited_handler(r, timestamps_list):
    window_start = timestamps_list[0]
    window_end = window_start + 3600
    window = []

    for timestamp in timestamps_list:
        if timestamp > window_end:
            window.pop(0)
            window_start = window[0]
            window_end = window_start + 3600
            window.append(timestamp)
            print("true")
        else:
            if len(window) < r:
                window.append(timestamp)
                print("true")
            else:
                print("false")


if __name__ == "__main__":
    rate_limit, timestamps = input_handler()
    rate_limited_handler(rate_limit, timestamps)
