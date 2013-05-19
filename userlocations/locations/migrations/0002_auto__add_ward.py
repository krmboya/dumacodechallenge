# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ward'
        db.create_table(u'locations_ward', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('num', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.County'])),
        ))
        db.send_create_signal(u'locations', ['Ward'])


    def backwards(self, orm):
        # Deleting model 'Ward'
        db.delete_table(u'locations_ward')


    models = {
        u'locations.county': {
            'Meta': {'object_name': 'County'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'locations.ward': {
            'Meta': {'object_name': 'Ward'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.County']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['locations']