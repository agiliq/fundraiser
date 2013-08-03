# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Publisher.website'
        db.alter_column(u'books_publisher', 'website', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'Publisher.email'
        db.alter_column(u'books_publisher', 'email', self.gf('django.db.models.fields.EmailField')(default='', unique=True, max_length=70))

    def backwards(self, orm):

        # Changing field 'Publisher.website'
        db.alter_column(u'books_publisher', 'website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Publisher.email'
        db.alter_column(u'books_publisher', 'email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=70, null=True))

    models = {
        u'books.book': {
            'Meta': {'object_name': 'Book'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['books.Publisher']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'synopsis': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'books.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '70', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['books']