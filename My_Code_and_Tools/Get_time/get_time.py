from datetime import datetime

#     %y 两位数的年份表示(00-99)
#     %Y 四位数的年份表示(000-9999)
#     %m 月份(01-12)
#     %d 月内中的一天(0-31)
#     %H 24小时制小时数(0-23)
#     %I 12小时制小时数(01-12)
#     %M 分钟数(00-59)
#     %S 秒(00-59)
#     %j 年内的一天(001-366)
#     %U 一年中的星期数(00-53)星期天为星期的开始
#     %w 星期(0-6)，星期天为星期的开始
#     %W 一年中的星期数(00-53)星期一为星期的开始
#     %Z 当前时区的名称

def get_now_time() -> str:
    now_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return now_time

def get_now_time_milliseconds() -> str:
    milliseconds_time = datetime.now().strftime("%m_%d_%H_%M_%S_%f")
    return milliseconds_time