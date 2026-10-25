import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
import gunicorn
app = Flask(__name__)

# 配置日志
def setup_logger():
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.DEBUG)

    # 避免重复添加 handler
    if not logger.handlers:
        # 输出到 app.log 文件，按大小轮转
        file_handler = RotatingFileHandler(
            'app.log',
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding='utf-8'
        )
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

logger = setup_logger()


@app.route('/log', methods=['GET'])
def log_demo():
    """调用日志函数，打印日志到 app.log"""
    logger.info('接口被调用了，这是一条日志记录')
    return {'status': 'ok', 'message': '日志已写入 app.log'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)