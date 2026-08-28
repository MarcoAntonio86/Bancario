from datetime import datetime, timedelta, timezone


def transaction_log(func):
    def wrapper(*args, **kwargs):
        date_time = datetime.now(
            timezone(timedelta(hours=-3))
        ).strftime("%d-%m-%Y %H:%M:%S")

        result = func(*args, **kwargs)

        log_entry = (
            f"Date and time: {date_time} | "
            f"Operation: {func.__name__} | "
            f"Args: {args} | "
            f"Kwargs: {kwargs} | "
            f"Return: {result}\n"
        )

        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(log_entry)

        return result

    return wrapper