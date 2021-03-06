# Generated by Django 3.0.6 on 2020-05-26 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaoCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classificacao', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=20)),
                ('nome_cliente', models.CharField(max_length=100)),
                ('responsavel_administrativo', models.CharField(max_length=60)),
                ('administrativo_telefone', models.CharField(max_length=12)),
                ('administrativo_email', models.CharField(max_length=50)),
                ('responsavel_tecnico', models.CharField(max_length=60)),
                ('tecnico_telefone', models.CharField(max_length=12)),
                ('tecnico_email', models.CharField(max_length=50)),
                ('classificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ClassificacaoCliente')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_site', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=150)),
                ('cep', models.CharField(max_length=10)),
                ('link_ip', models.CharField(blank=True, max_length=8, null=True)),
                ('lan_to_lan', models.CharField(blank=True, max_length=8, null=True)),
                ('vpn_l3', models.CharField(blank=True, max_length=8, null=True)),
                ('bloco_ip', models.CharField(blank=True, max_length=5, null=True)),
                ('data_ativacao', models.DateField(verbose_name='Ativação')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
        ),
    ]
