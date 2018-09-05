# coding: utf-8
import logging.config
import os
import yaml
import codecs


config_file_path = os.path.join(os.path.dirname(__file__), 'log.yaml')
with codecs.open(config_file_path, mode='r', encoding='utf-8') as config_file:
    config_dict = yaml.load(config_file)

logging.config.dictConfig(config_dict)
logger = logging.getLogger('output_logger.release_logger')
logger.debug('我是歌手_debug')
logger.info('我是歌手_info')
logger.error('我是歌手_error')
