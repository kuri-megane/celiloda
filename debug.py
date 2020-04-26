from lambda_function import lambda_handler


def success():
    event = ""
    context = ""
    lambda_handler(event=event, context=context)


if __name__ == '__main__':
    success()
