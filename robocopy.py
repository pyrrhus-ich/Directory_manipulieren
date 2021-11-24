from subprocess import call

stamm_src = "C:\\Users\\Menzelf\\GIT_Repos\\"
stamm_dst = "C:\\Users\\Menzelf\\Documents\\Python_Projekte\\"


call(["robocopy", stamm_src, stamm_dst, "/S" ])