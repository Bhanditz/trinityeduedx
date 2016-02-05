# -*- coding: utf-8 -*-
from south.v2 import DataMigration
from django.core.exceptions import ObjectDoesNotExist


class Migration(DataMigration):

    def forwards(self, orm):
        for authuser in orm['auth.User'].objects.all():
            try:
                tprofile = orm.TrinityUserProfile.objects.get(user=authuser)
            except ObjectDoesNotExist:
                tprofile = orm.TrinityUserProfile(user=authuser)
                tprofile.save()

    def backwards(self, orm):
        for authuser in orm['auth.User'].objects.all():
            try:
                tprofile = orm.TrinityUserProfile.objects.get(user=authuser)
                tprofile.delete()
            except ObjectDoesNotExist:
                pass

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
    'trinityeduedx.trinityuserprofile': {
        'Meta': {'object_name': 'TrinityUserProfile'},
        'district': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
        'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
        'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trinitypreferences'", 'to': "orm['auth.User']"})
    }
}

complete_apps = ['trinityeduedx']
symmetrical = True
