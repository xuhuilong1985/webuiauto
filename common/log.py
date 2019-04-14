# -*- coding:utf-8
# author: huilong xu
# time: 2019-4-14
# description: basic class for log
import logging
import os, sys

class basic_log(object):
    def __init__(self):
        pass
    def set_loglevel(self, log_level):
        if log_level.upper() == "INFO":
            self.logger.setLevel(logging.INFO)
        elif log_level.upper() == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        elif log_level.upper() == "WARNING":
            self.logger.setLevel(logging.WARNING)
        elif log_level.upper() == "ERROR":
            self.logger.setLevel(logging.ERROR)
        else:
            self.logger.setLevel(logging.CRITICAL)
        ch = logging.StreamHandler()
        fh = logging.FileHandler('%s/%s.log' % (self._log_path_, self._logname_))
        self.logformatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
        ch.setFormatter(self.logformatter)
        fh.setFormatter(self.logformatter)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def log_info(self, message):
        self.logger.info(message)
    def log_debug(self, message):
        call_function_name = sys._getframe().f_back.f_code.co_name
        call_function_line = sys._getframe().f_back.f_lineno
        self.logger.debug("fuction: %s() - line %s : %s "%(call_function_name, call_function_line, message))
    def log_warning(self, message):
        self.logger.warning(message)
    def log_error(self, message):
        self.logger.error(message)
    def log_critical(self, message):
        self.logger.critical(message)
    def set_logpath(self, file_path = os.curdir):
        self._log_path_ = file_path
    def set_logname(self, log_name = "default"):
        self._logname_ = log_name
        self.logger = logging.getLogger(self._logname_)

class test_log(basic_log):
    def __init__(self, name):
        self.component_name = name
        super(test_log, self).__init__()
        self.set_logname(self.component_name)
        self.set_logpath(os.curdir)
    def add(self):
        self.log_debug("3 + 5 = 8")
        self.log_info("2 +4 = 6")
        self.log_warning("1+6 = 7")
        self.log_error("0 +0 = 0")
        self.log_critical("8 +9 =17")
if __name__ == '__main__':
    test_log_list = ["testlog_debug", "testlog_critica"]
    test_log_lever_list = ["debug", "critica"]
    for index in range(len(test_log_list)):
        log_instance = test_log(test_log_list[index])
        log_instance.set_loglevel(test_log_lever_list[index])
        log_instance.add()


