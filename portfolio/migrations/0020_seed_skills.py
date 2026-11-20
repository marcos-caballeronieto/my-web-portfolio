from django.db import migrations


def seed_skills(apps, schema_editor):
    SkillCategory = apps.get_model('portfolio', 'SkillCategory')
    Skill = apps.get_model('portfolio', 'Skill')

    categories_data = [
        {
            'name': 'Machine Learning & Medical AI',
            'name_en': 'Machine Learning & Medical AI',
            'name_es': 'Machine Learning e IA Médica',
            'description_en': 'Applied in Chest X-Ray AI: Clinical Triage Optimization.',
            'description_es': 'Aplicado en Chest X-Ray AI: Clinical Triage Optimization.',
            'icon': 'fas fa-brain',
            'order': 1,
            'is_main': True,
            'skills': [
                ('Supervised Learning', 'Aprendizaje Supervisado'),
                ('Scikit-Learn', 'Scikit-Learn'),
                ('PyTorch', 'PyTorch'),
                ('Transfer Learning', 'Transfer Learning'),
                ('Medical Imaging', 'Imagen Médica'),
                ('DenseNet121', 'DenseNet121'),
            ],
        },
        {
            'name': 'AI Engineering',
            'name_en': 'AI Engineering',
            'name_es': 'Ingeniería de IA',
            'description_en': 'Supported by multimodal AI work and agentic development courses.',
            'description_es': 'Respaldada por experiencia con IA multimodal y cursos de desarrollo agéntico.',
            'icon': 'fas fa-robot',
            'order': 2,
            'is_main': True,
            'skills': [
                ('LLM Evaluation', 'Evaluación de LLMs'),
                ('Prompt Engineering', 'Prompt Engineering'),
                ('Multimodal AI', 'IA Multimodal'),
                ('AI-Assisted Development', 'Desarrollo con IA'),
                ('Coding Agents', 'Agentes de Código'),
                ('Claude Code', 'Claude Code'),
            ],
        },
        {
            'name': 'Biomedical & Clinical Computing',
            'name_en': 'Biomedical & Clinical Computing',
            'name_es': 'Computación Biomédica y Clínica',
            'description_en': 'Grounded in biomedical engineering and clinical trial projects.',
            'description_es': 'Basada en la formación biomédica y los proyectos de ensayos clínicos.',
            'icon': 'fas fa-flask',
            'order': 3,
            'is_main': True,
            'skills': [
                ('Biomedical Data', 'Datos Biomédicos'),
                ('Signal Processing', 'Procesado de Señales'),
                ('Clinical Algorithms', 'Algoritmos Clínicos'),
                ('Randomization', 'Aleatorización'),
                ('Statistical Balance', 'Equilibrio Estadístico'),
                ('Healthcare Applications', 'Aplicaciones Sanitarias'),
            ],
        },
        {
            'name': 'Web & Software Engineering',
            'name_en': 'Web & Software Engineering',
            'name_es': 'Ingeniería Web y de Software',
            'description_en': 'Demonstrated by this Django portfolio and its custom CMS.',
            'description_es': 'Demostrada en este portfolio Django y su CMS personalizado.',
            'icon': 'fas fa-code',
            'order': 4,
            'is_main': True,
            'skills': [
                ('Python', 'Python'),
                ('Django 5', 'Django 5'),
                ('SQLite', 'SQLite'),
                ('HTML & CSS', 'HTML y CSS'),
                ('Bootstrap', 'Bootstrap'),
                ('Git & GitHub', 'Git y GitHub'),
            ],
        },
    ]

    for cat_data in categories_data:
        category, _ = SkillCategory.objects.get_or_create(
            name=cat_data['name'],
            defaults={
                'name_en': cat_data['name_en'],
                'name_es': cat_data['name_es'],
                'description_en': cat_data['description_en'],
                'description_es': cat_data['description_es'],
                'icon': cat_data['icon'],
                'order': cat_data['order'],
                'is_main': cat_data['is_main'],
                'is_visible': True,
            },
        )
        for index, (skill_en, skill_es) in enumerate(cat_data['skills'], start=1):
            Skill.objects.get_or_create(
                category=category,
                name=skill_en,
                defaults={
                    'name_en': skill_en,
                    'name_es': skill_es,
                    'order': index,
                    'is_visible': True,
                    'show_on_about': True,
                },
            )


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_certificatecategory_skillcategory_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_skills, reverse_code=migrations.RunPython.noop),
    ]
