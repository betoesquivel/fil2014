# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Search'
        db.create_table(u'searches_search', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('requests', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('author', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('book', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('category', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'searches', ['Search'])


    def backwards(self, orm):
        # Deleting model 'Search'
        db.delete_table(u'searches_search')


    models = {
        u'searches.search': {
            'Meta': {'object_name': 'Search'},
            'author': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'book': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'requests': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['searches']