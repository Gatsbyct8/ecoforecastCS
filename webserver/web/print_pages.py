#!/usr/bin/python


def print_header():
	print "Content-type: text/html"
	print 
	print '''<head>
  		<link rel="stylesheet" type="text/css" href="style.css">
	</head>'''



def show_add_library_page():
	print_header()
	print "I am library Page"


def show_test_page():
	print_header()
	print "I am test page"


def show_login_page():
	print_header()
	print """<center>
    <h2>Welcome</h2>
    You must identify yourself to use this website. Please enter your:

    <form method="post">
    <table>
      <tr>
        <td>
          Email Address:
        </td>
        <td>
          <input type="text" name="email" size="20"><br>
        </td>
      </tr>

      <tr>
        <td>
          Password:
        </td>
        <td>
          <input type="password" name="pass" size="20"><br>
        </td>
      </tr>

    </table>
        <input type="submit" id="button3" name="login_button" value="login">

    </form> </center>
    """




def show_home_page():
	print_header()
	print ''' <div id="container">
		<form method="post">
			<input type="submit" id="button1" name="show_old" value="Show Old Results">
			<input type="submit" id="button2" name= "new_exp" value=" Run New Experiment">
		</form>
              </div>'''



def show_lib_page():
	print_header()
	print ''' 

	<form  method="post">
	<center>
	<table>
	<col width="300px">
	<col width="300px">
	<tr>
	<h1>Please specify libraries here!</h1>
	</tr>

	<tr>
	<td>
	Put GitHub Libraries "handle/package-name":
	</td>
	<td>
	Put Cran Libraries "package-name"
	</td>
	<tr>
	<td>
	<textarea placeholder="Github Libraries" name="git_libs" style="background:#C9F8A3;width:300px;height:400px;"></textarea>
	</td>
	<td>
	<textarea placeholder="Cran Libraries" name="cran_libs" style="background:#C9F8A3;width:300px;height:400px;"></textarea>
	</td>
	</tr>
	<tr>
	</tr>
	</table>
             <input type="submit" name="code_libs" value="Submit Libraries">
 	</center>
 
      </form>'''




def show_submit_code_page(cran_libs, git_libs):
	print_header()
	print """ 
         <center><form enctype="multipart/form-data"  method="post">

      	 <input type="hidden" name="job_cran_libs" value="{0}">
	 <input type="hidden" name="job_git_libs" value="{1}">

	<table>
	<col width="900px">
	<col width= "300px">
	<tr>
	<td>
	<h1> Sumbit Your Code here!</h1>
	</td>
	</tr>
	<tr>
	<td>
	Your Model Name: <input type="text" name="model_name" value="name">
	</td>
	</tr>
	<tr>
	<td>
	<textarea placeholder="Paste your R code here!!!" name="r_code" style="background:#C9F8A3;width:900px;height:500px;wrap:" hard";"=""></textarea>
        </td>
	<td>
	Do yo want to repeat this Experiment?<br> <input type="radio" name="repeat_it" value="No" selected> No <input type="radio" name="repeat_it" value="Yes"> Yes<br><br>
	Run it every(hours): <input type="text" name="run_interval" value="00"> <br><br>
	Till: <input type="date" name="end_date"><br><br>
	Supporting file (.zip): <input type="file" name="file" > <br><br><br>
	</td>
	</tr>
	</table>
        <input type="submit" name="submit_job" value="Submit Code">

	</form></center> """.format(cran_libs, git_libs)


def show_all_record_page(records, mes):
	print_header()
	print "<h1> All Records </h1>"

	if mes == "redirect":
		print "<p>if you just submitted a job, refresh this page in a while and you will see the results here!</p>"

	print """<center>
        	<table>
        	<tr> <td>User ID</td> <td>Experiment ID</td> <td>Experiment Name</td> <td>Time</td> <td>Preiodic</td> <td>Results</td></tr>
        	"""

	for rec in records:
		print """<tr>
			<td>{0}</td>
			<td>{1}</td>
			<td>{2}</td>
			<td>{3}</td>""".format(rec['user_id'], rec['transaction_id'], rec['model_name'], rec['time'])

		if rec["interval"] != "-1":
			print "<td>Yes</td>"
		else:
                	print "<td>No</td>"

                print """<td>{0}</td>
                	</tr>""".format(rec['result'])

	print """ </center>
		</table>"""

def show_error_page(message):
	print_header()
	print message
