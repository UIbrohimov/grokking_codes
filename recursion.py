# make a 30 level of nested dictionary with str keys
nested_dictionary = {
    'key1': {
        'key2': {
            'key3': {
                'key4': {
                    'key5': {
                        'key6': {
                            'key7': {
                                'key8': {
                                    'key9': {
                                        'key10': {
                                            'key11': {
                                                'key12': {
                                                    'key13': {
                                                        'key14': {
                                                            'key15': {
                                                                'key16': {
                                                                    'key17': {
                                                                        'key18': {
                                                                            'key19': {
                                                                                'key20': {
                                                                                    'key21': {
                                                                                        'key22': {
                                                                                            'key23': {
                                                                                                'key24': {
                                                                                                    'key25': {
                                                                                                        'key26': {
                                                                                                            'key27': {
                                                                                                                'key28': {
                                                                                                                    'found' : True
                                                                                                                }
                                                                                                            }
                                                                                                        }
                                                                                                    }
                                                                                                }
                                                                                            }
                                                                                        }
                                                                                    }
                                                                                }
                                                                            }
                                                                        }
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

def findFound(data, lookup_value):
    if data.get(lookup_value) is not None:
        print(data.get(lookup_value))
        return True
    else:
        for key, value in data.items():
            if isinstance(data[key], dict):
                return findFound(data[key], lookup_value)
            else:
                return False

# print(findFound(nested_dictionary, 'found'))

# look for tail recursion!


def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1 % num2)

# print(gcd(1680, 640))

# here we used divide and qonquire to find a GCD of two numbers
    # 1. Figure out a simple case as the base case.
    # 2. Figure out how to reduce your problem and get to the base case

def sum(ls: list = None):
    if len(ls) == 1:
        return ls[0]
    return ls[0] + sum(ls[1:])

print(sum([1, 2, 3]))


def length(ls):
    if len(ls) == 1:
        return 1
    return 1 + length(ls[1:])

print(length([1, 2, 3]))

def maximum(ls):
    if len(ls) == 1:
        return 1
    return 1 + maximum(ls[1:])

print(maximum([1, 2, 3]))

