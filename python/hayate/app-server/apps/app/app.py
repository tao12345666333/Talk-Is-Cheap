# -*- coding:utf-8 -*-

import turbo.log

from base import BaseHandler
from helpers import dc as dc_helper
from db.conn import dc_files


logger = turbo.log.getLogger(__file__)

db_dc = dc_helper.dc


class HomeHandler(BaseHandler):

    def get(self, *args, **kwargs):
        skip = self._skip
        limit = self._limit
        dcs = db_dc.find(limit=limit, skip=skip, sort=[('atime', -1)])

        dcs = list(dcs)

        self.render('index.html', dcs=dcs, limit=limit, skip=skip)


class CreateHandler(BaseHandler):

    def get(self, tp):
        limit = self._limit
        skip = self._skip

        if tp != 'dc':
            return

        self.render('dccreate.html', message='', limit=limit, skip=skip)

    _post_params = {
        'option': [
            ('name', basestring, ''),
            ('desc', basestring, ''),
            ('used', list, []),
            ('spec', basestring, ''),
            ('expiration', basestring, ''),

            ('file', file, None),
        ]
    }

    def post(self, tp):
        # print self.request.files['file'][0]['body']
        limit = self._limit
        skip = self._skip

        if tp != 'dc':
            return

        name = self._params['name']
        desc = self._params['desc']
        used = self._params['used']
        spec = self._params['spec']
        expiration = self._params['expiration']

        file = self._params['file']

        # print file

        # print type(file)
        fid = None

        try:
            fid = dc_files.put(self.request.files['file'][0]['body'])
        except Exception, e:
            print e

        db_dc.create({
            'name': name,
            'desc': desc,
            'used': used,
            'spec': spec,
            'expiration': expiration,

            'file': fid,
            'file_name': self.request.files['file'][0]['filename']
        })

        message = 'success! add %s,  %s' % (name, desc)
        self.render('dccreate.html', message=message, limit=limit, skip=skip)


class ListHandler(BaseHandler):

    def get(self, tp):
        skip = self._skip
        limit = self._limit

        if tp != 'dc':
            return

        dcs = db_dc.find(limit=limit, skip=skip)
        self.render('dclist.html', dcs=dcs, limit=limit, skip=skip)


class EditHandler(BaseHandler):

    def get(self, tp, objid):
        skip = self._skip
        limit = self._limit

        if tp != 'dc':
            return

        dc = db_dc.find_by_id(objid)
        if not dc:
            return

        self.render('dcedit.html', message='', dc=dc, limit=limit, skip=skip)

    _post_params = {
        'option': [
            ('name', basestring, ''),
            ('desc', basestring, ''),
            ('used', list, []),
            ('spec', basestring, ''),
            ('expiration', basestring, ''),
        ]
    }

    def post(self, tp, objid):
        limit = self._limit
        skip = self._skip

        if tp != 'dc':
            return

        dc = db_dc.find_by_id(objid)
        if not dc:
            return
        dc['name'] = self._params['name']
        dc['rank'] = self._params['rank'] or 0
        db_dc.save(dc)
        message = 'success! update %s,  %s' % (dc['name'], dc['desc'])
        self.render('dcedit.html', message=message, dc=dc, limit=limit, skip=skip)


class DelHandler(BaseHandler):
    pass


class FileHandler(BaseHandler):

    def get(self, objid):

        dc = db_dc.find_one({'file': self.to_objectid(objid)})

        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=%s' % dc['file_name'])

        self.write(dc_files.get(self.to_objectid(objid)).read())
