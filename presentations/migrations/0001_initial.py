# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Presentator'
        db.create_table(u'presentations_presentator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'presentations', ['Presentator'])

        # Adding model 'Conference'
        db.create_table(u'presentations_conference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('startTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('endTime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'presentations', ['Conference'])

        # Adding M2M table for field presentators on 'Conference'
        m2m_table_name = db.shorten_name(u'presentations_conference_presentators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('conference', models.ForeignKey(orm[u'presentations.conference'], null=False)),
            ('presentator', models.ForeignKey(orm[u'presentations.presentator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['conference_id', 'presentator_id'])

        # Adding model 'BookPresentation'
        db.create_table(u'presentations_bookpresentation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('startTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('endTime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'presentations', ['BookPresentation'])

        # Adding M2M table for field presentators on 'BookPresentation'
        m2m_table_name = db.shorten_name(u'presentations_bookpresentation_presentators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bookpresentation', models.ForeignKey(orm[u'presentations.bookpresentation'], null=False)),
            ('presentator', models.ForeignKey(orm[u'presentations.presentator'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bookpresentation_id', 'presentator_id'])


    def backwards(self, orm):
        # Deleting model 'Presentator'
        db.delete_table(u'presentations_presentator')

        # Deleting model 'Conference'
        db.delete_table(u'presentations_conference')

        # Removing M2M table for field presentators on 'Conference'
        db.delete_table(db.shorten_name(u'presentations_conference_presentators'))

        # Deleting model 'BookPresentation'
        db.delete_table(u'presentations_bookpresentation')

        # Removing M2M table for field presentators on 'BookPresentation'
        db.delete_table(db.shorten_name(u'presentations_bookpresentation_presentators'))


    models = {
        u'presentations.bookpresentation': {
            'Meta': {'object_name': 'BookPresentation'},
            'endTime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'presentators': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['presentations.Presentator']", 'symmetrical': 'False'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'startTime': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'presentations.conference': {
            'Meta': {'object_name': 'Conference'},
            'endTime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'presentators': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['presentations.Presentator']", 'symmetrical': 'False'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'startTime': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'presentations.presentator': {
            'Meta': {'object_name': 'Presentator'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['presentations']