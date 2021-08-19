# 10914 150 10916 10911 52 60
# Aug 17 05:40:00.006299 10914=aaa;150=A;10916=1;52=20210816;60=2
# Aug 17 05:40:00.006299 10914=aaa;150=A;10916=1;52=20210816;60=2
# Aug 17 05:40:00.006299 10914=aaa;150=A;10916=1;52=20210816;60=2
# Aug 17 05:40:00.006299 10914=aaa;150=A;10916=1;52=20210816;60=2

import sys
from datetime import datetime, timedelta


def parse_file(filepath):
  with open(filepath, 'r') as f:
    msgs = f.readlines()
  msg_dict = {}
  key_list = []
  for msg in msgs:
    tokens = msg.split()
    ts = ' '.join(tokens[:3])
    key = tokens[3]
    if key not in msg_dict:
      msg_dict[key] = ts
      key_list.append(key)
  return msg_dict, key_list


def main():
  sent_path = ''
  recv_path = ''
  offset_hours = 0
  nargv = len(sys.argv)

  if nargv >= 3:
    sent_path = sys.argv[1]
    recv_path = sys.argv[2]
    if nargv == 4:
      offset_hours = int(sys.argv[3])
  else:
    print('usage: python latency.py sentfile recvfile [offset_hours]\n'
          ' e.g.: python latency.py a b\n'
          ' e.g.: python latency.py a b 8')
    exit(1)

  sent_dict, sent_list = parse_file(sent_path)
  recv_dict, recv_list = parse_file(recv_path)

  for key in sent_list:
    sent_ts_str = sent_dict[key]
    sent_ts = datetime.strptime(sent_ts_str, '%b %d %H:%M:%S.%f')
    recv_ts_str = recv_dict[key]
    recv_ts = datetime.strptime(recv_ts_str, '%b %d %H:%M:%S.%f')
    #diff = (recv_ts - sent_ts) // timedelta(microseconds=1)
    #diff = (recv_ts - sent_ts) / timedelta(milliseconds=1)
    diff = (recv_ts - sent_ts + timedelta(hours=offset_hours)) / timedelta(seconds=1)
    print(f'{key}: sent={sent_ts_str}, recv={recv_ts_str}, diff={diff}')


if __name__ == '__main__':
  main()

