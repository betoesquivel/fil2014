# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exhibitor'
        db.create_table(u'exhibitors_exhibitor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'exhibitors', ['Exhibitor'])

        # Adding model 'Workshop'
        db.create_table(u'exhibitors_workshop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ages', self.gf('django.db.models.fields.CharField')(default='Todas', max_length=15)),
        ))
        db.send_create_signal(u'exhibitors', ['Workshop'])

        # Adding model 'WorkshopEvents'
        db.create_table(u'exhibitors_workshopevents', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('startTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('endTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('eventDescription', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('workshop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Workshop'])),
        ))
        db.send_create_signal(u'exhibitors', ['WorkshopEvents'])

        # Adding model 'Stand'
        db.create_table(u'exhibitors_stand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('exhibitor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Exhibitor'])),
            ('workshop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Workshop'])),
        ))
        db.send_create_signal(u'exhibitors', ['Stand'])

        # Adding model 'Editorial'
        db.create_table(u'exhibitors_editorial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('exhibitor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Exhibitor'])),
        ))
        db.send_create_signal(u'exhibitors', ['Editorial'])

        # Adding model 'Book'
        db.create_table(u'exhibitors_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('synopsis', self.gf('django.db.models.fields.CharField')(max_length=1500)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('editorial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Editorial'])),
        ))
        db.send_create_signal(u'exhibitors', ['Book'])

        # Adding model 'Author'
        db.create_table(u'exhibitors_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'exhibitors', ['Author'])

        # Adding M2M table for field books on 'Author'
        m2m_table_name = db.shorten_name(u'exhibitors_author_books')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('author', models.ForeignKey(orm[u'exhibitors.author'], null=False)),
            ('book', models.ForeignKey(orm[u'exhibitors.book'], null=False))
        ))
        db.create_unique(m2m_table_name, ['author_id', 'book_id'])

        # Adding model 'Category'
        db.create_table(u'exhibitors_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Book'])),
        ))
        db.send_create_signal(u'exhibitors', ['Category'])

        # Adding model 'Award'
        db.create_table(u'exhibitors_award', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Book'])),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Author'])),
        ))
        db.send_create_signal(u'exhibitors', ['Award'])

        # Adding model 'Volunteer'
        db.create_table(u'exhibitors_volunteer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('studentID', self.gf('django.db.models.fields.CharField')(max_length=9)),
        ))
        db.send_create_signal(u'exhibitors', ['Volunteer'])

        # Adding model 'BookRegistered'
        db.create_table(u'exhibitors_bookregistered', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('volunteer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Volunteer'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exhibitors.Book'])),
        ))
        db.send_create_signal(u'exhibitors', ['BookRegistered'])


    def backwards(self, orm):
        # Deleting model 'Exhibitor'
        db.delete_table(u'exhibitors_exhibitor')

        # Deleting model 'Workshop'
        db.delete_table(u'exhibitors_workshop')

        # Deleting model 'WorkshopEvents'
        db.delete_table(u'exhibitors_workshopevents')

        # Deleting model 'Stand'
        db.delete_table(u'exhibitors_stand')

        # Deleting model 'Editorial'
        db.delete_table(u'exhibitors_editorial')

        # Deleting model 'Book'
        db.delete_table(u'exhibitors_book')

        # Deleting model 'Author'
        db.delete_table(u'exhibitors_author')

        # Removing M2M table for field books on 'Author'
        db.delete_table(db.shorten_name(u'exhibitors_author_books'))

        # Deleting model 'Category'
        db.delete_table(u'exhibitors_category')

        # Deleting model 'Award'
        db.delete_table(u'exhibitors_award')

        # Deleting model 'Volunteer'
        db.delete_table(u'exhibitors_volunteer')

        # Deleting model 'BookRegistered'
        db.delete_table(u'exhibitors_bookregistered')


    models = {
        u'exhibitors.author': {
            'Meta': {'object_name': 'Author'},
            'books': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['exhibitors.Book']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exhibitors.award': {
            'Meta': {'object_name': 'Award'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Author']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exhibitors.Book']"}),
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