# Generated by Django 4.1.7 on 2024-11-25 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_clubjoinrequest_agree_meeting_attendance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='agree_meeting_attendance',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='agree_program_participation',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='agree_to_behavior',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='agree_to_disciplinary_rules',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='agree_to_general_member_terms',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='agree_to_respectfulness',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='agree_to_tools_usage',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='agree_to_truthfulness',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='experience_details',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='facebook_profile_link',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='other_clubs_details',
        ),
        migrations.RemoveField(
            model_name='clubjoinrequest',
            name='profile_photo',
        ),
    ]
