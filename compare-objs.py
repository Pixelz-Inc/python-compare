def compare_objs(obj, obj1, root=''):
    if type(obj) != type(obj1):
        # print(root + ' going out false')
        return False
    for a in dir(obj):
        if a not in dir(obj1):
            # print(root + ' going out false0')
            return False
    for a in dir(obj1):
        if a not in dir(obj):
            # print(root + ' going out false01')
            return False
    # check attributes
    if '__dict__' in dir(obj):
        assert(isinstance(obj.__dict__, dict))
        if len(obj.__dict__.keys()) != len(obj1.__dict__.keys()):
            # print(root + ' going out false')
            return False
        if len(obj.__dict__.keys()) > 0:
            for a in obj.__dict__.keys():
                if a not in obj1.__dict__.keys():
                    # print(root + ' going out false dict')
                    return False
            for attr_name in obj.__dict__.keys():
                roottemp = root + '.__dict__[\'' + attr_name + '\']'
                # print(roottemp)
                # protect against infinite recursive loop, need to check whole list of previous objects
                if not(obj is obj.__dict__[attr_name] or obj1 is obj1.__dict__[attr_name]):
                    # print(roottemp + ' going in')
                    tempval = compare_objs(obj.__dict__[attr_name], obj1.__dict__[attr_name], roottemp)
                    # print(tempval)
                    if not tempval:
                        # print(root + ' going out false attr')
                        return False
                elif obj.__dict__[attr_name] != obj1.__dict__[attr_name]:
                    # print(root + ' going out false attr1')
                    return False

    # check items
    if '__len__' in dir(obj) and '__getitem__' in dir(obj):
        try:
            if len(obj) != len(obj1):
                # print(root + ' going out false1')
                return False
            if len(obj) > 0:
                if 'keys' in dir(obj):
                    item_iterator = obj.keys()
                    add_root = '\''
                else:
                    item_iterator = range(len(obj))
                    add_root = ''
                for attr_name in item_iterator:
                    roottemp = root + '[' + add_root + str(attr_name) + add_root + ']'
                    # print(roottemp)
                    # speedup string comparison
                    if isinstance(obj.__getitem__(attr_name), str) and isinstance(obj1.__getitem__(attr_name), str):
                        if not obj.__getitem__(attr_name) == obj.__getitem__(attr_name):
                            # print(root + ' going out false attr20')
                            return False
                    else:
                        # protect against infinite recursive loop, need to check whole list of previous objects
                        if not(obj is obj.__getitem__(attr_name) or obj1 is obj1.__getitem__(attr_name)):
                            # print(roottemp + ' going in')
                            tempval = compare_objs(obj.__getitem__(attr_name), obj1.__getitem__(attr_name), roottemp)
                            # print(tempval)
                            if not tempval:
                                # print(root + ' going out false attr2')
                                return False
                        elif obj.__getitem__(attr_name) != obj1.__getitem__(attr_name):
                            # print(root + ' going out false attr3')
                            return False
        # some objects have len implemented but it throws an exception when we go too deep in the object
        # for example len(np.array(1))
        # also protect in case that keys and __getitem__ may throw as well
        except:
            return obj == obj1

    # check content
    if (not ('__len__' in dir(obj) and '__getitem__' in dir(obj))) and ('__dict__' not in dir(obj)):
        # print(root + ' going out compare2')
        return obj == obj1

    return True
