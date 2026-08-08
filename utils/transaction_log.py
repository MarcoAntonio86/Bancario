from datetime import datetime


def transaction_log(func):
    def wrapper(*args, **kwargs):
        date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        print(
            f"\n[LOG] Date and time: {date_time} | "
            f"Operation: {func.__name__}"
        )

        return func(*args, **kwargs)

    return wrapper