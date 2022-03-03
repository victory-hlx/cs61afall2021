test = {
  'name': 'smallest-int-having',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_having LIMIT 48;
          11/17/2021 14:08:17|5
          11/19/2021 11:35:27|18
          11/17/2021 13:52:09|21
          11/18/2021 15:08:53|25
          11/17/2021 12:16:43|28
          11/18/2021 14:12:41|36
          11/17/2021 14:15:51|39
          11/18/2021 19:59:35|40
          11/17/2021 14:10:34|43
          11/17/2021 11:55:11|44
          11/17/2021 11:31:44|48
          11/19/2021 14:14:30|51
          11/19/2021 14:45:10|52
          11/19/2021 17:54:28|53
          11/17/2021 15:21:03|68
          11/17/2021 23:54:56|70
          11/17/2021 14:11:08|71
          11/18/2021 13:16:24|72
          11/18/2021 10:16:50|73
          11/17/2021 14:20:21|79
          11/17/2021 18:43:56|82
          11/17/2021 17:47:18|87
          11/17/2021 13:07:02|90
          11/17/2021 14:05:41|91
          11/18/2021 10:05:37|98
          11/19/2021 10:01:21|101
          11/17/2021 15:06:44|109
          11/17/2021 15:43:52|110
          11/17/2021 14:01:02|111
          11/18/2021 21:51:14|132
          11/17/2021 22:56:05|136
          11/19/2021 17:08:03|137
          11/18/2021 23:35:30|188
          11/18/2021 20:09:55|189
          11/17/2021 13:32:19|213
          11/17/2021 12:23:14|234
          11/17/2021 18:57:14|237
          11/18/2021 14:19:55|246
          11/18/2021 20:21:46|285
          11/19/2021 14:36:01|302
          11/17/2021 12:04:38|412
          11/19/2021 14:20:01|414
          11/18/2021 15:55:30|500
          11/17/2021 16:30:36|819
          11/17/2021 14:10:58|827
          11/17/2021 14:06:09|995
          11/17/2021 14:05:52|1153
          11/17/2021 21:16:57|1234
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab13.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
