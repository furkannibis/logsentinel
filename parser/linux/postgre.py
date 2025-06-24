from re import findall
from datetime import datetime, timedelta, timezone

from parser.linux.definitions import PSQL_DEF



class PSQL_LOG(PSQL_DEF):
    def __init__(self, **data):
        super().__init__(**data)

    def read_psql(self) -> str:
        self.psql_log_dict = []
        for path in self.path:
            with open(file=path, mode="r", encoding="UTF-8", buffering=self.buffer) as postgre_log_files:
                postgre_log_files = postgre_log_files.readlines()
        
            for postgre_log_file in range(len(postgre_log_files)):  
                date_match = findall(r'\b(19\d\d|20\d\d)[-/](0[1-9]|1[0-2])[-/](0[1-9]|[12]\d|3[01])\b', postgre_log_files[postgre_log_file])[0]
                time_match = findall(r"\b\d{2}:\d{2}:\d{2}\.\d{3}\b",postgre_log_files[postgre_log_file])[0]

                tz_match = findall(r"\s([+-]\d{2})\s", postgre_log_files[postgre_log_file])[0]
                tz_offset = int(tz_match)
                tz = timezone(timedelta(hours=tz_offset))

                dt = datetime.strptime(f'{"/".join(date_match)} {time_match}', "%Y/%m/%d %H:%M:%S.%f")
                dt_with_tz = dt.replace(tzinfo=tz)

                pid = int(findall('\[(.*?)\]', postgre_log_files[postgre_log_file])[0])
                mesg_type = findall(r"\] (\w+):", postgre_log_files[postgre_log_file])[0]
                message = findall(r":\s+(.*)", postgre_log_files[postgre_log_file])[0]
                
                self.psql_log_dict.append(
                    {
                        "date": dt_with_tz,
                        "pid": pid,
                        "message_type": mesg_type,
                        "message": message
                    }
                )
