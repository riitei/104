# coding=utf-8
# https://blog.csdn.net/liuchunming033/article/details/39080457
__author__ = 'riitei'
import logging
class log:
    def main(self,mess):
        # 第一步，创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  # Log等级总开关

        # 第二步，创建一个handler，用于写入日志文件
        logfile = 'log.txt'
        fh = logging.FileHandler(logfile, mode='a')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

        # 第三步，再创建一个handler，用于输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        logger.addHandler(fh)
        # logger.addHandler(ch)

        # 日志
        # logger.debug('this is a logger debug message')
        logger.info(mess)
        logger.debug(mess)
        # logger.warning('this is a logger warning message')
        # logger.error('this is a logger error message')
        # logger.critical('this is a logger critical message')


if __name__ == '__main__':
    log().main('')
