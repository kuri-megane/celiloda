def set_env():
    from os.path import join, dirname
    from dotenv import load_dotenv
    load_dotenv(verbose=True)
    env_file_path = join(dirname(__file__), '.env')
    load_dotenv(env_file_path)


def success():
    from lambda_function import main
    event = {
        "body": "{\n  \"kind\":1,\n  \"val\":36.0\n}"
    }
    context = ""
    ret = main(event=event, context=context)
    print(ret)


if __name__ == '__main__':
    set_env()
    success()
