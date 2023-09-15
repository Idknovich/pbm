import traceback

def execute(code):
    try:
        exec(code)
    except Exception as error:

        traceback_info = traceback.format_exc().split("\n")
        line_with_error = traceback_info[-2]
        
        why=f"error: {str(error)}\n in line: '{line_with_error}'"
        print(why)
