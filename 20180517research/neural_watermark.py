import tensorflow as tf
import numpy as np
import scipy
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
IMAGE_H=512
IMAGE_W=512
keep_prob = tf.placeholder(tf.float32)
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    # stride [1, x_movement, y_movement, 1]
    # Must have strides[0] = strides[3] = 1

    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    # stride [1, x_movement, y_movement, 1]
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

def build_net():
    net = {}
    net['input'] = tf.Variable(np.zeros((1, IMAGE_H, IMAGE_W, 3)).astype('float32'))

    W_conv1 = weight_variable([5, 5, 3, 32])  # patch 5x5, in size 1, out size 32
    b_conv1 = bias_variable([32])

    net['conv1'] = tf.nn.relu(conv2d(net['input'], W_conv1) + b_conv1)  # output size 28x28x32
    net['pool1'] = max_pool_2x2(net['conv1'])  # output size 14x14x32

    W_conv2 = weight_variable([5, 5, 32, 4])  # patch 5x5, in size 32, out size 64
    b_conv2 = bias_variable([4])

    net['conv2'] = tf.nn.relu(conv2d(net['pool1'], W_conv2) + b_conv2)  # output size 14x14x64
    net['pool2'] = max_pool_2x2( net['conv2'])  # output size 7x7x64



    return net

def read_image(path,IMAGE_H,IMAGE_W):
  image = scipy.misc.imread(path)
  image = image[np.newaxis,:IMAGE_H,:IMAGE_W,:]

  return image

def write_image(path, image):
  image = image[0]
  image = np.clip(image, 0, 255).astype('uint8')
  scipy.misc.imsave(path, image)

def main():
    image=read_image('/home/ttc/Desktop/Lena.png',512,512)
    image2 = read_image('/home/ttc/Downloads/binary.png',128,128)
    write_image('/home/ttc/Desktop/Lena111.png', image)

    net = build_net()
    cross_entropy = net['pool2']-image2 # loss
    train_step = tf.train.AdamOptimizer(2.0).minimize(cross_entropy)

    sess = tf.Session()
    if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
        init = tf.initialize_all_variables()
    else:
        init = tf.global_variables_initializer()
    sess.run(init)


    sess.run([net['input'].assign(image)])

    for i in range(1000):
        sess.run(train_step)
        print(i)
        if i % 10==0:
            result_img = sess.run(net['input'])
            print(sess.run(net['pool1']))
            write_image('/home/ttc/Desktop/image/Lena'+str(i)+'.png',result_img)

if __name__ == '__main__':
        main()
    # IMAGE_W = 1855
# IMAGE_H = 1056
#
# def read_image(path):
#   image = scipy.misc.imread(path)
#   image = image[np.newaxis,:IMAGE_H,:IMAGE_W,:]
#
#   return image
#
# def write_image(path, image):
#   image = image
#   image = image[0]
#   image = np.clip(image, 0, 255).astype('uint8')
#   scipy.misc.imsave(path, image)
#
# def weight_variable(shape):
#     inital=tf.truncated_normal(shape,stddev=0.1)
#     return tf.Variable(inital)
#
# def bias_variable(shape):
#
#     inital=tf.constant(0.1,shape=shape)
#     return tf.Variable(inital)
#
# def conv_2D(x,W):
#     #SRIDE[1,x_movement,y_movement,1]
#     #most have stride is[1,,,1]
#     return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
#
# def max_pool_2x2(x):
#     return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
#
#
#
#
#
#
# if __name__ == '__main__':
#     image = read_image('/home/ttc/Desktop/picture.png')
#     write_image('/home/ttc/Desktop/picture1.png', image)
#
#
#
#     # conv1
#     W_conv1 = weight_variable([5, 5, 1, 32])
#     b_conv1 = bias_variable([32])
#
#     h_conv1 = tf.nn.relu(conv_2D(image, W_conv1) + b_conv1)
#     h_pool1 = max_pool_2x2(h_conv1)
#
#     # conv2
#     W_conv2 = weight_variable([5, 5, 32, 64])
#     b_conv2 = bias_variable([64])