# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Move.parent'
        db.delete_column('practice_tracking_move', 'parent_id')

        # Adding M2M table for field parent on 'Move'
        db.create_table('practice_tracking_move_parent', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('move', models.ForeignKey(orm['practice_tracking.move'], null=False)),
            ('parentmove', models.ForeignKey(orm['practice_tracking.parentmove'], null=False))
        ))
        db.create_unique('practice_tracking_move_parent', ['move_id', 'parentmove_id'])


    def backwards(self, orm):
        # Adding field 'Move.parent'
        db.add_column('practice_tracking_move', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='Test', to=orm['practice_tracking.ParentMove']),
                      keep_default=False)

        # Removing M2M table for field parent on 'Move'
        db.delete_table('practice_tracking_move_parent')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'practice_tracking.move': {
            'Meta': {'object_name': 'Move'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'move_classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['practice_tracking.MoveClass']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'parent': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['practice_tracking.ParentMove']", 'symmetrical': 'False'}),
            'value': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'practice_tracking.moveclass': {
            'Meta': {'object_name': 'MoveClass'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'practice_tracking.parentmove': {
            'Meta': {'object_name': 'ParentMove'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'move_classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['practice_tracking.MoveClass']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'practice_tracking.sesh': {
            'Meta': {'object_name': 'Sesh'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moves': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['practice_tracking.Move']", 'symmetrical': 'False'})
        },
        'practice_tracking.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'bboyname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'crew': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moves': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['practice_tracking.Move']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'value': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['practice_tracking']