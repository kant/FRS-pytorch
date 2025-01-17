import torch


def parse_cfg(cfg_path):
    ret = {}
    with open(cfg_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == '#':  # notation skip
                continue
            line = line.strip().split(':')
            ret[line[0]] = line[1].strip()
    return ret


# def create_model(nb_class, input_size):
#     # create pytorch model by config
#     model = Net(nb_class, input_size)
#     return model


def load_classes(path):
    classes = {}
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(' ')
            class_, idx = line[0], line[1]
            classes[int(idx)] = class_
    return classes


def load_prices(path):
    prices = {}
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(' ')
            class_, price = line[0], line[1]
            prices[class_] = price
    return prices
