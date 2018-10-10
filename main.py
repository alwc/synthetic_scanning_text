import utils
from printer import Printer


def text_generator():
    for i in range(10):
        yield str(i), 1


def generate(config_file):
    # config = io.read_config(config_file)
    # todo 主体逻辑
    printer = Printer("fonts/fangsong_GB2312.ttf", 16)
    for img, text in printer.print(16, 16, text_generator()):
        utils.save_sample("%s.jpg" % text, img)


if __name__ == '__main__':
    generate(None)
