__author__ = 'nickl-'

# Abstraction layer of pure python only helpers to simplify the implementation
# complexities for ipython as gnu make SHELL.


def prompt(kx):
    """
    Facilitate the validation and usage printout for
    targets with required values.
    """
    if len(kx['value'].strip()) == 0:
        print kx['message']
        if 'usage' in kx:
            print '{:>9}\n{:10}{}'.format('Usage:', '', kx['usage'])
        return True
    return False

def prompt_in(msg):
    """
    Assist with getting a prompt flushed in make target process.
    Hopefully there are more elegant ways but I tried readline, stdin, stdout,
    input, even print function and it is not like they ace only slightly broken
    this is the only way I have managed to both display the prompt message
    before the wait on read and successfully managed to retrieve the results.
    works for now...
    """
    from sys import stdout
    print msg
    stdout.flush()
    inp = raw_input('')
    stdout.flush()
    return inp