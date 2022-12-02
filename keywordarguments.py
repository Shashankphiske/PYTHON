# keyword arguments =  these are arguments that are preceded by an identifier when we pass them to a function
#                      the order of the argument doesnt matter , unlike positional arguments 
#                      python knowss the names of the arguments that our function receives

def hello(first , middle , last):
    print("hello "+first +middle +last)

hello(first="shashank",middle=" satish",last=" phiske")# now even of we change the place of the arguments it doesnt
                                                       # matter (eg: we replace first = "shashank" in place of 
                                                       # last = "phiske")
                                                        