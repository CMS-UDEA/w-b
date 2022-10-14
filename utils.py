import os
from datetime import datetime
import errno
# crear carpetas necesarias
#fecha=datetime.now().strftime('%Y-%m-%d')

def crear_carpetas(fecha,carpeta,outplots):
    try:
        os.mkdir(outplots)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(carpeta)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(carpeta+"/"+str(fecha))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2016")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(carpeta+"/"+str(fecha)+"/2016")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2017")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(carpeta+"/"+str(fecha)+"/2017")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2018")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(carpeta+"/"+str(fecha)+"/2018")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2016/plots")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2016/plots_two")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise 
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2016/scalefactor")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2016/plots_one_two")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2016/plots_several")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2016/plots_sum_back")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2016/plots_eff")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise 
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2016/rc")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise 
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2017/plots")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2017/plots_two")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2017/scalefactor")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2017/plots_one_two")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2017/plots_several")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2017/plots_sum_back")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2017/plots_eff")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise 
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2017/rc")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise 
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2018/plots")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2018/plots_two")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2018/scalefactor")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2018/plots_one_two")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2018/plots_several")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2018/plots_sum_back")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2018/plots_eff")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    try:
        os.mkdir(outplots+"/"+str(fecha)+"/2018/rc")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise 