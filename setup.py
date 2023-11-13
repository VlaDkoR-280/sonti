import setuptools

setuptools.setup(
        name='sonti',
        version='1.0',
        description='Module for detecting activity in a telegram',
        author='VlaDkoR-280, Alex-bit-rus, Beescute',
        author_email='vlad@kor280.ru, aleks-mayorov@inbox.ru, atdany@mail.ru',
        packages=setuptools.find_packages(),
        install_requires=['pandas', 'telethon', 'datetime'],
        include_package_data=True,
        entry_points='''
            [console_scripts]
            sonti=scripts.sonti:run
        ''',
)
