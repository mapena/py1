from datetime import datetime    
import pypyodbc    
import json
from flask import Flask, render_template, redirect, request ,jsonify 
from flask_swagger_ui import get_swaggerui_blueprint
import decimal
import os
from flask_cors import CORS

app = Flask(__name__)
cors=CORS(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Devops - Estadisticas pipelines"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

### end swagger specific ###

# host="AP_ALMA_MGM\SQL2012"
# database="Mgm_ALM"
# user="usr_alm_read"
# password="123456789"
host=os.environ.get("DB_HOST")
database=os.environ.get("DB_BASE")
user=os.environ.get("DB_USER")
password=os.environ.get("DB_PASS")

def conv_func(list_data):
    dic ={"Id":list_data[0],
	        "Sigla":list_data[1].strip(),
	        "Proyecto":list_data[2].strip(),
	        "Aplicacion":list_data[3].strip(),
	        "Ambiente":list_data[4].strip(),
	        "Resultado":list_data[5].strip(),
	        "QualityGate":list_data[6].strip(),
	        "PipelineCommit":list_data[7].strip(),
        	"ApplicationCommit":list_data[8],
        	"ConfigurationCommit":list_data[9],
        	"Version":list_data[10].strip(),
        	"BaseImageName":list_data[11].strip(),
        	"BaseImageHash":list_data[12].strip(),
        	"ApplicationImage":list_data[13].strip(),
        	"StartDate":list_data[14],
        	"EndDate":list_data[15],
        	"Agent":list_data[16].strip(),
        	"BuildId":list_data[17].strip(),
        	"Lenguaje":list_data[18].strip(),
        	"Aprobador":list_data[19].strip(),
        	"VeracodeTest":list_data[20].strip(),
        	"TipoDespliegue":list_data[21].strip(),
        	"EjecutadoPor":list_data[22].strip(),
        	"URL":list_data[23].strip(),
          "uuid":list_data[24].strip(),
	        "Jenkinsfile":list_data[25].strip(),
	        "Branch":list_data[26].strip(),
	        "DevopsTag":list_data[27].strip()
          }

    return dic

def conv_stage(list_stage):
    dict_stage={
          "Id":list_stage[0], 
        	"uuid":list_stage[1].strip(),
        	"loadGaliciaResult":list_stage[2].strip(), 
        	"loadGaliciaDuration":list_stage[3], 
        	"downloadResult":list_stage[4].strip(),  
        	"downloadDuration":list_stage[5], 
        	"compileResult":list_stage[6].strip(),  
        	"compileDuration":list_stage[7], 
        	"unitTestsResult":list_stage[8].strip(),  
        	"unitTestsDuration":list_stage[9],
        	"sonarTestsResult":list_stage[10].strip(),  
        	"sonarTestsDuration":list_stage[11], 
        	"veracodeTestsResult":list_stage[12].strip(),  
        	"veracodeTestsDuration":list_stage[13], 
        	"generateImageResult":list_stage[14].strip(),  
        	"generateImageDuration":list_stage[15],
        	"loadingEnvironmentsVarsResult":list_stage[16].strip(),  
        	"loadingEnvironmentsVarsDuration":list_stage[17], 
        	"configProbesResult":list_stage[18].strip(), 
        	"configProbesDuration":list_stage[19],
        	"loadAppDynamicsConfigResult":list_stage[20].strip(),  
        	"loadAppDynamicsConfigDuration":list_stage[21],
        	"deployApplicationResult":list_stage[22].strip(),  
          "deployApplicationDuration":list_stage[23],
        	"postActionsResult":list_stage[24].strip(),  
        	"postActionsDuration":list_stage[25],
        	"selectTagResult":list_stage[26].strip(),  
        	"selectTagDuration":list_stage[27],
        	"approvalResult":list_stage[28].strip(),  
        	"approvalDuration":list_stage[29], 
        	"promoteTagResult":list_stage[30].strip(),  
        	"promoteTagDuration":list_stage[31],
        	"integrationTestResult":list_stage[32].strip(),  
        	"integrationTestDuration":list_stage[33],
        	"publishToNexusResult":list_stage[34].strip(),  
        	"publishToNexusDuration":list_stage[35],
        	"prepareResult":list_stage[36].strip(),  
        	"prepareDuration":list_stage[37],
        	"pushNotesGitResult":list_stage[38].strip(),  
        	"pushNotesGitDuration":list_stage[39]
      }

    return dict_stage


def dec_serializer(o):
    if isinstance(o, decimal.Decimal):
        return float(o)

# creating connection Object which will contain SQL Server Connection    
connection = pypyodbc.connect('Driver={{ODBC Driver 17 for SQL Server}};Server={0};Database={1};uid={2};pwd={3};'.format(host,database,user,password))# Creating Cursor    
cursor = connection.cursor() 
cursor.execute('SELECT * FROM "ALM-OpenshiftDeploymentTracking"')
rows=cursor.fetchall()
connection.close() 

connection = pypyodbc.connect('Driver={{ODBC Driver 17 for SQL Server}};Server={0};Database={1};uid={2};pwd={3};'.format(host,database,user,password))# Creating Cursor    
cursor2 = connection.cursor() 
cursor2.execute('SELECT * FROM "ALM-OpenshiftStageTracking"')
rows2=cursor2.fetchall()
connection.close() 

json_stages_output=[]
for w in rows2:
    json_stages_output.append(conv_stage(w))


json_output=[]
for x in rows:
    json_output.append(conv_func(x))

@app.route('/')     
def home():  
    response = jsonify(json_output)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/proyecto/<id>', methods=['GET'])     
def porproj(id):   
    proj = [task for task in json_output if task["Proyecto"] == id]
    response = jsonify(proj)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/veracode/<id>', methods=['GET'])     
def veracode(id):   
    proj = [task for task in json_output if task["VeracodeTest"] == id]
    response = jsonify(proj)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/resultados/<id>', methods=['GET'])     
def resul(id):   
    proj = [task for task in json_output if task["Resultado"] == id]
    response = jsonify(proj)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/uuid/', methods=['GET'])     
def uuid():   
    response = jsonify(json_stages_output)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
                 app.run(debug=True,host='0.0.0.0',port=8080) 
              #  app.run(debug=True)     