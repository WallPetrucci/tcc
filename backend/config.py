import os

<<<<<<< Updated upstream

CONNECT_DB = 'mysql+pymysql://{user}:{pw}@{host}/mydb'.format(user=os.environ['WHM_DB_USER'],
                                                              pw=os.environ['WHM_DB_PW'],
                                                              host=os.environ['WHM_DB_HOST'])
=======
CONNECT_DB = 'mysql+pymysql://{user}:{pw}@{host}:3306/dbwhm'.format(user=os.environ['WHM_DB_USER'],
                                                                    pw=os.environ['WHM_DB_PW'],
                                                                    host=os.environ['WHM_DB_HOST'])
>>>>>>> Stashed changes
