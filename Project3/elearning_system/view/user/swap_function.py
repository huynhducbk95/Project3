
# check login

def check_log_in(name_func):
    def swapper_function(request):
        print ('login is true')
        name_func(request)
    return swapper_function