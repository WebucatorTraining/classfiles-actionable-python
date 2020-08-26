from datetime import datetime

def format_report(f):
    def inner(text):
        print('MY REPORT')
        print('-' * 50)
        f(text)
        print('-' * 50)
        print('Report completed: {}.'.format(datetime.now()))
    return inner

@format_report
def report(text):
    print(text)

report('I have created my second decorator.')