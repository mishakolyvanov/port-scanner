import logging, sys
PORT = 8000
HOST = '127.0.0.1'
TIME = 0.5


LOG_SETTINGS = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        # 'sys-logger6': {
        #     'class': 'logging.handlers.SysLogHandler',
        #     'address': '/dev/log',
        #     'facility': "local6",
        #     'formatter': 'verbose',
        # },
    },
    'loggers': {
        '': {
            'handlers': ['stdout'],
            'level': logging.DEBUG,
            'propagate': True,
        },

        # 'my-logger': {
        #     'handlers': ['sys-logger6', 'stdout'],
        #     'level': logging.DEBUG,
        #     'propagate': True,
        # },
    }
}
