from datetime import datetime


def handle_input():
    # Taking input for N and R
    n, r = map(int, input().split())

    ts_list = []

    # Handling N requests R
    for i in range(n):
        # Take input for each request timestamp
        timestamp_str = input().strip()
        datetime_obj = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S%z")
        epoch_time = int(datetime_obj.timestamp())
        ts_list.append(epoch_time)

    return r, ts_list


# Example usage
if __name__ == "__main__":
    rate_limit, timestamp_list = handle_input()

    window_start = timestamp_list[0]
    window_end = window_start + 3600
    window = []

    for timestamp in timestamp_list:
        if timestamp > window_end:
            window.pop(0)
            window_start = window[0]
            window_end = window_start + 3600
            window.append(timestamp)
            print("true")
        else:
            if len(window) < rate_limit:
                window.append(timestamp)
                print("true")
            else:
                print("false")