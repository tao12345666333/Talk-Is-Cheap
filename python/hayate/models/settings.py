# -*- coding:utf-8 -*-

from db.conn import (
    test as _test,
    dc as _dc,

    test_files as _test_files,
    dc_files as _dc_files,
)

MONGO_DB_MAPPING = {
    'db': {
        'test': _test,
        'dc': _dc,
    },
    'db_file': {
        'test': _test_files,
        'dc': _dc_files,
    }
}
