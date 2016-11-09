# -*- coding:utf-8 -*-

import turbo.log

from base import BaseHandler
from helpers import dc as dc_helper
from db.conn import dc_files


logger = turbo.log.getLogger(__file__)

db_dc = dc_helper.dc


class HomeHandler(BaseHandler):

    _get_params = {
        'option': [
            ('skip', int, 0),
            ('limit', int, 0)
        ]
    }

    def get(self, *args, **kwargs):
        skip = self._params['skip']
        limit = self._params['limit']
        dcs = db_dc.find(limit=limit, skip=skip, sort=[('atime', -1)])
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


class EditHandler(BaseHandler):

    def get(self, tp, objid):
        skip = self._skip
        limit = self._limit

        if tp != 'dc':
            return

        dc = db_dc.find_by_id(objid)
        if not dc:
            return

        dc['used'] = ','.join(dc['used'])
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
        dc['desc'] = self._params['desc']
        dc['used'] = self._params['used']
        dc['spec'] = self._params['spec']
        dc['expiration'] = self._params['expiration']

        if self.request.files.get('file', None):
            self.request.files['file'][0]['body']
            dc['file'] = dc_files.put(self.request.files['file'][0]['body'])
            dc['file_name'] = self.request.files['file'][0]['filename']

        db_dc.save(dc)
        message = 'success! update %s,  %s' % (dc['name'], dc['desc'])
        dc['used'] = ','.join(dc['used'])
        self.render('dcedit.html', message=message, dc=dc, limit=limit, skip=skip)


class DelHandler(BaseHandler):
    pass


class FileHandler(BaseHandler):

    def get(self, objid):

        dc = db_dc.find_one({'file': self.to_objectid(objid)})

        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=%s' % dc['file_name'])

        self.write(dc_files.get(self.to_objectid(objid)).read())
