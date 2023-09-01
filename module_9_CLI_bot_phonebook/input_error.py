# input_error.py

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid input format."
        except IndexError:
            return "Command arguments missing."
    return wrapper
