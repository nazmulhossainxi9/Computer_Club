# Generated by Django 4.1.7 on 2024-11-25 15:50

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_applyclub_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyclub',
            name='interests',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('graphics_design', 'Graphics Design'), ('video_editing', 'Video Editing'), ('motion_graphics', 'Motion Graphics'), ('competitive_programming', 'Competitive Programming'), ('web_development', 'Web Development'), ('android_development', 'Android Development'), ('e_sports', 'E-Sports'), ('ui_ux_design', 'UI/UX Design'), ('event_management', 'Event Management'), ('content_writing', 'Content Writing'), ('photography', 'Photography'), ('paper_crafting', 'Paper Crafting'), ('volunteering', 'Volunteering'), ('singing', 'Singing'), ('dancing', 'Dancing'), ('anchoring', 'Anchoring'), ('debating', 'Debating'), ('other', 'Other')], max_length=241),
        ),
        migrations.AddField(
            model_name='applyclub',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('graphics_design', 'Graphics Design'), ('video_editing', 'Video Editing'), ('motion_graphics', 'Motion Graphics'), ('competitive_programming', 'Competitive Programming'), ('web_development', 'Web Development'), ('android_development', 'Android Development'), ('e_sports', 'E-Sports'), ('ui_ux_design', 'UI/UX Design'), ('event_management', 'Event Management'), ('content_writing', 'Content Writing'), ('photography', 'Photography'), ('paper_crafting', 'Paper Crafting'), ('volunteering', 'Volunteering'), ('singing', 'Singing'), ('dancing', 'Dancing'), ('anchoring', 'Anchoring'), ('debating', 'Debating'), ('other', 'Other')], max_length=241),
        ),
    ]
