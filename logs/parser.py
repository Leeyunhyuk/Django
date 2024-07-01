# import os
# from datetime import datetime
# from .models import LogEntry

# LOG_FILE_PATH = '/path/to/logfile.log'

# def parse_log_file():
#     with open(LOG_FILE_PATH, 'r') as file:
#         for line in file:
#             parts = line.split(' ')
#             timestamp = datetime.strptime(parts[0], '%Y-%m-%d %H:%M:%S')
#             log_level = parts[1]
#             message = ' '.join(parts[2:])
#             LogEntry.objects.create(timestamp=timestamp, log_level=log_level, message=message)
import os
from datetime import datetime
from .models import LogEntry

# 로그 파일 경로를 실제 존재하는 경로로 수정합니다.
LOG_FILE_PATH = '/Users/yhlee/PycharmProjects/Django/logs/logfile.log'

def parse_log_file():
    if not os.path.exists(LOG_FILE_PATH):
        print(f"Log file not found: {LOG_FILE_PATH}")
        return

    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            # 로그 파일의 각 줄을 공백으로 분리합니다.
            parts = line.split(' ', 3)
            if len(parts) < 4:
                continue  # 잘못된 형식의 로그 항목을 건너뜁니다.

            # 로그 항목의 각 부분을 추출합니다.
            timestamp_str = f"{parts[0]} {parts[1]}"
            log_level = parts[2]
            message = parts[3].strip()

            # 문자열로 된 타임스탬프를 datetime 객체로 변환합니다.
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

            # 로그 항목을 데이터베이스에 저장합니다.
            LogEntry.objects.create(timestamp=timestamp, log_level=log_level, message=message)

    print("Log file parsed and data saved to the database.")

