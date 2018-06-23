# Generated by Django 2.0.6 on 2018-06-23 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EthBlock',
            fields=[
                ('block_id', models.IntegerField(primary_key=True, serialize=False)),
                ('block_ts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RCAnswer',
            fields=[
                ('answer_id', models.CharField(editable=False, max_length=66, primary_key=True, serialize=False, unique=True)),
                ('answer', models.CharField(editable=False, max_length=66, null=True)),
                ('answer_commitment', models.CharField(editable=False, max_length=66, null=True, unique=True)),
                ('history_hash', models.CharField(editable=False, max_length=66)),
                ('user', models.CharField(max_length=42)),
                ('bond', models.CharField(editable=False, max_length=66)),
                ('ts', models.IntegerField(editable=False)),
                ('is_commitment', models.BooleanField()),
                ('nonce', models.CharField(max_length=66, null=True)),
                ('db_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RCQuestion',
            fields=[
                ('question_id', models.CharField(editable=False, max_length=66, primary_key=True, serialize=False, unique=True)),
                ('user', models.CharField(editable=False, max_length=42)),
                ('question', models.TextField(editable=False, null=True)),
                ('content_hash', models.CharField(editable=False, max_length=66)),
                ('arbitrator', models.CharField(editable=False, max_length=42)),
                ('timeout', models.IntegerField()),
                ('opening_ts', models.IntegerField()),
                ('nonce', models.CharField(editable=False, max_length=66)),
                ('created', models.IntegerField()),
                ('finalize_ts', models.IntegerField(null=True)),
                ('bounty', models.CharField(max_length=66, null=True)),
                ('history_hash', models.CharField(max_length=66, null=True)),
                ('best_answer', models.CharField(max_length=66, null=True)),
                ('bond', models.CharField(max_length=66, null=True)),
                ('db_created_at', models.DateTimeField(auto_now_add=True)),
                ('db_updated_at', models.DateTimeField(auto_now=True)),
                ('db_refreshed_at', models.DateTimeField(null=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcindex.EthBlock')),
            ],
        ),
        migrations.CreateModel(
            name='RCTemplate',
            fields=[
                ('template_id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.CharField(max_length=42, null=True)),
                ('question_text', models.TextField(null=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcindex.EthBlock')),
            ],
        ),
        migrations.AddField(
            model_name='rcquestion',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcindex.RCTemplate'),
        ),
        migrations.AddField(
            model_name='rcanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcindex.RCQuestion'),
        ),
    ]
