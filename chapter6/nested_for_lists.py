my_sizes = ['S', 'M', 'XS']


def clearing_list(size_list=None):
    matching_sizes=[]
    if size_list is not None:
        for my_size in my_sizes:
            for size in size_list:
                if size == my_size:
                    matching_sizes.append(my_size)

    print("We have your sizes: {} from available sizes: {}".format(matching_sizes, size_list))


available_sizes = ['L', 'XL', 'M', 'S']

clearing_list(available_sizes)
# clearing_list()
# clearing_list([])
