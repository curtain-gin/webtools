import logging

def get_logger():
    """
    默认肉孜节哦
    """
    logger=logging.getLogger('django')
    return logger
def decorator_log(func):
    def log(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            get_logger().error(e)
    return log

