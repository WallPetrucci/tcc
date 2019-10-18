host = 'ls-7e711ccdfac9d2f4516e065f75d0cdd590377538.cvbhjerykxan.us-east-1.rds.amazonaws.com'
pwd = 'Sg(&^Lz]t,VPhIrwyoxhaPw9]c<q{=8^'
user = 'adminwhm'
CONNECT_DB = 'mysql+pymysql://{user}:{pw}@{host}:3306/dbwhm'.format(user=user,
                                                                    pw=pwd,
                                                                    host=host)
