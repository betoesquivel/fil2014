# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Award.book'
        db.alter_column(u'exhibitors_award', 'book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Book'], null=True))

        # Changing field 'Award.author'
        db.alter_column(u'exhibitors_award', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Author'], null=True))

    def backwards(self, orm):

        # Changing field 'Award.book'
        db.alter_column(u'exhibitors_award', 'book_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['exhibitors.Book']))

        # Changing field 'Award.author'
        db.alter_column(u'exhibitors_award', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['exhibitors.Author']))

    models = {
        u'exhibitors.author': {
            'Meta': {'object_name': 'Author'},
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['exhibitors.Book']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exhibitors.award': {
            'Meta': {'object_name': 'Award'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exhibitors.Author']", 'null': 'True', 'blank': 'True'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['exhibitors.Book']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'exhibitors.book': {
            'Meta': {'object_name': 'Book'},
            'editorial': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Editorial']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'synopsis': ('django.db.models.fields.CharField', [], {'max_length': '1500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exhibitors.bookregistered': {
            'Meta': {'object_name': 'BookRegistered'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'volunteer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Volunteer']"})
        },
        u'exhibitors.category': {
            'Meta': {'object_name': 'Category'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'exhibitors.editorial': {
            'Meta': {'object_name': 'Editorial'},
            'exhibitor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Exhibitor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'exhibitors.exhibitor': {
            'Meta': {'object_name': 'Exhibitor'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'exhibitors.stand': {
            'Meta': {'object_name': 'Stand'},
            'exhibitor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Exhibitor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Workshop']"})
        },
        u'exhibitors.volunteer': {
            'Meta': {'object_name': 'Volunteer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'studentID': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        u'exhibitors.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'ages': ('django.db.models.fields.CharField', [], {'default': "'Todas'", 'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'exhibitors.workshopevents': {
            'Meta': {'object_name': 'WorkshopEvents'},
            'endTime': ('django.db.models.fields.DateTimeField', [], {}),
            'eventDescription': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'startTime': ('django.db.models.fields.DateTimeField', [], {}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Workshop']"})
        }
    }

    complete_apps = ['exhibitors']