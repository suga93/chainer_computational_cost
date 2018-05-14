from chainer.functions.array.concat import Concat
from chainer.functions.array.reshape import Reshape
from chainer.functions.array.resize_images import ResizeImages
from chainer.functions.array.transpose import Transpose


def calc_concat(func: Concat, in_data, **kwargs):
    size = sum([x.size for x in in_data])
    return (0, size, size, {'axis': func.axis})


def calc_reshape(func: Reshape, in_data, **kwargs):
    return (0, 0, 0, {'shape': func.shape})


def calc_resize(func: ResizeImages, in_data, **kwargs):
    x, = in_data
    batch_size, in_c = x.shape[:2]
    out_size = batch_size * in_c * func.out_H * func.out_W
    params = {'size': (func.out_H, func.out_W)}
    return (out_size * 18, out_size * 4, out_size, params)


def calc_transpose(func: Transpose, in_data, **kwargs):
    x, = in_data
    return (0, x.size, x.size, {'axes': func.axes})
