# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'locations_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('num', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('lat', self.gf('django.db.models.fields.CharField')(default='0.000000', max_length=255, blank=True)),
            ('lon', self.gf('django.db.models.fields.CharField')(default='0.000000', max_length=255, blank=True)),
            ('ward', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Ward'])),
        ))
        db.send_create_signal(u'locations', ['Location'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'locations_location')


    models = {
        u'locations.county': {
            'Meta': {'object_name': 'County'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'locations.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'default': "'0.000000'", 'max_length': '255', 'blank': 'True'}),
            'lon': ('django.db.models.fields.CharField', [], {'default': "'0.000000'", 'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'ward': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['locations.Ward']"})
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